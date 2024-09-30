def main():
    print("Welcome to our conversation starter!")
    

    questions_and_responses = {
        "What is your name?": "Nice to meet you, {}!",
        "What is your gender?": "Nice to meet you, {}!",
        "What is your favorite color?": "Ah, {} is a great choice!",
        "How old are you?": "You're {} years old! You're so young!",
    }
    
    answers = {}
    
    for question, response in questions_and_responses.items():
        user_input = input(question + "\n")
        answers[question] = user_input
        
        # Check if the response is a lambda function
        if callable(response):
            print(response(user_input))
        else:
            print(response.format(user_input))
    
    print("\nThank you for chatting with us. Here's a summary of your answers:")
    for question, answer in answers.items():
        print(f"{question}: {answer}")

if __name__ == "__main__":
    main()