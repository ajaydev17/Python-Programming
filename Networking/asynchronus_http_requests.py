"""
Asynchronous HTTP requests allow for non-blocking operations, enabling multiple requests
to be processed simultaneously. In Python, the aiohttp library provides asynchronous
support for HTTP requests. Using async and await, multiple requests can be initiated and
processed concurrently, which is more efficient than synchronous requests.
"""

import aiohttp
import asyncio

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["http://example.com", "http://example.org", "http://example.net"]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for url, result in zip(urls, results):
            print(f"URL: {url}\nContent: {result}\n")


asyncio.run(main())