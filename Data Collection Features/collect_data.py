import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import spacy
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

spacy_ner = spacy.load("en_core_web_sm")

porter_stemmer = PorterStemmer()

stop_words = set(stopwords.words('english'))

questions_and_responses = {
    "What is your name?": "Nice to meet you, {}!",
    "What is your gender?": "Nice to meet you, {}!",
    "What is your favorite color?": "Ah, {} is a great choice!",
    "What is your birth year?": lambda x: f"You're {x - 2024} years old! You're so young!",
    "Do you have any pets?": "That's interesting. Tell me more about your pet."
}

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum() or token in ['.', ',', '?', '!']]
    stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)

def extract_entities(text):
    doc = spacy_ner(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

def extract_name(text):
    name_pattern = r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b'
    names = re.findall(name_pattern, text)
    return names

def extract_age(text):
    age_patterns = [
        r'\b\d{1,3}\b years old\b',
        r'\b\d{2,4}\b'
    ]
    ages = []
    for pattern in age_patterns:
        ages.extend(re.findall(pattern, text))
    return ages

def extract_color(text):
    color_patterns = [
        r'\b[A-Za-z]+\b',
        r'\b[A-Z][a-z]+\b'
    ]
    colors = set()
    for pattern in color_patterns:
        colors.update(re.findall(pattern, text))
    return list(colors)

def extract_year(text):
    year_pattern = r'\b\d{4}\b'
    years = re.findall(year_pattern, text)
    return years

def start_conversation():
    answers = {}
    
    for question, response in questions_and_responses.items():
        user_input = input(question + "\n")
        
        preprocessed_input = preprocess_text(user_input)
        
        entities = extract_entities(preprocessed_input)
        name = extract_name(preprocessed_input)[0] if entities else None
        age = extract_age(preprocessed_input)[0] if entities else None
        favorite_color = extract_color(preprocessed_input)[0] if entities else None
        birth_year = extract_year(preprocessed_input)[0] if entities else None
        
        formatted_response = response.format(name or "Unknown", age or "Unknown", favorite_color or "Unknown", birth_year or "Unknown")
        
        answers[question] = {
            "raw_input": user_input,
            "preprocessed_input": preprocessed_input,
            "entities": entities,
            "name": name,
            "age": age,
            "favorite_color": favorite_color,
            "birth_year": birth_year
        }
        
        print(formatted_response)
    
    return answers

def main():
    print("Welcome to our enhanced conversation starter!")
    answers = start_conversation()
    
    print("\nThank you for chatting with us. Here's a summary of your answers:")
    for question, answer in answers.items():
        print(f"{question}:")
        print(f"Raw input: {answer['raw_input']}")
        print(f"Preprocessed input: {answer['preprocessed_input']}")
        print(f"Entities: {answer['entities']}")
        print(f"Name: {answer['name']}")
        print(f"Age: {answer['age']}")
        print(f"Favorite color: {answer['favorite_color']}")
        print(f"Birth year: {answer['birth_year']}")
        print("---")

if __name__ == "__main__":
    main()
