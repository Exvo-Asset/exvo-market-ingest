import asyncio
from providers.yahoo_provider import YahooProvider
from connectors.kafka_producer import KafkaProducer


async def poll_loop():
prov = YahooProvider()
producer = KafkaProducer(topic='market-snapshots')
while True:
snaps = await prov.fetch_latest(['AAPL','MSFT'])
await producer.send_batch(snaps)
await asyncio.sleep(5)


if __name__ == '__main__':
asyncio.run(poll_loop())
