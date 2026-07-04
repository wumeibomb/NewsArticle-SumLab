import re

text_to_analyze = """
User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. “We want to cater to all taste preferences, from the traditional to the adventurous,” said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master’s environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. “Sustainability is at the core of all our product designs,” emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, “It’s like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings.”

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.
"""

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
    pattern = r"\w" #how do I exclude the underscore??
    pattern_match = re.findall(pattern, str)

    if str == "":
        print("None")
    else:
        for eachcharacter in pattern_match:
         count += 1
        
        average = count / len(mean)
        print(average.__round__(2))  

#calculate_average_word_length("")

def count_paragraphs(str):
    #if libe break, b? is present, +1?
    separator = r"^\s"
    counter = 0
    okay = re.findall(separator, str, re.MULTILINE)
        #if wordcount is less than certain number, don't include in count???
    
    for each in okay:
        counter += 1

    print(counter)

count_paragraphs(text_to_analyze)