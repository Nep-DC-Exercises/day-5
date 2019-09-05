# Exercise 1
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923',
}

# 1a. Print Elizabeth's phone number
print('1a')
print(phonebook_dict['Elizabeth'])
# 1b. Add an an entry to the dictionary: Kareem's number is 938-489-1234
print('1b')
phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict)
# 1c. Delete Alice's phone entry.
print('1c')
del phonebook_dict['Alice']
print(phonebook_dict)
# 1d. Change Bob's number to '968-345-2345'
print('1d')
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict['Bob'])
# 1e. Print all the phone entries
print('1e')
phone_entries = phonebook_dict.values()
print(phone_entries)

# Exercise 2: Nested Dictionaries
import collections
import operator
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

# 2a. Get Ramit's email address
print('2a')
print(ramit['email'])
# 2b. Get the first of Ramit's interests
print('2b')
print(ramit['interests'][0])
# 2c. Get Jasmine's email
print('2c')
print(ramit['friends'][0]['email'])
# 2d. Get Jan's two interests
print('2d')
print(ramit['friends'][1]['interests'])

# Exercise 3: Letter Summary
''' Prompt:
Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word.
'''

string_eval = input("Add a word. Will show how often each letter appears. >> ")
string_eval = string_eval.lower()

letter_count = {}

for letter in string_eval:

    if letter not in letter_count:
        letter_count[letter] = 1

    else:
        letter_count[letter] += 1

print(letter_count)

# Exercise 4: Word Summary
'''Prompt: 
Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text. 
'''

sentence_eval = "The red truck went over the red bridge because of the blue water truck"
sentence_eval = sentence_eval.lower()
word_count = {}

for word in sentence_eval.split():

    if word not in word_count:
        word_count[word] = 1

    else:
        word_count[word] += 1

print(word_count)


# Bonus Challenge: Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.

# list of tuples in decending order by value
word_count_sorted = sorted(
    word_count.items(), key=lambda x: x[1], reverse=True)
print(word_count_sorted[0:3])  # only need the first three
