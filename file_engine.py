import os
import json


class MovesData():
    """
    Class for accessing the moves-api data local directories.
    """
    BASE_DIR: str = "C:\\Users\\madpe\\moves_json\\json"

    def __init__(self, base_dir: str = None) -> None:
        """
        Initialize MovesData object.
        :param base_dir:(optional) Base directory containing json api data.
        """
        if base_dir is not None and os.path.exists(base_dir):
            self.BASE_DIR = base_dir

    async def get_json_v0(self, date: str) -> dict:
        """
        Get json data for v0 api from daily/activities directory.
        Returns {} if not found.
        :param date: date in str format YYYYMMDD
        """
        filename = f"activities_{date}.json"
        path = os.path.join(self.BASE_DIR, os.sep.join(
            ['daily', 'activities', filename]))
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                json_response = json.load(f)
            return json_response[0]
        return {}

    async def get_json_v1(self, filepath: str) -> dict:
        """
        Get json data for v1 api from base_dir.
        Returns {} if not found.
        :param filepath: path to the requested file.
        """
        path = os.sep.join([self.BASE_DIR, filepath])
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                json_response = json.load(f)
            return json_response
        return {}
