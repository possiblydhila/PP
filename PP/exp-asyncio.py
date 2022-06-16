import asyncio
import time
#secara concurrent / proses secara async pake asyncio module

async def count():
    print('satu')
    await asyncio.sleep(3)
    print('dua')
    await asyncio.sleep(1)
    print('tiga')
async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} dieksekusi dalam {elapsed:0.2f} detik")

# fungsi hitung2 dan hitung3 dijalankan ketika hitung1 sedang await.asyncio 1s