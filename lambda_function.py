import os
import requests
import slack
import random

GREETINGS = [
  "Here is some inspiration for the day:",
  "Just a little inspiration for you:",
  "Here's something to think about:",
  "Want some inspiration? Look no further:"
]

def send_slack_msg(client, msg):
  client.chat_postMessage(
    channel=os.environ["channel"],
    text=msg,
    as_user=True
  )

def send_slack_img(client, img_url):
  client.chat_postMessage(
    channel=os.environ["channel"],
    attachments=[{"text": "", "title": "", "image_url": img_url}],
    as_user=True
  )

def get_image_url():
  req = requests.get("https://inspirobot.me/api?generate=true")
  return req.text

def lambda_handler(event, context):
  client = slack.WebClient(token=os.environ["slack_token"])
  img_url = get_image_url()
  send_slack_msg(client, random.choice(GREETINGS))
  send_slack_img(client, img_url)


if __name__ == "__main__":
  lambda_handler(None, None)