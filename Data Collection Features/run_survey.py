import os
from dotenv import load_dotenv
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from data_processor import structure_survey_data

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_SESSION_SECRET']  

# MongoDB setup
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['EdilsonsProjects']  # database name
surveys_collection = db['AgriBot_SMS_Data']  # collection name

questions_list = [
    "What is your name?\n\n(Please provide only your name. Example: Edilson Zau)", 
    "What is your date of birth?\n\n(Please provide only your date of birth. Example: 12 November 1987)", 
    "Where are you located?\n\n(Please provide your region and constituency. Example: Khomas, Windhoek)", 
    "What do you farm?\n\n(Please provide only your produce. Example: Tomatoes, potatoes, onions, and spinach)", 
    "How often do you harvest?\n\n(Example: 3 or 4 Times a year)", 
    "Do you get any help from the Ministry of Agriculture Water and Land reform or any other institutions?", 
    "Are you certified by the Namibia Agronomic Board (NAB)? (Yes/No)", 
    "What are your challenges? (Please be as detailed as possible)"
]

@app.route("/sms", methods=['POST'])
def survey_client():
    incoming_msg = request.values.get('Body', '').strip()
    phone_number = request.values.get('From')
    
    resp = MessagingResponse()
    
    if 'survey_sessions' not in session:
        session['survey_sessions'] = {}
    
    if phone_number not in session['survey_sessions']:
        session['survey_sessions'][phone_number] = {
            'current_question': -1,
            'responses': {}
        }
    
    user_session = session['survey_sessions'][phone_number]
    
    if user_session['current_question'] == -1:
        if incoming_msg.lower() == 'yes':
            resp.message("Thank you for taking interest in improving agriculture in Namibia!")
            user_session['current_question'] += 1
            resp.message(questions_list[user_session['current_question']])
        else:
            resp.message("To start the survey, please reply with 'yes'. If you don't want to participate, reply with 'no'.")
    elif user_session['current_question'] < len(questions_list):
        # Save the response to the current question
        user_session['responses'][questions_list[user_session['current_question']]] = incoming_msg
        
        # Move to the next question
        user_session['current_question'] += 1
        
        if user_session['current_question'] < len(questions_list):
            resp.message(questions_list[user_session['current_question']])
        else:
            # Structure and save the data to MongoDB
            survey_data = structure_survey_data(
                phone_number, 
                user_session['responses'],
                questions_list
            )

            try:
                surveys_collection.insert_one(survey_data)
                resp.message("Thank you for completing the survey! Your responses have been saved.")
            except Exception as e:
                print(f"Error saving to MongoDB: {e}")
                resp.message("Thank you for completing the survey! However, there was an issue saving your responses.")

            print(user_session['responses'])  # Print responses to console
            # Here you could also save the responses to a database
            
            # Reset the session for this user
            session['survey_sessions'][phone_number] = {
                'current_question': -1,
                'responses': {}
            }
    
    # Save the updated session
    session['survey_sessions'][phone_number] = user_session
    session.modified = True
    
    return str(resp)

# Utility route to check stored surveys (for development/testing)
@app.route("/check-surveys", methods=['GET'])
def check_surveys():
    if not os.getenv('FLASK_DEBUG'):
        return "Not available in production", 403
    
    surveys = list(surveys_collection.find({}, {'_id': 0}))
    return {'surveys': surveys}

if __name__ == "__main__":
    app.run(debug=True)