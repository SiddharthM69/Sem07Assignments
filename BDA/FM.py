def countZeroes(x):
    if x == 0:
        return 1
    count = 0
    while x & 1 == 0:
        count += 1
        x >>= 1
    return count


def FM(arr, k):
    max_zeros = 0
    for i in range(k):
        hash_vals = [countZeroes(el) for el in arr]
        max_zeros = max(max_zeros, max(hash_vals))

    return 2 ** max_zeros

data = []
n=int(input("Enter the number of elements to the data"))
for i in range(n):
    data.append(int(input("Enter the element no. {} ".format(i+1))))
res = FM(data, len(data))
print("The estimated amount of distinct elements in the data are {} ".format(res))