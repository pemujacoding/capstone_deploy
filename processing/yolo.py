import cv2
import numpy as np
import onnxruntime as ort

# Load ONNX model
session = ort.InferenceSession(
    "yolov8n.onnx",
    providers=["CPUExecutionProvider"],
    sess_options=ort.SessionOptions()
)
session.set_providers(["CPUExecutionProvider"], [{'intra_op_num_threads': 2}])
input_name = session.get_inputs()[0].name
input_shape = session.get_inputs()[0].shape  # (1, 3, H, W)
IMG_H, IMG_W = input_shape[2], input_shape[3]

def preprocess(frame):
    img = cv2.resize(frame, (IMG_W, IMG_H))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))  # HWC → CHW
    img = np.expand_dims(img, axis=0)
    return img

def postprocess(outputs, orig_shape, conf_thresh=0.3, class_id=0):
    pred = outputs[0][0]  # (N, 6 atau lebih) — x1, y1, x2, y2, score, cls
    results = []

    h, w = orig_shape[:2]

    for det in pred:
        if len(det) < 6:
            continue  # skip kalau format tidak sesuai

        x1, y1, x2, y2, score, cls = det[:6]

        if score < conf_thresh:
            continue
        if int(cls) != class_id:
            continue

        results.append([
            int(x1 * w / IMG_W),
            int(y1 * h / IMG_H),
            int(x2 * w / IMG_W),
            int(y2 * h / IMG_H)
        ])
    return results

def run_detection(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        cap = cv2.VideoCapture(video_path, cv2.CAP_FFMPEG)
        if not cap.isOpened():
            raise RuntimeError("Gagal membuka video")

    fps_real = cap.get(cv2.CAP_PROP_FPS)
    FPS = int(round(fps_real)) if fps_real > 0 else 30
    SKIP = max(1, FPS // 2)

    cheat_person_count = 0
    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_id += 1
        if frame_id % SKIP != 0:
            continue

        # ONNX inference
        inp = preprocess(frame)
        outputs = session.run(None, {input_name: inp})
        persons = postprocess(outputs, frame.shape)

        if len(persons) > 1:
            cheat_person_count += 1

    cap.release()

    return {
        "banyak_orang_terdeteksi": cheat_person_count,
        "final": "MENCURIGAKAN" if cheat_person_count > 0 else "TIDAK_MENCURIGAKAN"
    }