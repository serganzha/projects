import spacy

# Similarity function
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("***")
# We can see that cat and monkey have the highest similarity as they are both animals,
# followed by banana and monkey, because monkeys like to eat bananas
# with banana and cat being the least similar.

# Vectors
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print("***")
# apple and banana have the highest similarity, as they are both fruit,
# and cat and apple are the least similar


# Working with sentences
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
print("***")
# the most similar sentence to "Why is my cat on the car", is "Hello, there is my car"
# and the least similar is I\'d like my boat back"


# own example
nlp = spacy.load('en_core_web_md')
word1 = nlp("car")
word2 = nlp("boat")
word3 = nlp("cup")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("***")
# Car and Boat are most similar, as they are both methods of transportation
# Cup and Car are least similar

# By using the smaller language model "en_core_web_sm", on example.py
# we can see the similarity rating drop by ≈ 0.2-0.3 with a few exceptions
