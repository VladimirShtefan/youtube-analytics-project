import datetime
from unittest.mock import Mock

import pytest

from src.channel import Youtube


@pytest.fixture
def data_channel():
    return {
        'items': [
            {
                'id': 'UCMCgOm8GZkHp8zJ6l7_hIuA',
                'snippet': {
                    'title': 'вДудь',
                    'description': 'Здесь задают вопросы',
                },
                'statistics': {
                    'viewCount': '1973320446',
                    'subscriberCount': '10300000',
                    'hiddenSubscriberCount': False,
                    'videoCount': '166'
                }
            }
        ]
    }


@pytest.fixture
def data_video():
    return {
        'items': [
            {
                'id': '9lO06Zxhu88',
                'snippet': {
                    'channelId': 'UCMCgOm8GZkHp8zJ6l7_hIuA',
                    'title': 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)',
                    'description': 'TestVideo',
                    },
                    'channelTitle': 'вДудь',
                    'categoryId': '22',
                'statistics': {
                    'viewCount': '49441501',
                    'likeCount': '976780',
                    'favoriteCount': '0',
                    'commentCount': '79485'
                },
            }
        ],
        }


@pytest.fixture
def data_playlist():
    return {
        'items': [
            {
                'id': 'PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb',
                'snippet': {
                    'channelId': 'UC1eFXmJNkjITxPFWTy6RsWg',
                    'title': 'Редакция. АнтиТревел',
                    'description': 'TestDescriptoin',

                    'channelTitle': 'Редакция',
                    'localized': {
                        'title': 'Редакция. АнтиТревел',
                        'description': 'TestDescription'
                    }
                },
                'contentDetails': {'itemCount': 5}}]}


@pytest.fixture
def data_video_in_playlist():
    return [
        {
            'id': '4jRSy-_CLFg',
            'contentDetails': {
                'duration': 'PT36M24S',
                'dimension': '2d',
                'definition': 'hd',
                'caption': 'false',
                'licensedContent': True,
                'contentRating': {},
                'projection': 'rectangular'
            },
            'statistics': {
                'viewCount': '836682',
                'likeCount': '43679',
                'favoriteCount': '0',
                'commentCount': '3421'
            }
        },
        {
            'id': 'XG6pQ9n4kr0',
            'contentDetails': {
                'duration': 'PT49M10S',
                'dimension': '2d',
                'definition': 'hd',
                'caption': 'false',
                'licensedContent': True,
                'contentRating': {},
                'projection': 'rectangular'
            },
            'statistics': {
                'viewCount': '769600',
                'likeCount': '44001',
                'favoriteCount': '0',
                'commentCount': '4912'
            }
        },
        {
         'id': 'cIs7N8B300M',
         'contentDetails': {
             'duration': 'PT46M11S',
             'dimension': '2d',
             'definition': 'hd',
             'caption': 'false',
             'licensedContent': True,
             'contentRating': {},
             'projection': 'rectangular'
         },
         'statistics': {
             'viewCount': '870242',
             'likeCount': '45523',
             'favoriteCount': '0',
             'commentCount': '4790'
         }
         },
        {
         'id': 'S7Ri5-9WHQY',
         'contentDetails': {
             'duration': 'PT46M32S',
             'dimension': '2d',
             'definition': 'hd',
             'caption': 'false',
             'licensedContent': True,
             'contentRating': {},
             'projection': 'rectangular'
         },
         'statistics': {
             'viewCount': '1184903',
             'likeCount': '63498',
             'favoriteCount': '0',
             'commentCount': '9753'
         }
         },
        {
         'id': '9Bv2zltQKQA',
         'contentDetails': {'duration': 'PT42M44S',
                            'dimension': '2d',
                            'definition': 'hd',
                            'caption': 'false',
                            'licensedContent': True,
                            'contentRating': {},
                            'projection': 'rectangular'},
         'statistics': {'viewCount': '1881043', 'likeCount': '175920', 'favoriteCount': '0', 'commentCount': '46492'}}]


@pytest.fixture
def youtube(data_channel, data_video, data_playlist, data_video_in_playlist):
    mock_object = Youtube
    mock_object.get_channel = Mock(return_value=data_channel)
    mock_object.get_video = Mock(return_value=data_video)
    mock_object.get_playlist = Mock(return_value=data_playlist)
    mock_object.get_playlist_video_ids = Mock(return_value=[1, 2, 3, 4])
    mock_object.get_videos_duration = Mock(return_value=datetime.timedelta(minutes=60))
    mock_object.get_videos_in_playlist = Mock(return_value=data_video_in_playlist)
    return mock_object
