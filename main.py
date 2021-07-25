from datetime import datetime as dt
from typing import Optional

from fastapi import FastAPI, Depends

from file_engine import MovesData
from exceptions import ActivityNotFound, InvalidDateError
from dependencies import Period, date_kwargs
from query_processing import QueryParamsProcessor


app = FastAPI()
md = MovesData()


@app.get('/')
def read_root():
    return {'message': "Welcome to moves_api!"}


@app.get('/v0/daily/activities/{YYYYMMDD}')
async def get_daily_activity(YYYYMMDD: str):
    try:
        dt.strptime(YYYYMMDD, f"%Y%m%d")
    except ValueError:
        raise InvalidDateError(f"Invalid date format for YYYYMMDD: {YYYYMMDD}")

    data = await md.get_json_v0(YYYYMMDD)
    if data:
        return data
    raise ActivityNotFound(f"No activities for date: {YYYYMMDD}")


@app.get('/v1/activities')
async def get_moves_data(period: Optional[Period] = None,
                         date: dict = Depends(date_kwargs)):
    processor = QueryParamsProcessor(period, date)
    data = await md.get_json_v1(processor())
    if data:
        return data
    raise ActivityNotFound(detail={
        "message": "Activity not found.",
        "period": period.value if period else "",
        **date
    })
