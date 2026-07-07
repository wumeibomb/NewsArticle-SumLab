import re


def count_specific_word(text, word2):
    count = 0
    text = text.split()
    print(text)
    for each in text:
        if each == word2:
            count += 1
    print(f"{count}")

count_specific_word("This is as test. Only a test", "test")

def identify_most_common_word(text):
#       in the text, for each word, count it's frequency.
    if text == "":
       print("None")
    else:
       counter = {} #dictionary 
       for eachword in text:
            counter[eachword] =+ 1
            #for x,y in counter.items():
            #   print(x,y)
            #if x is the same as another x, then add their y's together
            #whichever y is the highest, print that.
            #okay I don't know how to total the count and print that..
            

def calculate_average_word_length(str):
    mean = str.split()
    count = 0
    pattern = r"\w" #how do I exclude the underscore??
    pattern_match = re.findall(pattern, str)

    if str == "":
        print("None")
    else:
        for eachcharacter in pattern_match:
                count += 1        

        average = count / len(mean)
        print(f"{average.__round__(2)}")  

calculate_average_word_length("This is a test")

def count_paragraphs(str):
    separator = r"\s$"
    counter = 0
    checker = re.findall(separator, str, re.MULTILINE)

    if str == "":
        print(1)
    else:
        for eachparagraph in checker:
            counter += 1

    print(f"{counter}")

count_paragraphs("This is a test. \n\nThis is only a test.")


def count_sentences(str):
    sentences = r"[.?!]"
    check = re.findall(sentences,str)
    sentence_count = 0
    if str == "":
        print("1")

    else:
        for eachsentence in check:
            sentence_count += 1
        print(f"{sentence_count}") #prints 48 sentences but a character counter online says there are 49?
        #tested with other counters and they all give a range of sentence counts? - seen 41, 44 and grammarly said 57??

count_sentences("Hello wordl. How are you? I'm fine, thank you.")