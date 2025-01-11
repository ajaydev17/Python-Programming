import asyncio
import aiohttp

# fetching the data
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['http://example.com', 'http://example.org']
    tasks = [fetch(url) for url in urls]
    data = await asyncio.gather(*tasks)
    print(data)

# running the async main function
asyncio.run(main())

