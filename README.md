# **RECRUITSENSE AI BY CAPSTONE JAYA**

## 1. Deskripsi Singkat
RecruitSense AI adalah sebuah website yang memungkinkan pengguna menganalisis interview hanya dengan menginput video, pertanyaan, dan nilai projek. Sistem menghasilkan keluaran berupa hasil speech to text, cheating detection, interview score, dan final result. Fitur cheating detection menandai video sebagai mencurigakan jika terdapat lebih dari satu orang pada video. Interview score dihitung dengan AI berdasarkan kesesuain jawaban kandidat dan pertanyaan yang ditetapkan pengguna. Pengguna dapat menginput nilai projek dan note, sistem kemudian memberikan keluaran final result berupa semua ringkasan interview dan hasil akhir serta keputusan apakah kandidat layak atau tidak

## 2. Tautan Model dan Fungsi Model
- Model yang digunakan antara lain Yolo, Whisper v3 dan Gemini flash
- Whisperv3 diaplikasikan dengan API KEY yang disediakan oleh Groq : speech to tect
- Gemini flash diaplikasikan dengan API KEY : interview score 
- Yolo berupa model yang disediakan oleh ultralytic dalam format onnx berikut tautannya : https://github.com/pemujacoding/capstone_deploy/blob/main/yolov8n.onnx

## 3. Cara Penggunaan
- Akses web pada tautan capstonedeploy-production-be3a.up.railway.app
- Penggunaan dapat diakses melalui video berikut https://drive.google.com/file/d/10YarXuR9yb0vtwlFu3zXL3Fe-kJzofgA/view?usp=drive_link

## 4. Cara Replikasi
- Unduh semua file : https://github.com/pemujacoding/capstone_deploy
- Sesuaikan connect dengan database yang dimiliki
- Import tabel ke database : https://drive.google.com/file/d/1vFuewH7SPZpFzvJ8SXHOfu5tKfCZ_uZy/view?usp=drive_link
