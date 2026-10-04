import asyncio
import time
async def brewing_chai(name):
    print(f"Brewing {name} chai...")
    await asyncio.sleep(2)
    # time.sleep(2)
    print(f"{name} chai is ready")


async def main():
   await asyncio.gather(
       brewing_chai("Masala"),
       brewing_chai("Green"),
       brewing_chai("Ginger"),
   )

asyncio.run(main())