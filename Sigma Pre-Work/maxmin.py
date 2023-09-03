#given a LIST of integers, return the highest and lowest numbers without using max() or min()
def input_integers():
    integers =input('Please input a list of integers of your choice, separated by a comma:')
    int_list = integers.split(',')
    return int_list

def find_min(int_list):
    min_val = int_list[0]
    for num in int_list:
        if num < min_val:
            min_val = num
    return min_val

def find_max(int_list):
    max_val = int_list[0]
    for num in int_list:
        if max_val < num:
            max_val = num
    return max_val

def min_and_max(min_val,max_val):
    ans = [int(min_val), int(max_val)]
    return ans

print(min_and_max(find_min(input_integers()),find_max(input_integers())))
