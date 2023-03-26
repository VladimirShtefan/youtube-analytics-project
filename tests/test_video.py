import datetime

from src.channel import Channel
from src.playlist import PlayList
from src.video import Video


def test_video(youtube):
    video = Video('test_id_video')
    assert video.url == 'https://www.youtube.com/watch?v=test_id_video'
    assert video.title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert video.id_video == 'test_id_video'
    assert video.views_count == '49441501'
    assert video.likes_count == '976780'
    assert str(video) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_playlist(youtube):
    playlist = PlayList('test_test_test')
    assert playlist.url == 'https://www.youtube.com/playlist?list=test_test_test'
    assert playlist.title == 'Редакция. АнтиТревел'
    assert playlist.total_duration == datetime.timedelta(minutes=60)
    assert playlist.show_best_video == 'https://www.youtube.com/watch?v=9Bv2zltQKQA'


def test_channel(youtube):
    channel = Channel('12345')
    assert channel.url == 'https://www.youtube.com/channel/12345'
    assert channel.channel_id == '12345'
    assert channel.description == 'Здесь задают вопросы'
    assert channel.subscribers_count == 10300000
    assert channel.video_count == 166
    assert channel.views_count == 1973320446

# Остальные тесты по аналогии