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

# Variable to start the conversation with the user
conversation_starter = input("Hello! I am a data collection bot for the agricultural industry in Namibia. Do you have 5 minutes to answer questions to help the agricultural sector?")

# Variable to store user responses
responses_list = {}

if conversation_starter.lower() == "yes":
    print("Thank you for taking interest in improving Namibia")

    for question in questions_list:
        print(question)
        response = input()
        responses_list[question] = response
        
    print("Thank you for participation in the survey!\n\nYour feedback has been logged and will be used to improve aids efforts across Namibia.")

else: 
    print("Have an amazing day!")


print(responses_list)