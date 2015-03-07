import mlpython.misc.io as mlio
import numpy as np
import os

def load(dir_path,load_to_memory=False,dtype=np.float64):
    """
    Loads the k_zeros dataset.

    The data is given by a dictionary mapping from strings
    'train', 'valid' and 'test' to the associated pair of data and metadata.
    
    reads lengths from meta file.

    Defined metadata: 
    - 'input_size'
    - 'length'
    """
    
    meta_file_str = os.path.join(dir_path, 'meta')
    meta_file = open(meta_file_str, 'r')
    nums_list = [line.strip() for line in meta_file]
    
    train_length = int(nums_list[0])
    valid_length = int(nums_list[1])
    test_length = int(nums_list[2])
    k_zeros = int(nums_list[3])
    input_size = int(nums_list[4])
    print (nums_list)

    meta_file.close()
    dir_path = os.path.expanduser(dir_path)
    def load_line(line):
        tokens = line.split()
        return np.array([int(i) for i in tokens[:]]) 

    train_file,valid_file,test_file = [os.path.join(dir_path, ds + '_set.amat') for ds in ['train','valid','test']]
    # Get data
    train,valid,test = [mlio.load_from_file(f,load_line) for f in [train_file,valid_file,test_file]]

    lengths = [train_length, valid_length, test_length]
    if load_to_memory:
        train,valid,test = [mlio.MemoryDataset(d,[(input_size,)],[dtype],l) for d,l in zip([train,valid,test],lengths)]
        
    # Get metadata
    train_meta,valid_meta,test_meta = [{'input_size':input_size,
                              'length':l} for l in lengths]
    
    return {'train':(train,train_meta),'valid':(valid,valid_meta),'test':(test,test_meta)}
