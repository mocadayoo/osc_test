import time
from pythonosc import udp_client

from Utils.lrclib.lyrics import get_lrc_lyrics
from Utils.lrclib.to_json import parse_lrc

artist_name = "ヨルシカ"
track_name = "忘れてください"
lrc_resp = get_lrc_lyrics(artist_name, track_name)
json_lrc = parse_lrc(lrc_resp["syncedLyrics"])

duration_ms = lrc_resp["duration"] * 1000
client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

def send_osc_lyrics(text):
    client.send_message("/chatbox/input", [text, True])
    print(f"[Sent]: {text}")

start_time = time.time() * 1000  # 開始時刻をミリ秒で記録
next_index = 0

try:
    while True:
        elapsed_ms = (time.time() * 1000) - start_time
        
        # 歌詞のlenを超えていないかチェック
        if next_index < len(json_lrc):
            target_lyric = json_lrc[next_index]
            
            # 時間が過ぎていたら送信
            if elapsed_ms >= target_lyric["startTimeMs"]:
                send_osc_lyrics(f"now playing: {track_name} - {artist_name}:\n{target_lyric['text']}")
                next_index += 1
        
        if elapsed_ms >= duration_ms:
            print("曲が終了しました")
            break
            
        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nfin")