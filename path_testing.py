from file_engine import MovesData


test_cases = [
    "daily/activities?year=2015&month=9&day=6",
    "daily/activities?year=2016&month=3&day=23",
    "daily/activities?year=2022&month=9&day=6",
    "daily/activities?year=1997&month=11&day=27",
    "daily/activities?year=654987&month=165765126&day=6540",
    "daily/activities?year=null&month=null&day=null",
]

md = MovesData()
md()