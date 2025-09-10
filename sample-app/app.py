import logging
import json
import time
import random
import sys

logger = logging.getLogger("sample-app")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    while True:
        log = {
            "app": "sample-app",
            "level": random.choice(["INFO", "WARN", "ERROR"]),
            "message": "Hello from sample app",
            "value": random.randint(1, 100),
        }
        logger.info(json.dumps(log))
        time.sleep(1)