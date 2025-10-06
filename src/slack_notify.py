import os, requests
from dotenv import load_dotenv

load_dotenv()


def send_slack_alert(message):
    webhook = os.getenv("SLACK_WEBHOOK")
    requests.post(webhook, json={"text": message})
