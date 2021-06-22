# FUCK: WHY?

'''
Input:
Dictionary to Save,
Output file path

Output:
Retrieved Object

'''


import pickle 

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)


def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


