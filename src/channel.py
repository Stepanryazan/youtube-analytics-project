from googleapiclient.discovery import build
import isodate
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv('../.env')


class Channel:
    """Класс для ютуб-канала"""
    apy_key: str = os.getenv('YT_APY_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        print(self.apy_key)
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=self.apy_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        pprint(channel)
