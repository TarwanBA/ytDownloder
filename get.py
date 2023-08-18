from pytube import YouTube
import time

def progress_hook(stream, chunk, bytes_remaining):
    total      = stream.filesize
    bd         = total - bytes_remaining
    presentasi = (bd / total) * 100
    print(f"Sementaras Download: {presentasi:.2f}%")

def download_video(url, output_path):
    waktu_mulai = time.time()

    yt = YouTube(url, on_progress_callback=progress_hook)
    video = yt.streams.get_highest_resolution()
    video.download(output_path)

    waktu_berakhir = time.time()
    total_waktu = waktu_berakhir - waktu_mulai
    print(f"Total waktu untuk download: {total_waktu:.2f} seconds")

    # cetak deskripsi
    video_description = yt.description
    print(f"Deskripsi video:\n{video_description}")

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=2OiKj0IqJsw"
    output_path = "ddd"
    download_video(video_url, output_path)
