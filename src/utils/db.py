import asyncio
from prisma import Prisma

async def main() -> None:
    try:
        db = Prisma()
        await db.connect()

        # write your queries here

        await db.disconnect()
    except:
        print("[Database Connection Error]: Failed connecting to DB.")
        

if __name__ == '__main__':
    asyncio.run(main())