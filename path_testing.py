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


start_time = time.time()


async def main():
    print('testing moves_api_v0')
    async with aiohttp.ClientSession() as session:

        for case in test_cases_v0:
            url = f"http://localhost:8000/{case}"
            print(f"Requesting {url}")
            async with session.get(url) as res:
                print(res.status)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
