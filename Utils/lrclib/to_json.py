import re

from .models import syncedLyricsList

def parse_lrc(lrc_text) -> syncedLyricsList:
    if not lrc_text:
        return []

    lyrics_list = []
    # [00:22.00]あの風 をmin, sec, tex, に分離するための正規表現
    pattern = re.compile(r'\[(\d+):(\d+\.\d+)\](.*)')

    for line in lrc_text.split('\n'):
        match = pattern.match(line)
        if match:
            minutes = int(match.group(1))
            seconds = float(match.group(2))
            text = match.group(3).strip()
            
            # 分、秒を足して秒に変換 
            lyrics_ms = (minutes * 60 + seconds) * 1000
            lyrics_list.append({
                "startTimeMs": lyrics_ms,
                "text": text
            })
    
    return lyrics_list