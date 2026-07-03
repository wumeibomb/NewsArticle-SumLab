import re

text_to_analyze = "With the break break statement we can stop the loop before it has looped through all the items, break in the statment break"
#my test string ^

#word2 = input("word to count: ")

def count_specific_word(text, word2):
    count = 0
    text = text_to_analyze.split()
    for each in text:
        if each == word2:
            count += 1
    print(f"{count} matches")
        #+1 for the counter

#count_specific_word(text_to_analyze, word2)

#def identify_most_common_word(text):
#    find_in = text_to_analyze.split()
#I DON'T KNOW HOW TO FIND THE COMMON WORD...

def calculate_average_word_length(str):
    mean = text_to_analyze.split()
    count = 0
    unwanted_characters = 0
    #pattern = r"^[a-zA-Z(+*)]"
    #bjjb = re.match(pattern, str)

    for eachletter in str:
        if not eachletter == " " and ",":
            count += 1
        else:
            unwanted_characters += 1
        
    print(count, unwanted_characters)
    average = count / len(mean)
    print(average.__round__(2))

calculate_average_word_length(text_to_analyze)

