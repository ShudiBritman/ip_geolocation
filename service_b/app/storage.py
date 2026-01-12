import redis
import os

DB_CONFIG = {
    "host": os.getenv("REDIS_HOST", "localhost"),
    "port": os.getenv("REDIS_PORT", "6379"),
            }
r = redis.Redis(DB_CONFIG, decode_responses=True)