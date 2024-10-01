from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from LLM.generate_response import generate_response

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    response = MessagingResponse()

    # Determine the right reply for this message
    if body.lower() == 'hello':
        # Add a message
        response.message("Hello! How can I assist you today?")
    elif body.lower() == 'bye':
        # Add a message
        response.message("Have a nice day!")
    else: 
        #Calls the generate_response function to make a response using gpt-3.5-turbo
        response.message(generate_response(body))

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
