__author__ = 'belovpavel'

import sys
import os
import time
import random

class Experiment:
    pass
    #def __init__():

   # def create_sample(self):
   #     raise NotImplementedError("Subclass should implement this method.")


class KPoints():       # exactly k 1-s in random positions

    def __init__(self, k, vector_size):
        self.k = k
        self.vector_size = vector_size

    def create_sample(self, k):
        sample = [1] * k
        sample.extend([0] * (self.vector_size - k))
        for i in range(1, 100):
            sample.shuffle()
        return [sample]

    def create_training_samples(self, training_size):
        sample = [1] * self.k
        sample.extend([0] * (self.vector_size - self.k))
        training_set = []
        for j in range(1, training_size):
              training_set.append(self.create_sample(self.k))

        return [training_set]
    def create_all_combinations(self, free_positions, combination, cmb_length):
        if combination.size() == cmb_length:
            pass

def k_first(k_zeros, n):
    result_vector = [0] * k_zeros
    for i in range(k_zeros, n):
        result_vector.append(random.randint(0, 1))
    return result_vector


def k_first_gen_list(k_zeros, vector_size, list_size):
    result_list = []
    for i in range(0, list_size):
        result_list.append(k_first(k_zeros, vector_size))
    return result_list


def k_zeros_first_gen_test_file(k_zeros, vector_size, list_size, output_file):
    result_list = k_first_gen_list(k_zeros, vector_size, list_size)
    for i in range (0, list_size):
        #output_file.write('1 ')         #id of class for current object
        for j in range(0, vector_size):
            output_file.write(str(result_list[i][j]) + ' ')
            #if result_list[i][j] == 1:             #it is for libsvm format
             #   output_file.write(str(j + 1) + ':1 ')
        output_file.write('\n')


def gen_meta_file(train_size, valid_size, test_size, k_zeros, n, output_file):
    output_file.write(str(train_size) + '\n')
    output_file.write(str(valid_size) + '\n')
    output_file.write(str(test_size) + '\n')
    output_file.write(str(k_zeros) + '\n')
    output_file.write(str(n) + '\n')


seed = 1
#datadir = os.path.abspath(os.path.curdir) + '/data/'
output_train = 'data/k_zeros/train_set.amat'
output_test = 'data/k_zeros/test_set.amat'
output_valid = 'data/k_zeros/valid_set.amat'
output_meta = 'data/k_zeros/meta'
train_size = 10000
valid_size = 1000
test_size = 500
k_zeros = 10
k_zeros_test = 5
n = 20

random.seed(seed)

file_train = open(output_train, 'w')
file_test = open(output_test, 'w')
file_valid = open(output_valid, 'w')
file_meta = open(output_meta, 'w')

k_zeros_first_gen_test_file(k_zeros, n, train_size, file_train)
k_zeros_first_gen_test_file(k_zeros, n, valid_size, file_valid)
k_zeros_first_gen_test_file(k_zeros_test, n, test_size, file_test)
gen_meta_file(train_size, valid_size, test_size, k_zeros, n, file_meta)

file_train.close()
file_test.close()
file_valid.close()
file_meta.close()

