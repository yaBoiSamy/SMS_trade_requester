import send
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    resp.message("")
    return str(resp)


app.run()
