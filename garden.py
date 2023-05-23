import spacy

# list of sentances imported from
# https://www.apartmenttherapy.com/garden-sentences-262915

nlp = spacy.load('en_core_web_md')
gardenpathSentences = [
    "Helen is expecting tomorrow to be a bad day.",
    "When Fred eats food gets thrown.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# loop to tokenise each sentence,
# and a nested loop to perform Named Entity Recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    for token in doc:
        print(token.text)
    print("Named Entities:")
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    print("***")


entity_fac = spacy.explain("GPE")
print(f"GPE:{entity_fac}")
# GPE:Countries, cities, states
# Mississippi was identified as GPE, it makes sence based on the explanation

entity_fac = spacy.explain("ORG")
print(f"ORG:{entity_fac}")
# ORG:Companies, agencies, institutions, etc.
# Band-Aid was identified as ORG, this might be reference to a charity group,
# and not an adhesive bandage
