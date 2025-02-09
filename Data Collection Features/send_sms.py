# Download the helper library from https://www.twilio.com/docs/python/install
import os
from dotenv import load_dotenv
from twilio.rest import Client # type: ignore

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]

# account_sid = "AC72d20417b3e6ca6ef342e275294984a2"

auth_token = os.environ["TWILIO_AUTH_TOKEN"]

# auth_token = "56af0755af3b5bb541adabf8313f77a1"

client = Client(account_sid, auth_token)

bot_phone = "+12028836616"
client_phone = "+264818779053"

message = client.messages.create(
    body="Hello! I am a data collection bot for the agricultural industry in Namibia. Do you have 5 minutes to answer questions to help the agricultural sector?",
    from_=bot_phone,
    to=client_phone,
)

print(message.body)