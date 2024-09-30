# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("As a farmers my problem is that there is no enough rain, so crops no grow. Also I no have money to buy pesticides and I struggle to sell my vegs.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

print("++++++++++++++++++++++++++")
# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)