import redis
import os

DB_CONFIG = {
    "host": os.getenv("REDIS_HOST", "localhost"),
    "port": os.getenv("REDIS_PORT", "6379"),
            }


def get_connection():
    r = redis.Redis(**DB_CONFIG, decode_responses=True)
    return r


def add_item(data: dict):
    r = get_connection()
    ip = next(iter(data))
    coords = data[ip]
    r.hset(f"ip:{ip}", mapping=coords)
    r.close()

