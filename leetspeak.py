# This is the leetspeak exercise from week2 day1 using a while loop/lists instead of dictionary

text = input('What is your message? >> ')
letters_to_convert = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
numbers = [4, 3, 6, 1, 0, 5, 7]

uppercase_text = text.upper()

index = 0

translation = ""

while index < len(uppercase_text):

    # print(uppercase_text[index])
    index_inner_loop = 0
    letter_to_add_to_translation = ""

    while index_inner_loop < len(letters_to_convert):
        # print(letters_to_convert[index_inner_loop])
        if uppercase_text[index] == letters_to_convert[index_inner_loop]:
            # print("WE HAVE A MATCH!")
            # print(numbers[index_inner_loop])
            letter_to_add_to_translation = str(numbers[index_inner_loop])
            break

        else:
            letter_to_add_to_translation = uppercase_text[index]

        index_inner_loop += 1

    index += 1
    translation += letter_to_add_to_translation

print(translation)
