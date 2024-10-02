from dotenv import load_dotenv
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def survey_client():
    # List of questions to be asked
    questions_list = [
        "What is your name?\n\n(Please provide only your name. Example: Edilson Zau)", 
        "What is you date of birth?\n\n(Please provide only your date of birth. Example: 12 November 1987)", 
        "Where are you located?\n\n(Please provide your region and constituency. Example: Khomas, Windhoek)", 
        "What do you farm?\n\n(Please provide only your produce. Example: Tomatoes, potatoes, onions, and spinach)", 
        "How often do you harvest?\n\n(Example: 3 or 4 Times a year)", 
        "Do you get any help from the Ministry of Agriculture Water and Land reform or any other institutions?", 
        "Are you certified by the Namibia Agronomic Board (NAB)? (Yes/No)", 
        "What are your challenges? (Please be as detailed as possible)"
    ]

    # Variable to store user responses
    responses_list = {}

    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    response = MessagingResponse()

    if 'yes' in body.lower():
        response.message("Thank you for taking interest in improving agriculture in Namibia!")

        for question in questions_list:
            response.message(question)

            responses_list[question] = body.lower()
              
    else: 
        response.message("Have an amazing day!")

    print(responses_list)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)