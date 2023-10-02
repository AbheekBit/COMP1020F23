import string
import random


def make_response_dictionary(chatbot_file):
    with open(chatbot_file) as file:
        lines = file.readlines()
    possible = {}
    for sentences in lines:
        pair_of_words = sentences.split(",")
        possible[pair_of_words[0]] = pair_of_words[1]

    return possible


class ChatBot:
    def __init__(self, greeting, response, default):
        self.greeting = greeting
        self.keyword_and_response = make_response_dictionary(response)
        self.default = default

    def greet(self):
        print(self.greeting)

    def respond(self, human_text):
        # Creating a dictionary

        human_text = human_text.lower()
        human_text = human_text.translate(str.maketrans('', '', string.punctuation))
        human_words = human_text.split()
        poss_responses = []
        for word in human_words:

            if word in self.keyword_and_response:
                poss_responses.append(self.keyword_and_response[word])

        if len(poss_responses) == 0:
            return self.default

        return poss_responses[random.randrange(0, len(poss_responses))]
