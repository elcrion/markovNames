# Created by glebiakovlev at 3/7/19

# Main class for parameters input and boys/girls files read
# Pass everything to Generator class for training
from Generator import Generator


class Main:
    '''
        Main class implementation
    '''

    def __init__(self):
        self.get_parameters()

    def get_parameters(self):

        """
        Get initial parameters
        min_name_length :
        male_female :
        model_order :
        number_of_names :
        :return: null
        """
        data = []
        male_female = int(input('Input 1 if female 2 if male : '))

        if male_female  not in [1, 2]:
            print('Input should be 1 or 2')
            self.get_parameters()

        min_name_length = int(input('Enter minimum name length: '))
        max_name_length = int(input('Enter maximum name length: '))

        if min_name_length > max_name_length:
            print('Minimum name length should be greater then maximum')
            self.get_parameters()

        model_order = int(input('Enter order of the model: '))
        number_of_names = int(input('Number of names: '))

        if male_female == 1:
            data = open('namesBoys.txt', 'r')
        if male_female == 2:
            data = open('namesGirls.txt', 'r')

        model =  Generator(data, min_name_length, max_name_length, model_order, number_of_names)
        print(model.generate_names())

        repeat = input('Push enter to try again')

        if repeat == "":
            self.get_parameters()


if __name__ == '__main__':
    Main()
