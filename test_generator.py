# Created by glebiakovlev at 3/9/19
from unittest import TestCase


# Test main functions here

from Generator import Generator


class markovTest(TestCase):
    def setUp(self):
        self.data = open('namesBoys.txt', 'r')
        self.min_name_length = 2
        self.max_name_length = 5
        self.number_of_names = 5
        self.model_order = 2
        self.model = Generator(self.data, self.min_name_length, self.max_name_length, self.model_order, self.number_of_names)


class DefaulFileReadTestCase(markovTest):
    def runTest(self):
        self.assertNotEqual(len(self.model.read_file()),0,'Failed to process  name list')


class DefaultTrainTestCase(markovTest):

    def setUp(self):
        self.names = self.model.read_file()
        self.model = self.model.train_model(self.names)

    def runDefaultTrainTest(self):
        self.assertNotEqual(len(self.model),0,'Failed to train model')


    def runDetailedTrainTest(self):
        self.assertEqual(len(self.model.keys()), len(self.model.values()))


class DefaultNameGenTestCase(markovTest):
    def runTest(self):
        model = self.model.generate_names()
        self.assertNotEqual(len(model), 0, 'Failed to generate names, length is 0 ')
        self.assertLessEqual(len(model),self.number_of_names,'Failed to generate names, length is not within constraints')
