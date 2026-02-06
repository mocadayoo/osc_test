import time
from typing import Callable

from .models import lrcJson, syncedLyric

def play_lyrics(lrc_json: lrcJson, callBackFn: Callable[[syncedLyric, lrcJson, int], None]) -> bool:
    syncedLyrics = lrc_json["syncedLyrics"]
    duration_ms = lrc_json["duration"] * 1000
    start_time = time.time() * 1000  # 開始時刻をmsで保存
    next_index = 0

    while True:
        elapsed_ms = (time.time() * 1000) - start_time
        
        # 歌詞のlenを超えていないかチェック
        if next_index < len(syncedLyrics):
            time_lyric = syncedLyrics[next_index]
            
            # 時間が過ぎていたら送信
            if elapsed_ms >= time_lyric["startTimeMs"]:
                callBackFn(time_lyric, lrc_json, next_index)
                next_index += 1
        
        if elapsed_ms >= duration_ms:
            print("曲が終了しました")
            break
            
        time.sleep(0.01)

    return True