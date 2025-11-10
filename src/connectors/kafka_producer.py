class KafkaProducer:
def __init__(self, topic='market-snapshots'):
self.topic = topic


async def send_batch(self, records):
# stub: in real code, push to kafka
print(f"[kafka] sending {len(records)} records to {self.topic}")
return True
