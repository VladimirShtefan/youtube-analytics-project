import datetime

from src.playlist import PlayList
from src.video import Video

if __name__ == '__main__':
    video = Video('9Bv2zltQKQA')
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    assert pl.title == "Редакция. АнтиТревел"
    assert pl.url == "https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb"

    duration = pl.total_duration
    assert str(duration) == "3:41:01"
    assert issubclass(type(duration), datetime.timedelta)
    assert duration.total_seconds() == 13261.0

    assert pl.show_best_video() == "https://www.youtube.com/watch?v=9Bv2zltQKQA"

# "https://youtu.be/9Bv2zltQKQA"