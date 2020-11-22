def find_missing(input):
    # input 12456

    n = len(input) + 1  #expected length
    expected_sum = n * (1 + n) / 2
    actual_sum = sum(input)
    print(expected_sum - actual_sum)

find_missing([1,2,4,5])



def find_sum_of_two(A, val):

    sum_val = sum(val)
    if A == sum_val:
        return True
    else:
        return False



def find_sum_of_two(A, val):
    found_values = set()
    print(found_values)
    for a in A:
        print(val -a)
        if val - a in found_values:
            print('true')
            return True

        found_values.add(a)
        print(found_values)
    print('false')
    return False

A =[3,11,2,46]
print(find_sum_of_two(A, 13))




# https://www.educative.io/blog/crack-amazon-coding-interview-questions