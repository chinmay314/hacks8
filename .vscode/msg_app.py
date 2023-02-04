import os
from twilio.rest import Client

account_sid = "AC86f449be9a4c3ac8ed8a04a7ec5ba59f"
auth_token = "9ca725b6a853771aa3bac205e992cc0e"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello from Twilio",
  from_="+18555257221",
  to="+14252179013"
)

print(message.sid)