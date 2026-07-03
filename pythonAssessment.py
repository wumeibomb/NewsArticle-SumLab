import re

text_to_analyze = "With the break statement we can stop the loop before it has looped through all the items, break in the statment break"

word2 = input("word to count: ")

def count_specific_word(text, word2):
    count = 0
    text = text_to_analyze.split()
    for each in text:
        if each == word2:
            count += 1
    print(f"{count} matches")
        #+1 for the counter

count_specific_word(text_to_analyze, word2)

#def identify_most_common_word(text):
#    find_in = text_to_analyze.split()
#I DON'T KNOW HOW TO FIND THE COMMON WORD...



