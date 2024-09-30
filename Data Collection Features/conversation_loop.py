conversation_starter = input("Hello! I am a data collection bot for the agricultural industry in Namibia. Do you have 5 minutes to answer questions to help the agricultural sector?")

questions_list = ["What is your name?", "What is you date of birth?", "Where are you located?", "What do you farm?", "How often do you harvest?", "Do you get any help from the Ministry of Agriculture Water and Land reform or any other institutions?", "Are you certified by the Namibia Agronomic Board (NAB)?", "What are your challenges?"]

responses_list = {}

run = True

if conversation_starter.lower() == "yes":
    print("Thank you for taking interest in improving Namibia")

    while run: 
        for question in questions_list:
            print(question)
            response = input()
            responses_list[question] = response
            #Await answer
            print("LLM Message response...")
        
        print("Thank you for participation in the survey! Your feedback has been logged and will be used to improve aids efforts across Namibia.")
        run = False
else: 
    print("Have an amazing day!")


print(responses_list)