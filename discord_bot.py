import requests
import os


WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")


def send_message(content):
    if not WEBHOOK_URL:
        return

    requests.post(
        WEBHOOK_URL,
        json={"content": content},
        timeout=10
    )
