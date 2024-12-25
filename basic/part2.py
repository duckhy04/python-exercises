# 1. Unique Numbers Check
import random


def unique_numbers_check():
    nums = [1, 2, 3, 4, 5, 8, 9]
    if len(set(nums)) != len(nums):
        print(False)
    else:
        print(True)


# 2. All Unique Strings
def all_unique_string():
    char_list = ['a', 'e', 'i', 'o', 'u']
    random.shuffle(char_list)
    print(''.join(char_list))


# 3. Remove Every Third
def remove_every_third():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pos = 3 - 1
    index = 0
    length = len(nums)
    print(nums)
    while length > 0:
        index = (pos + index) % length
        print(nums.pop(index), end=' ')
        length -= 1
    print(nums)


# 4. Zero Sum Triplets
def zero_sum_triplets():
    nums = [1, -6, 4, 2, -1, 2, 0, -2, 0, 1]
    result = []
    nums.sort()
    print(nums)
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                result.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1

    print(result)


# 5. 3-Digit Combinations
def three_digit_combinations():
    result = []
    for num in range(1000):
        num = str(num).zfill(3)
        print(num)



# 6. Word Frequency Counter
def word_frequency_counter():
    result = []
    print(result)


word_frequency_counter()