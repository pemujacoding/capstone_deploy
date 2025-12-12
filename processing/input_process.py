from moviepy import VideoFileClip
import tempfile
import os
import datetime
import model.input as conn_input
import subprocess
from . import yolo
from . import stt

def compress_video(input_path, output_path):
    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-vcodec", "libx264",
        "-crf", "28", 
        "-preset", "veryfast",
        "-acodec", "aac",
        output_path
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("FFmpeg error:", result.stderr.decode())
        return False

    return True

def extract_audio(video_path, audio_path):
    try:
        cmd = [
            "ffmpeg",
            "-y",                     # overwrite output
            "-i", video_path,         # input
            "-vn",                    # no video
            "-acodec", "pcm_s16le",   # WAV format
            "-ar", "16000",           # sampling rate
            "-ac", "1",               # mono
            audio_path
        ]

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            print("FFmpeg error:", result.stderr.decode())
            return False

        return os.path.exists(audio_path) and os.path.getsize(audio_path) > 0

    except Exception as e:
        print("Exception:", e)
        return False

def save_video_temp(video_bytes):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tmp.write(video_bytes)
    tmp.close()
    return tmp.name

def create_temp_path(suffix):
    fd, path = tempfile.mkstemp(suffix=suffix)
    os.close(fd)  # penting: file descriptor ditutup biar tidak terkunci
    return path

    
def input_files(video_path,filename,ext,interview_id,question):
    if ext not in [".mp4", ".webm"]:
        print("Ext invalid")
        return None, None

    compressed_path = create_temp_path(".mp4")
    audio_path = create_temp_path(".wav")

    try:
        # compress input video
        if not compress_video(video_path, compressed_path):
            print("compression failed")
            return None, None

        # extract audio
        if not extract_audio(compressed_path, audio_path):
            print("audio extraction failed")
            return None, None

        # load files
        with open(compressed_path, "rb") as f:
            compressed_bytes = f.read()
        with open(audio_path, "rb") as f:
            audio_bytes = f.read()

        # run ai
        result_cd = yolo.run_detection(compressed_path)
        result_stt = stt.speech_to_text(audio_bytes, os.path.basename(video_path), question)

        conn_input.insert_video_bytes(
            filename,
            result_cd,
            result_stt,
            interview_id
        )

        return result_cd, result_stt

    finally:
        for p in [compressed_path, audio_path]:
            if os.path.exists(p):
                os.remove(p)


def final_result(project_score,interview_score,interviews_checklist,candidate_id,candidate_name,candidate_photo,project_name,notes) :
        # Hitung total dengan bobot
        total_score = round((project_score * 0.715) + (interview_score * 0.285), 2)
        
        
        if total_score >= 90:
            recommendation = "PASS - Candidate exceeds expectations and is recommended for hiring based on industry standards."
        elif 70 <= total_score < 90:
            recommendation = "CONSIDERED - Candidate meets basic requirements but may need further evaluation or training for industry fit."
        else:
            recommendation = "REJECTED - Candidate does not meet the required thresholds for this role based on industry benchmarks."
        
        # Buat JSON lengkap
        final_data = {
            "assessorProfile": {
                "id": candidate_id,
                "name": candidate_name,
                "photoUrl": candidate_photo
            },
            "decision": "Need Human",
            "reviewedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "scoresOverview": {
                "project": project_score,
                "interview": interview_score,
                "total": total_score
            },
            "reviewChecklistResult": {
                "project": [project_name],
                "interviews": interviews_checklist
            },
            "Overall notes": notes,
            "recommendation": recommendation
        }
        return final_data