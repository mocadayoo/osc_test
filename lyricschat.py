from pythonosc import udp_client

from Utils.lrclib.play import play_lyrics
from Utils.lrclib.lyrics import get_lrc_lyrics
from Utils.lrclib.to_json import parse_lrc
from Utils.lrclib.models import syncedLyric, lrcJson

artist_name = "ヨルシカ"
track_name = "忘れてください"
lrc_json = get_lrc_lyrics(artist_name, track_name)
lrc_json["syncedLyrics"] = parse_lrc(lrc_json["syncedLyrics"])

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

def send_osc_lyrics(lyric: syncedLyric , lrc_json: lrcJson, _):
    text = (f"now playing: {lrc_json['trackName']} - {lrc_json['artistName']}:\n{lyric['text']}")
    client.send_message("/chatbox/input", [text, True])
    print(f"[Sent]: {text}")

try:
    play_lyrics(lrc_json, send_osc_lyrics)
except KeyboardInterrupt:
    print("\nfin")