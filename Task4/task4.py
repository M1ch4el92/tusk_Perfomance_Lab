import sys

fnums = open(sys.argv[1], 'r', encoding='UTF-8')
nums = []
for line in fnums.readlines():
    nums.append(int(line))
fnums.close()
result_digit = round(sum(nums)/len(nums))
count = 0
for num in nums:
    while num != result_digit:
        if num < result_digit:
            num += 1
            count += 1
        elif num > result_digit:
             num -= 1
             count += 1
        count += 1

print(count)
