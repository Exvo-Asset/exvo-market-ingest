import asyncio


class YahooProvider:
async def fetch_latest(self, symbols):
# placeholder values
await asyncio.sleep(0.01)
from datetime import datetime
ts = datetime.utcnow().isoformat() + 'Z'
return [{'symbol': s, 'ts': ts, 'price': 100.0 + i} for i,s in enumerate(symbols)]
