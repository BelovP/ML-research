__author__ = 'belovpavel'

import sys
import os
import time
import random

def binary_random_distr(n):              #only 0.1*k type
    result_vector = []
    for i in range(n):
        result_vector.append(random.randint(0, 10) * 10)
    return result_vector

def binary_rand_vector(distr, n):
    result_vector = []
    for i in range(n):
        if random.randint(0, 100) < distr[i]:
            result_vector.append(1)
        else:
            result_vector.append(0)
    return result_vector


def binary_rand_gen_list(distr, vector_size, list_size):
    result_list = []
    for i in range(0, list_size):
        result_list.append(binary_rand_vector(distr, vector_size))
    return result_list


def binary_rand_gen_test_file(distr, vector_size, list_size, output_file):
    result_list = binary_rand_gen_list(distr, vector_size, list_size)
    for i in range (0, list_size):
        for j in range(0, vector_size):
            output_file.write(str(result_list[i][j]) + ' ')
        output_file.write('\n')


def gen_meta_file(train_size, valid_size, test_size, distr_train, distr_test, n, output_file):
    output_file.write(str(train_size) + '\n')
    output_file.write(str(valid_size) + '\n')
    output_file.write(str(test_size) + '\n')
    output_file.write(str(n) + '\n')
    output_file.write(str(n) + '\n')
    output_file.write('distr_train: ')
    for i in range(n):
        output_file.write(str(distr_train[i]) + ' ')
    output_file.write('\n')
    output_file.write('distr_test: ')
    for i in range(n):
        output_file.write(str(distr_test[i]) + ' ')


seed = 1
random.seed(seed)
output_train = 'data/binary_rand/binary_rand_train_set.amat'
output_test = 'data/binary_rand/binary_rand_test_set.amat'
output_valid = 'data/binary_rand/binary_rand_valid_set.amat'
output_meta = 'data/binary_rand/binary_rand_meta'
n = 25
distr1 = binary_random_distr(n)
distr2 = binary_random_distr(n)
distr_train = distr2
distr_test = distr1
train_size = 10000
valid_size = 1000
test_size = 1000

random.seed(seed)

file_train = open(output_train, 'w')
file_test = open(output_test, 'w')
file_valid = open(output_valid, 'w')
file_meta = open(output_meta, 'w')

binary_rand_gen_test_file(distr_train, n, train_size, file_train)
binary_rand_gen_test_file(distr_train, n, valid_size, file_valid)
binary_rand_gen_test_file(distr_test, n, test_size, file_test)
gen_meta_file(train_size, valid_size, test_size, distr_train, distr_test, n, file_meta)

file_train.close()
file_test.close()
file_valid.close()
file_meta.close()

