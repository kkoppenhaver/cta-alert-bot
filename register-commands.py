from dotenv import load_dotenv
import os
import requests

load_dotenv()

APP_ID    = os.getenv('APP_ID')
GUILD_ID  = os.getenv('GUILD_ID')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# When bot is more developed, register commands globally
# url = f'https://discord.com/api/v8/applications/{APP_ID}/commands'
url = f'https://discord.com/api/v8/applications/{APP_ID}/guilds/{GUILD_ID}/commands'

json = {
  'name': 'transitalert',
  'description': 'Sets a transit alert for a bus or train line.',
  'options': [
    {
        "name": "route",
        "description": "The bus or train route that you want an alert for.",
        "type": 3,
        "required": True,
    },
    {
        "name": "time",
        "description": "When is the latest you can get on the bus or train? (e.g 12:15PM)",
        "type": 3,
        "required": True,
    },
    {
        "name": "notice",
        "description": "How much advance notice do you want before the bus or train arrives? (e.g. 5mins)",
        "type": 3,
        "required": True,
    }
  ] 
}

response = requests.post(url, headers={
  'Authorization': f'Bot {BOT_TOKEN}'
}, json=json)

print(response.json())