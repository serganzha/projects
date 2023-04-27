# test_string = ("Hello world!, I am learning to code")

input_string = input("Please enter a word or a phrase: ")
alternative_letter = ""
# using a loop to iterate over each character in the string, to check if its
# index is odd or even
for i in range(len(input_string)):
    if i % 2 == 0:
        alternative_letter += input_string[i].upper()
    else:
        alternative_letter += input_string[i].lower()

print(alternative_letter)

words = input_string.split()
alternative_word = []
# split the words, then join them after for loop appends them
for i in range(len(words)):
    if i % 2 == 0:
        alternative_word.append(words[i].lower())
    else:
        alternative_word.append(words[i].upper())

alternative_word = " ".join(alternative_word)
print(alternative_word)
