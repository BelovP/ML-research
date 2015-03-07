__author__ = 'belovpavel'

import sys
import os
import time
import random

class Experiment:
    pass
    #def __init__():


def k_points_rand_vec(k_points, n):               #returns vector with exactly k 1's in random positions
    available_positions_list = list(x for x in range(0, n))
    target_positions = random.sample(available_positions_list, k_points)
    result_vector = [0] * n
    for pos in target_positions:
        result_vector[pos] = 1
    return result_vector


def k_points_rand_gen_list(k_points, vector_size, list_size):
    result_list = []
    for i in range(0, list_size):
        result_list.append(k_points_rand_vec(k_points, vector_size))
    return result_list


def k_points_rand_gen_train_file(k_points, vector_size, list_size, output_file):         #generates valid and train files
    result_list = k_points_rand_gen_list(k_points, vector_size, list_size)
    for i in range (0, list_size):
        #output_file.write('1 ')         #id of class for current object
        for j in range(0, vector_size):
            output_file.write(str(result_list[i][j]) + ' ')
            #if result_list[i][j] == 1:             #it is for libsvm format
             #   output_file.write(str(j + 1) + ':1 ')
        output_file.write('\n')


def gen_meta_file(train_size, valid_size, test_size, k_points, n, output_file):
    output_file.write(str(train_size) + '\n')
    output_file.write(str(valid_size) + '\n')
    output_file.write(str(test_size) + '\n')
    output_file.write(str(k_points) + '\n')
    output_file.write(str(n) + '\n')


def k_points_rand_gen_test_file(k_points_test, vector_size, test_size, output_file):             #IMPORTANT! k_points_test != k_points (may be), used for creating test sets 
    result_list = k_points_rand_gen_list(k_points, vector_size, test_size)
    for i in range (0, test_size):
        for j in range(0, vector_size):
            output_file.write(str(result_list[i][j]) + ' ')
        output_file.write('\n')    

seed = 1
#datadir = os.path.abspath(os.path.curdir) + '/data/'
output_train = 'k_points_rand_train_set.amat'
output_test = 'k_points_rand_test_set.amat'
output_valid = 'k_points_rand_valid_set.amat'
output_meta = 'k_points_rand_meta'
train_size = 4000
valid_size = 800
test_size = 800
k_points = 4
k_points_test = 8
n = 20
random.seed(seed)

file_train = open(output_train, 'w')
file_test = open(output_test, 'w')
file_valid = open(output_valid, 'w')
file_meta = open(output_meta, 'w')

k_points_rand_gen_train_file(k_points, n, train_size, file_train)
k_points_rand_gen_train_file(k_points, n, valid_size, file_valid)
gen_meta_file(train_size, valid_size, test_size, k_points, n, file_meta)
k_points_rand_gen_test_file(k_points_test, n, test_size, file_test)

file_train.close()
file_test.close()
file_valid.close()
file_meta.close()

