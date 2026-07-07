import re

text_to_analyze = """ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation
ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the “Apple Pie Master,” this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. “This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results,” Doe explained.

Unpacking the Technology
The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, “The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one.”

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features
ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. “We want to cater to all taste preferences, from the traditional to the adventurous,” said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact
ACME Inc. is also proud of the Apple Pie Master’s environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. “Sustainability is at the core of all our product designs,” emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability
The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, “It’s like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings.”

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking
Looking ahead, ACME Inc. plans to expand its range of automated baking machines. “The Apple Pie Master is just the beginning,” said CEO Jane Doe. “We’re exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking.”

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations.
"""


word2 = input("word to count: ")


def count_specific_word(text, word2):
    count = 0
    text = text_to_analyze.split()
    for each in text:
        if each == word2:
            count += 1
    print(f"{count} matches for the word '{word2}'")

count_specific_word(text_to_analyze, word2)

def identify_most_common_word(text):
    find_in = text_to_analyze.split()
#       in the text, for each word, count it's frwuency.
    if text == "":
       print("None")
    else:
       counter = {}
       for eachword in find_in:
            counter[eachword] =+ 1
            print(counter)        

identify_most_common_word(text_to_analyze)

#I DON'T KNOW HOW TO FIND THE COMMON WORD...

def calculate_average_word_length(str):
    mean = text_to_analyze.split()
    count = 0
    pattern = r"\w" #how do I exclude the underscore??
    pattern_match = re.findall(pattern, text_to_analyze)

    if str == "":
        print("None")
    else:
        for eachcharacter in pattern_match:
                count += 1        

        average = count / len(mean)
        print(f"This is the average word count: {average.__round__(2)}")  

calculate_average_word_length(text_to_analyze)

def count_paragraphs(str):
    separator = r"\s$"
    counter = 0
    checker = re.findall(separator, str, re.MULTILINE)

    if str == "":
        print("There is 1 paragraph")
    else:
        for eachparagraph in checker:
            counter += 1

    print(f"There are {counter} paragraphs")

count_paragraphs(text_to_analyze)

def count_sentences(str):
    sentences = r"[.?!]"
    check = re.findall(sentences,str)
    sentence_count = 0
    if str == "":
        print("There is 1 sentence")

    else:
        for eachsentence in check:
            sentence_count += 1
        print(f"There are {sentence_count} sentences") #prints 48 sentences but a character counter online says there are 49?
        #tested with other counters and they all give a range of sentence counts? - seen 41, 44 and grammarly said 57??


count_sentences(text_to_analyze)

