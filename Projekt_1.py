
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Anna Peloušková
email: a.pelouskova@seznam.cz
discord: Pel#9400
"""
from user_database import users
from text_database import texts

def login(user_database):
    print("username:", end = "")
    username = input()
    print("password:", end = "")
    password = input()

    for user in user_database:
        if (user_database[user]["user"] == username):
            if (user_database[user]["password"] == password):
                return username
        
    return None

def select_text(text_database):
    number_of_texts = len(text_database)
    
    print("We have",number_of_texts, "texts to be analyzed.")
    print("----------------------------------------")
    print("Enter a number btw. 1 and", number_of_texts, "to select: ", end = "")
    
    user_input = input()
    
    if not user_input.isdigit():
        return None
    
    index = int(user_input)

    if (index > number_of_texts):
        return None

    return index

def analyze_text(text):  
    number_of_titlecase = 0
    number_of_uppercase = 0
    number_of_lowercase = 0
    number_of_numeric = 0
    total_sum_of_numerics = 0
    histogram = {}

    words = text.split()

    for i in range(0, len(words)):
        analyzed_word = words[i]
        # Tecka a carka neni soucasti analyzy slova
        analyzed_word = analyzed_word.replace(".","").replace(",","")
        word_length = len(analyzed_word)
        if word_length not in histogram.keys():
            histogram[word_length] = 0
        histogram[word_length] = histogram[word_length] + 1
        if (analyzed_word[0].isupper()):
            number_of_titlecase = number_of_titlecase + 1
        if (analyzed_word.isupper() and analyzed_word.isalpha()):
            number_of_uppercase = number_of_uppercase + 1
        if (analyzed_word.islower() and analyzed_word.isalpha()):
            number_of_lowercase = number_of_lowercase + 1
        if (analyzed_word.isdigit()):
            number_of_numeric = number_of_numeric + 1
            total_sum_of_numerics = total_sum_of_numerics + int(analyzed_word)

    print("There are", len(words), "words in the selected text.")
    print("There are", number_of_titlecase, "titlecase words.")
    print("There are", number_of_uppercase, "uppercase words.")
    print("There are", number_of_lowercase, "lowercase words.")
    print("There are", number_of_numeric, "numeric strings.")
    print("The sum of all the numbers", total_sum_of_numerics)
    print("----------------------------------------")
    
    max_occurences = max(histogram.values())
    
    print(f'LEN|{"OCCURENCES":^{max_occurences + 2}}|NR.')
    print("----------------------------------------")

    max_word_length = max(histogram.keys())
    
    for i in range(1, max_word_length + 1):
        if i in histogram.keys():
            print(f'{i:>3}|{"*" * histogram[i]:<{max_occurences + 2}}|'
                   + str(histogram[i]))
        else:
            print(f'{i:>3}|{"*" * 0:<{max_occurences + 2}}|' + "0") 
    return

logged_user = login(users)

if not logged_user:
    print("unregistered user, terminating the program..")
    exit()

print("----------------------------------------")
print("Welcome to the app,", logged_user)

text_index = select_text(texts)

if not text_index:
    print("wrong index of text")
    exit()

# Zmena z uzivatelskeho indexovani na pocitacove ;)
text_index = text_index - 1

print("----------------------------------------")

analyze_text(texts[text_index])
