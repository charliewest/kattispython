# 1 permutation (2) = 2
# 2 permutations (2 * 3) (3 * 2) = 6
# 3 permutations (2 * 2 * 3) (2 * 3 * 2) (3 * 2 * 2) = 12
# 4 permutations (2 * 2 * 2 * 3) = 24
# 5 permutations (3 * 2 * 2 * 2 * 2) = 48
# 6 permutations (2 * 2 * 3 * 3) = 36     (2 * 2 * 2 * 2 * 2 * 3 = 96)
#                (2 * 3 * 5) = 30

# how many 2s, 3s, 5s, 7s etc are needed to create n permutations

# how many (repeatable) objects are needed to create n permutations


#                   fact(number_of_elements)
# ---------------------------------------------------------------     =     n
# fact(multi_1) x fact(multi_2) x ... x fact(multi_m)

# Get possible arrays - store minimum value.

from math import factorial
from itertools import product

def get_partitions(target, max_value, partition_list, current_list):
    if target == 0:
        new_list = [x for x in current_list]
        print("Appending {} to partition_list".format(new_list))
        partition_list.append(new_list)
        current_list.clear()
    else:
        for i in range(1, 100):
            if i > max_value or i > target:
                break
            print("Appending {} to current_list".format(i))
            current_list.append(i)
            get_partitions(target - i, i, partition_list, current_list)
                
        
def get_min_value(n):
    min_value = 2 ** 63

    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

    for i in range(1, n + 1):

        print("RANGE {}".format(i))
        top = factorial(i)

        tested_combs = {}
        
        # Cartesian product (get all possible arrangement of the prime
        #                    values in the variable primes so that the
        #                    length is i (RANGE))
        for j, factor_arr in enumerate(product(primes[:i], repeat = i)):
            
            counter = []
            for prime in primes:
                counter.append((prime, factor_arr.count(prime)))
                if prime > (top / 2) + 1:
                    break
                
            bottom = 1
            for element in counter:
                bottom *= factorial(element[1])
            
            if top / bottom == n:
                print("FOUND MATCH FOR {}".format(factor_arr))
                value = 1
                for entry in counter:
                    print("multiplying by {}".format(entry[0] ** entry[1]))
                    value *= entry[0] ** entry[1]
                min_value = min(value, min_value)
                print(min_value)
                break

            
            print("{} {}".format(j, factor_arr))
            if len(factor_arr) > 0:
                if factor_arr[0] == primes[1]:
                    print("LOOPED THROUGH ALL VARIATIONS, MOVE ON {}".format(factor_arr))
                    break

            if primes[i] in factor_arr:
                print("REACHED HIGHEST PRIME WITHOUT MATCH, MOVE ON {}".format(factor_arr))
                break

        
        # Conditions to break out early.
        if 3 * (2 ** (i + 1)) > min_value: # naive solution 2**(n - 1) + 3
            print("No point to continue after {}".format(i))
            break

    return min_value

n = int(input())

partition_list = []
current_list = []
get_partitions(n, n, partition_list, current_list)

print(partition_list)

get_min_value(n)