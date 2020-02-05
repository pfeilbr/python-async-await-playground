import asyncio
import aiohttp
import time


async def do_work():
    print("hello")
    sleep_in_seconds = 1
    print("sleeping {} seconds ...".format(sleep_in_seconds))
    await asyncio.sleep(2)
    print("world")


async def do_work_example():
    print(f"started at {time.strftime('%X')}")
    await do_work()
    print(f"finished at {time.strftime('%X')}")


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def http_example():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://postman-echo.com/get')
        print(html)


async def main():
    await asyncio.gather(
        do_work_example(),
        http_example(),
    )

if __name__ == '__main__':
    asyncio.run(main())
