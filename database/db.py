import asyncpg

class Database:
    def __init__(self):
        self.pool = None

    async def connection(self):
        self.pool = await asyncpg.create_pool(
            user="postgres",
            password="1234",
            database="logicmartbot",
            host="localhost"
        )

    async def is_user_exists(self, user_id):
        async with self.pool.acquire() as conn:
            res = await conn.fetchrow(
                "SELECT * FROM users WHERE user_id=$1", user_id
            )
            return bool(res)

    async def add_user(self, user_id, name, surename, age, phone):
        async with self.pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO users(user_id,name,surename,age,phone) VALUES($1,$2,$3,$4,$5)",
                user_id, name, surename, age, phone
            )

    async def get_user(self, user_id):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(
                "SELECT * FROM users WHERE user_id=$1", user_id
            )
        
    async def get_user_role(self, telegram_id):
        query = """SELECT role FROM users WHERE telegram_id=$1"""
        return await self.pool.fetchval(query, telegram_id)
 