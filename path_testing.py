import requests
from file_engine import MovesData


test_cases_v0 = [
    "v0/daily/activities/20201010",
    "v0/daily/activities/19971012",
    "v0/daily/activities/20142459",
    "v0/daily/activities/20140707",
]

test_cases_v1 = [
    "daily/activities?year=2015&month=9&day=6",
    "daily/activities?year=2016&month=3&day=23",
    "daily/activities?year=2022&month=9&day=6",
    "daily/activities?year=1997&month=11&day=27",
    "daily/activities?year=654987&month=165765126&day=6540",
    "daily/activities?year=null&month=null&day=null",
]

if __name__ == "__main__":
    print('testing api')
    print('v0')
    for case in test_cases_v0:
        url = "http://localhost:8000/" + case
        res = requests.get(url)
        print(res)