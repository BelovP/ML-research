__author__ = 'belovpavel'

import sys
import os
import time
import random

def conj_vector(prob_pos1, prob_pos2, is_conj, one_prob, n):
    result_vector = []
    if random.randint(0, 100) < prob_pos1:
        result_vector.append(1)
    else:
        result_vector.append(0)
    
    if random.randint(0, 100) < prob_pos2:
        result_vector.append(1)
    else:
        result_vector.append(0)

    if is_conj:
        result_vector.append(result_vector[0] and result_vector[1])
    else:
        if random.randint(0, 100) < prob_pos1 * prob_pos2 / 100:
            result_vector.append(1)
        else:
            result_vector.append(0)
    for i in range(3, n):
        if random.randint(0, 100) < one_prob:
            result_vector.append(1)
        else:
            result_vector.append(0)
    return result_vector


def conj_gen_list(prob_pos1, prob_pos2, is_conj, one_prob, vector_size, list_size):
    result_list = []
    for i in range(0, list_size):
        result_list.append(conj_vector(prob_pos1, prob_pos2, is_conj, one_prob, vector_size))
    return result_list


def conj_gen_test_file(prob_pos1, prob_pos2, is_conj, one_prob, vector_size, list_size, output_file):
    result_list = conj_gen_list(prob_pos1, prob_pos2, is_conj, one_prob, vector_size, list_size)
    for i in range (0, list_size):
        #output_file.write('1 ')         #id of class for current object
        for j in range(0, vector_size):
            output_file.write(str(result_list[i][j]) + ' ')
            #if result_list[i][j] == 1:             #it is for libsvm format
             #   output_file.write(str(j + 1) + ':1 ')
        output_file.write('\n')


def gen_meta_file(train_size, valid_size, test_size, prob_pos1, prob_pos2, is_conj, one_prob, n, output_file):
    output_file.write(str(train_size) + '\n')
    output_file.write(str(valid_size) + '\n')
    output_file.write(str(test_size) + '\n')
    output_file.write(str(one_prob) + '\n')
    output_file.write(str(n) + '\n')
    output_file.write(str(prob_pos1) + '\n')
    output_file.write(str(prob_pos2) + '\n')
    output_file.write(str(is_conj) + '\n')

seed = 1
#datadir = os.path.abspath(os.path.curdir) + '/data/'
output_train = 'data/conjuctive/conj_train_set.amat'
output_test = 'data/conjuctive/conj_test_set.amat'
output_valid = 'data/conjuctive/conj_valid_set.amat'
output_meta = 'data/conjuctive/conj_meta'
prob_pos1 = 10
prob_pos2 = 40
one_prob = 50
train_size = 100000
valid_size = 5000
test_size = 1000
n = 25

random.seed(seed)

file_train = open(output_train, 'w')
file_test = open(output_test, 'w')
file_valid = open(output_valid, 'w')
file_meta = open(output_meta, 'w')

conj_gen_test_file(prob_pos1, prob_pos2, True, one_prob, n, train_size, file_train)
conj_gen_test_file(prob_pos1, prob_pos2, True,  one_prob, n, valid_size, file_valid)
conj_gen_test_file(prob_pos1, prob_pos2, False, one_prob, n, test_size, file_test)
gen_meta_file(train_size, valid_size, test_size, prob_pos1, prob_pos2, False, one_prob, n, file_meta)

file_train.close()
file_test.close()
file_valid.close()
file_meta.close()

