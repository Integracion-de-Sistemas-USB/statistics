import motor.motor_asyncio

MONGODB_URL = "mongodb://localhost:27017/stats"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

database = client.python_db