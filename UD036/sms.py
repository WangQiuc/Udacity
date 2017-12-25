from twilio.rest import Client

account_sid = 'AC05f9828a486b82f311f2d10605c58237'
auth_token = '6c1d1fe1dfe10d6fa9fee8cee80c3754'
client = Client(account_sid, auth_token)

message = client.messages.create(
        body='没事，不急',
        to='+8613661980262',
        from_='+12406967650')
print(message.sid)

