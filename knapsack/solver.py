#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # Dynamic programming approach
    num_items = len(items)
    dp = [[0] * (num_items + 1) for i in range(capacity + 1)]
    taken = [0] * num_items 

    # Fill in the table
    for k in range(capacity + 1):
        for j in range(1, num_items + 1):
            vj = items[j - 1].value
            wj = items[j - 1].weight
            if wj <= k:
                dp[k][j] = max(dp[k][j - 1], dp[k - wj][j - 1] + vj)
            else:
                dp[k][j] = dp[k][j - 1]

    # Now backtrace to get the solution
    k = capacity
    j = num_items
    opt_value = dp[capacity][num_items]
    value = opt_value 

    while k > 0 and j > 0:
        if dp[k][j] == dp[k][j - 1]:
            j -= 1
        else:
            j -= 1
            taken[j] = 1
            value -= items[j].value 
            while k > 0 and dp[k][j] != value:
                k -= 1
            # Remove duplicates
            while k > 0 and dp[k - 1][j] == value:
                k -= 1
 
    # prepare the solution in the specified output format
    output_data = str(opt_value) + ' ' + str(int(value != 0)) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

    ''' 
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data
    '''

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

