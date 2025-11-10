import asyncio
from src.providers.yahoo_provider import YahooProvider


async def run_test():
prov = YahooProvider()
snaps = await prov.fetch_latest(['AAPL'])
assert snaps[0]['symbol'] == 'AAPL'


if __name__ == '__main__':
asyncio.run(run_test())
