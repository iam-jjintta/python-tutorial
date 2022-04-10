
# pytube: YouTube 동영상을 다운로드하기 위한 가볍고 종속성이 없는 라이브러리 및 명령줄 유틸리티
# 해당 라이브러리를 사용하기 위해서는 'pip' 명령어를 통해 설치해야 한다.
# 설치 명령어: pip install pytube
from pytube import YouTube


# 노래: < 무직전생 ~이세계에 갔으면 최선을 다한다~ OST :: 머나먼 자장가 >
# 동영상 제목: TVアニメ『無職転生』第19話ノンクレジットOPムービー／OPテーマ：「遠くの子守の唄」大原ゆい子
url = 'https://www.youtube.com/watch?v=d79iZcngOGQ'
# YouTube 객체를 생성한다.
yt = YouTube(url)

# 스트리밍 데이터 프로퍼티를 가져온다.
streams = yt.streams
# 스트리밍 데이터 중에서 mp4에 해당하는 스트리밍 데이터만을 필터링하여 가져온다.
streams = streams.filter(file_extension='mp4', progressive=True)
# 필터링한 스트리밍 데이터들을 resolution으로 정렬한다.
streams = streams.order_by('resolution')
streams = streams.desc()

# mp4 스트리밍 데이터를 가져온다.
mp4 = streams.first()
# 가져온 mp4 스트리밍 데이터를 다운로드 한다.
mp4.download()
