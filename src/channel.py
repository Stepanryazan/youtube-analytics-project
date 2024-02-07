from googleapiclient.discovery import build
import isodate
import os
from dotenv import load_dotenv
from pprint import pprint
import json

load_dotenv('../.env')

apy_key: str = os.getenv('YT_APY_KEY')

moscowpython_list = []


class Channel:
    """Класс для ютуб-канала"""
    __youtube = build('youtube', 'v3', developerKey=apy_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.__youtube.channels().list(id =self.__channel_id, part ='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pprint(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, filename):
        data = json.dumps(self.channel)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.channel['items'][0]['snippet']['title']

    @property
    def video_count(self):
        return self.channel['items'][0]['statistics']['videoCount']

    @property
    def url(self):
        return self.channel['items'][0]['snippet']['thumbnails']

    @classmethod
    def get_service(cls):
        return cls.__youtube


