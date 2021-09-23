# website for sms :https://www.twilio.com/
# might need to install twilio using pip
from twilio.rest import Client

account_sid = 'ACe38fff87763a7b1bbac533892fcd40cb'
auth_token = '532c0985b965d868988b1cf50bac0aa6'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGbc8ee47b2695f26eae7012648de998c2',
    body='hi',
    to='+919714648827'
)

print(message.sid)
# it works
