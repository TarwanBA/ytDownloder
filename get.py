from pytube import YouTube
import time

def progress_hook(stream, chunk, bytes_remaining):
    total      = stream.filesize
    bd         = total - bytes_remaining
    presentasi = (bd / total) * 100
    print(f"Sementara Download: {presentasi:.2f}%")

def download_video(url, output_path):
    waktu_mulai = time.time()

    yt = YouTube(url, on_progress_callback=progress_hook)
    video = yt.streams.get_highest_resolution()
    video.download(output_path)

    waktu_berakhir = time.time()
    total_waktu = waktu_berakhir - waktu_mulai
    print(f"Total waktu untuk download: {total_waktu:.2f} detik")

    # Simpan deskripsi dalam file .txt
    video_title = yt.title
    video_description = yt.description

    file_name = f"deskripsi_{video_title}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(video_description)

    print(f"Deskripsi video disimpan dalam file: {file_name}")

if __name__ == "__main__":
    video_url = "https://www.youtube.com/*******"
    output_path = "***"
    download_video(video_url, output_path)
