from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video_as_mp3(youtube_url, output_path):
    try:
        # Download the video
        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).first()
        downloaded_file = video.download(output_path=output_path)
        
        # Convert the downloaded file to mp3
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        audio = AudioSegment.from_file(downloaded_file)
        audio.export(new_file, format="mp3")
        
        # Optionally, remove the original file
        os.remove(downloaded_file)
        
        print(f"Downloaded and converted to mp3: {new_file}")
        return new_file
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=Bcjr-299Qxk"
    output_path = "./"  # Output directory
    download_youtube_video_as_mp3(youtube_url, output_path)
