from twilio.rest import Client
import Private_Constants as pc


def sendTests(msg):
    questrade_phone_num = "+15674323769"
    nic_phone_num = "+15145820908"

    client = Client(pc.account_SID, pc.auth_token)
    client.messages.create(
        to=nic_phone_num,
        from_=questrade_phone_num,
        body=msg
    )
