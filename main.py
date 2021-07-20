import os
from datetime import datetime as dt

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from file_engine import MovesData


app = FastAPI()
md = MovesData()


@app.get('/')
def read_root():
    return {'message': "Welcome to moves_api!"}

@app.get('/v0/daily/activities/{date_YYYYMMDD}')
def read_item(date_YYYYMMDD: str):
    return md.get_daily_activity(date_YYYYMMDD)
