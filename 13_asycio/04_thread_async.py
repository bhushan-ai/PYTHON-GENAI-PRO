import asyncio
import time
from concurrent.futures import ThreadPoolExecutor   

def check_stock(item):
    print(f"Checkin {item} in store...")
    time.sleep(3)# Blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop() 
    with ThreadPoolExecutor() as pool:
        # the run_in_executer() let asyncio run async fun but in another thread, we r not touching main thread 
        result = await loop.run_in_executor(pool,check_stock,"Masala chai")
        print(result)

asyncio.run(main())   