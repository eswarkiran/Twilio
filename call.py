from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC94017c4393097370f18eafddd40b65ef"
auth_token  = "04cf0f0516d70bfa86ec45a4164dd0cd"
client = TwilioRestClient(account_sid, auth_token)

call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
    #to='+911234567890'
    to="+91",
    from_="+12406161700")
print(call.sid)
