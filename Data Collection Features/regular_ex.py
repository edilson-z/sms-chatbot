import re

def main():
    print("Welcome to our conversation starter!")

    questions_and_responses = {
        "What is your name?": "Nice to meet you, {}!",
        "What is your gender?": "Nice to meet you, {}!",
        "What is your favorite color?": "Ah, {} is a great choice!",
        "How old are you?": "You're {} years old! You're so young!",
        "What is your birth year?": "You were born in {}. That's a great year to be born!"
    }

    answers = {}

    for question, response in questions_and_responses.items():
        user_input = input(question + "\n")

        # Extract relevant data using regular expressions
        if question == "What is your name?":
            match = re.search(r"(\w+)", user_input)
            if match:
                user_input = match.group(1)
        elif question == "What is your gender?":
            match = re.search(r"(male|female|non-binary|other)", user_input, re.IGNORECASE)
            if match:
                user_input = match.group(1)
        elif question == "What is your favorite color?":
            match = re.search(r"(\w+)", user_input)
            if match:
                user_input = match.group(1)
        elif question == "How old are you?":
            match = re.search(r"(\d+)", user_input)
            if match:
                user_input = match.group(1)
        elif question == "What is your birth year?":
            match = re.search(r"(\d{4})", user_input)
            if match:
                user_input = match.group(1)

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