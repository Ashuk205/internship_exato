from youtube_transcript_api import YouTubeTranscriptApi as yta  # type: ignore
 
video_id = "1UyQaR8pvjk"
 
try:
    transcript = yta.get_transcript(video_id)
 
   
    transcript_parts = [entry['text'] for entry in transcript]
 
   
    final_tra = " ".join(transcript_parts)
 
    print(final_tra)
 
except Exception as e:
    print(f"An error occurred: {e}")