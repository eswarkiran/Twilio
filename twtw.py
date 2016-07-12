import twilio
from twilio import rest
print(twilio.__version__)
    # put your own credentials here
ACCOUNT_SID = 'AC94017c4393097370f18eafddd40b65ef'
AUTH_TOKEN = '04cf0f0516d70bfa86ec45a4164dd0cd'

client = rest.TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    #to='+911234567890'
        to = '+91',
        from_ = '+12406161700',
        body = 'Twilio welcomes you',
        media_url ='http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg'
    )
