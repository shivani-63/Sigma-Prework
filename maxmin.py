def find_min_max(int_list):
    min_val = int_list[0]
    max_val = int_list[0]
    for num in int_list:
        if num < min_val:
            min_val = num
        if max_val < num:
            max_val = num
    ans = [int(min_val), int(max_val)]
    return ans

test_cases =  [
    [10,-10,-100,67,9],
    [10,14,16,28],
    [-67,-15,-75,-100]
]
for test in test_cases:
    print(find_min_max(test))

#some test case examples, to check the find_min_max() function works
#expected output: [-100,67][10,28][-100,-15]