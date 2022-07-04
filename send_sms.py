from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3a45ca2378c805c19ec5c26cc8b493e2"
# Your Auth Token from twilio.com/console
auth_token  = "e2e49683134cb27c28790e1a2d6c6746"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17326372256", 
    from_="+19707164834",
    body="Hello from Python!")

print(message.sid)