import datetime
import json
import os

import isodate
from dotenv import load_dotenv
from googleapiclient.discovery import build

from settings import ENV_FILE

load_dotenv(ENV_FILE)


class Youtube:
    __api_key: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    @classmethod
    def get_channel(cls, channel_id):
        return cls.__youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    @classmethod
    def get_video(cls, video_id):
        return cls.__youtube.videos().list(
            part='snippet,statistics,contentDetails,topicDetails',
            id=video_id
        ).execute()

    @classmethod
    def get_playlist(cls, playlist_id):
        return cls.__youtube.playlists().list(
            id=playlist_id,
            part='contentDetails, snippet',
            maxResults=50,
        ).execute()

    @classmethod
    def get_playlist_video_ids(cls, playlist_id):
        ids = []
        playlist = cls.__youtube.playlistItems().list(
            playlistId=playlist_id,
            part='contentDetails',
            maxResults=50,
        ).execute()
        for video in playlist['items']:
            ids.append(video['contentDetails']['videoId'])
        return ids

    @classmethod
    def get_videos_duration(cls, playlist_id) -> datetime.timedelta:
        video_response = cls.__youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(cls.get_playlist_video_ids(playlist_id))
        ).execute()
        delta = datetime.timedelta()
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            delta += duration
        return delta

    @classmethod
    def get_videos_in_playlist(cls, playlist_id):
        video_response = cls.__youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(cls.get_playlist_video_ids(playlist_id))
        ).execute()
        return video_response['items']


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__channel = Youtube.get_channel(self.__channel_id)
        self.__title = self.__channel['items'][0]['snippet']['title']
        self.__description = self.__channel['items'][0]['snippet']['description']
        self.__url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.__subscribers_count = int(self.__channel['items'][0]['statistics']['subscriberCount'])
        self.__video_count = int(self.__channel['items'][0]['statistics']['videoCount'])
        self.__views_count = int(self.__channel['items'][0]['statistics']['viewCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__channel, indent=2, ensure_ascii=False))

    @property
    def title(self) -> str:
        """Геттер возвращает название канала."""
        return self.__title

    @property
    def description(self) -> str:
        """Геттер возвращает описание канала."""
        return self.__description

    @property
    def url(self) -> str:
        """Геттер возвращает url канала."""
        return self.__url

    @property
    def subscribers_count(self) -> int:
        """Геттер возвращает количество подписчиков канала."""
        return self.__subscribers_count

    @property
    def video_count(self) -> int:
        """Геттер возвращает количество видео канала."""
        return self.__video_count

    @property
    def views_count(self) -> int:
        """Геттер возвращает количество просмотров канала."""
        return self.__views_count

    @property
    def channel_id(self) -> str:
        """Геттер возвращает id канала."""
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, id):
        """Сеттер возвращает id канала."""
        print("AttributeError: property 'channel_id' of 'Channel' object has no setter")

    # @classmethod
    # def get_service(cls):
    #     """Класс-метод возвращает объект для работы с YouTube API."""
    #     return cls.__youtube

    def to_json(self, filename) -> None:
        """Метод возвращает в json значения атрибутов экземпляра Channel."""
        data = {
            'channel_id': self.__channel_id,
            'title': self.__title,
            'description': self.__description,
            'url': self.__url,
            'subscribers_count': self.__subscribers_count,
            'video_count': self.__video_count,
            'views_count': self.__views_count
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def __str__(self) -> str:
        return f'{self.__title} ({self.__url})'

    def __add__(self, other: 'Channel') -> int:
        return self.__subscribers_count + other.__subscribers_count

    def __sub__(self, other: 'Channel') -> int:
        return self.__subscribers_count - other.__subscribers_count

    def __ge__(self, other: 'Channel') -> bool:
        return self.__subscribers_count >= other.__subscribers_count
