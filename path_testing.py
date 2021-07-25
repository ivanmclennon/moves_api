from typing import List
import aiohttp
import asyncio
import time


test_cases_v0 = [
    "v0/daily/activities/20201010",
    "v0/daily/activities/19971012",
    "v0/daily/activities/20142459",
    "v0/daily/activities/;ALSKJGFH",
    "v0/daily/activities/20140724",
    "v0/daily/activities/20140612",
]

test_cases_v1 = [

    "v1/activities?period=yearly&year=2015&month=6&day=12",
    "v1/activities?period=yearly&year=2015&month=6",
    "v1/activities?period=yearly&year=2015",
    "v1/activities?period=yearly",

    "v1/activities?period=monthly&year=2015&month=6&day=12",
    "v1/activities?period=monthly&year=2015&month=6",
    "v1/activities?period=monthly&year=2015",
    "v1/activities?period=monthly",

    "v1/activities?period=weekly&year=2015&month=10&day=10",
    "v1/activities?period=weekly&year=2015&month=10",
    "v1/activities?period=weekly&year=2015",
    "v1/activities?period=weekly",

    "v1/activities?period=daily&year=2016&month=6&day=12",
    "v1/activities?period=daily&year=2016&month=6",
    "v1/activities?period=daily&year=2016",
    "v1/activities?period=daily",

    "v1/activities?period=daily&year=gas&month=6&day=12",
    "v1/activities?period=monthly&year=2014&month=0986",
    "v1/activities?period=daily&year=20141212",
    "v1/activities?period=perdaily",
    "v1/activities?period=None",
    "v1/activities?period=null",

    "v1/activities?year=2015&month=2&day=3",
    "v1/activities?year=2016&month=2",
    "v1/activities?year=2017",
    "v1/activities",
]


async def get_request_result(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as res:
        print(f"Requested {url}")
        print(f"Response code {res.status}")
        print("")


async def main(test_cases: List[str]):
    print(f'Testing api...')
    print(f"Testing {len(test_cases)} cases...")
    print("")
    async with aiohttp.ClientSession() as session:
        tasks = []
        for case in test_cases:
            url = f"http://localhost:8000/{case}"
            task = asyncio.create_task(get_request_result(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)
        print(f"Got {len(tasks)} results.")

start_time = time.time()

asyncio.run(main(test_cases_v1))

print("--- %s seconds ---" % (time.time() - start_time))
