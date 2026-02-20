import time


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

# time.time()возвращает уникальный таймстамп.
# Это гарантирует, что наш email будет всегда уникален в любой момент времени.