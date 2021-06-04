# 기본 문법
import youtube_dl

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(['https://www.youtube.com/watch?v=WY5T5hni1X4&t=204s'])

# 함수 사용 문법 (1)
"""
import youtube_dl

# 다운로드가 가능한 모든 format을 불러옵니다.
ydl_opt = {
    'listformats': True
}

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(['https://www.youtube.com/watch?v=WY5T5hni1X4&t=204s'])
"""

# 함수 사용 문법 (2)
"""
import youtube_dl

# 다운로드가 가능한 모든 format을 불러옵니다.
ydl_opt = {

    # format의 번호
    'format': = '18',
    
    # 'best[height <= 480]', 파일 해상도 제한
    # 'best[filesize<10M]', 파일 크기 제한 
    
    # 함수 = 제목, 해상도, 형식
    'outtmpl': = '%(title)s %(resolution)s.%(ext)s'
}

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(['https://www.youtube.com/watch?v=WY5T5hni1X4&t=204s'])
"""