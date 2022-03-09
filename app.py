from pydoc import cli
from config import account_sid
from config import auth_token
from config import from_number
from config import to_numer

from twilio.rest import Client

client = Client(account_sid,auth_token)
call = client.messages.create(
    to= to_numer,
    from_= from_number,
    body="SMS text..."
)

