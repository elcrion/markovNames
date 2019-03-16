# Created by glebiakovlev at 3/7/19

# Markov Generator for inputted names
# Train the system based on inputted boys and girls text file names
# Calculate probabilities for further names generation

import random


class Generator:
    list_of_names = []
    model_order = 0
    min_name_length = 0
    max_name_length = 0
    number_of_names = 0

    def __init__(self, list_of_names, min_name_length, max_name_length, model_order, number_of_names):
        '''
        Initiate object
        :param list_of_names: []
        :param min_name_length: int
        :param max_name_length: int
        :param model_order: int
        :param number_of_names: int
        :param self.word_breaks : string , set amount of breaks as _ times order of the model
        '''
        self.list_of_names = list_of_names
        self.max_name_length = max_name_length
        self.min_name_length = min_name_length
        self.number_of_names = number_of_names
        self.model_order = model_order
        self.word_breaks = self.model_order*'_'


    def read_file(self):
        '''
        Iterate over list of names to create a list of unique letters
        Ignore name for now  if name length is less then order
        Depends on order get the first letters as state
        (ex. : if order 2 the initial state is 2 letters)
        Count the frequencies of subsequent letters that appear after state
        in the dict dictionary.
        If state exists in the dictionary, check for subsequent letter and count frequency
        If not, add the state to dictionary and set frequency to 1

        :return: dictionary of each letter from names list ex. : 'gu': {'i': 1, 's': 4, 'e': 1, 'n': 2}
        '''


        baby_names = (self.word_breaks+item.lower().strip()+self.word_breaks for item in self.list_of_names)
        dict = {}
        for name in baby_names:

            for letter_index in range(len(name)):
                if self.model_order <= letter_index <= len(name):
                    if name[letter_index - self.model_order:letter_index] not in dict:
                        dict[name[letter_index - self.model_order:letter_index]] = {name[letter_index]: 1}
                    else:
                        if name[letter_index] not in dict[name[letter_index - self.model_order:letter_index]]:
                            dict[name[letter_index - self.model_order:letter_index]][name[letter_index]] = 1
                        else:
                            dict[name[letter_index - self.model_order:letter_index]][name[letter_index]] += 1

        return dict

    @staticmethod
    def train_model(names):
        '''
        Calculate sum of frequencies for all possible successors
        in chain that belong to initial state.
        Use the sum to calculate probability for each subsequent state
        :param names: dictionary of letters
        :return: dictionary of letter probabilities ex.: 'gu': [['i', 's', 'e', 'n'], [0.125, 0.5, 0.125, 0.25]]
        '''
        model = {}
        for letter, successors in names.items():
            model[letter] = list()
            sum_successors = sum(successors.values())
            state_probability = map(lambda x: int(round(float(x) / sum_successors, 2) * 100), list(successors.values()))
            model[letter].append(list(successors.keys()))
            model[letter].append(list(state_probability))

        return model

    def generate_names(self):
        '''
        Main function to generate random unique names not included in original list
        Get initial letter from word breaks symbol.
        Get new state (letter) from trained dictionary with weighted random choice every time with previous state
        Continue until the end of word break symbol appears in the state
        Remove word breaks symbol from names
        Check if name between max and min length and name list constraints satisfies
        :return: list of possible names
        '''
        words_dict = self.read_file()
        probabilities_dict = self.train_model(words_dict)
        names = []
        while len(names) < self.number_of_names:
            init_prob =  probabilities_dict.get(self.word_breaks)
            name =  self.word_breaks+self.next_state(list(init_prob[0]),list(init_prob[1]))
            while name[-self.model_order:]!= self.word_breaks:
                prob_dict = probabilities_dict.get(name[-self.model_order:])
                next_state = self.next_state(list(prob_dict[0]), list(prob_dict[1]))
                name += next_state

            name = name.replace(self.word_breaks,'')
            if name not in self.list_of_names and self.max_name_length > len(name) >= self.min_name_length:
                names.append(name)

        return names

    @staticmethod
    def next_state(dict, weights):
        return random.choices(dict, weights=weights, k=1).pop()


