from youtube_search import YoutubeSearch
from youtube_transcript_api import YouTubeTranscriptApi

def search(query, max_results=30):
    results = YoutubeSearch(query, max_results).to_dict()
    print(f"> Retrieved {len(results)} videos from YouTube")
    return results

def get_transcript(video_id):
    transcript =  YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([x['text'] for x in transcript])
    return text