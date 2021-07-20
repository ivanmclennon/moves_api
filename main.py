from datetime import datetime as dt
from typing import Any, Optional, Dict

from fastapi import FastAPI, HTTPException

from file_engine import MovesData


class InvalidDateError(HTTPException):

    status_code: int = 400
    headers: Optional[Dict[str, Any]] = {}

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail=detail, headers=self.headers)


class ActivityNotFound(HTTPException):

    status_code: int = 404
    headers: Optional[Dict[str, Any]] = {}

    def __init__(self, detail: str) -> None:
        super().__init__(self.status_code, detail=detail, headers=self.headers)


app = FastAPI()
md = MovesData()


@app.get('/')
def read_root():
    return {'message': "Welcome to moves_api_v0!"}


@app.get('/v0/daily/activities/{YYYYMMDD}')
async def get_daily_activity(YYYYMMDD: str):
    try:
        dt.strptime(YYYYMMDD, f"%Y%m%d")
    except ValueError:
        raise InvalidDateError(f"Invalid date format for YYYYMMDD: {YYYYMMDD}")

    data = await md.get_json(YYYYMMDD)
    if data:
        return data
    raise ActivityNotFound(f"No activities for date: {YYYYMMDD}")
