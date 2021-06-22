'''

Input:
List to search, value to search for:

Output:
list of indexes

Careful:
Multidimensional lists

example=[
    [
        [1,2,3],
        2,
        [1,3],
    ]
    [1,2,3]
]

index_all(example,2)
-> [
    [0,0,1],
    [0,1]
]

'''

def index_all(search_list, item):
    indices = list()

    for i in range(len(search_list)):
        if search_list[i]==item:
            indices.append(i)
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):
                indices.append( [i] + index ) #Error ? 
    return indices


example=[
    [
        [1,2,3],
        2,
        [1,3],
    ],
    [1,2,3]
]

print('\n')
print(example)
print('\n')
print('\n')

print(index_all(example, 2 ) )

