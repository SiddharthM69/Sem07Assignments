class BloomFilter:
    def hashFunc1(self, x):
        return (3 * x) % len(self.arr)

    def hashFunc2(self, x):
        return (4 * x) % len(self.arr)

    def hashFunc3(self, x):
        return (5 * x) % len(self.arr)

    def __init__(self, b):
        self.arr = [0 for _ in b]
        for el in b:
            self.arr[self.hashFunc1(el)] = 1
            self.arr[self.hashFunc2(el)] = 1
            self.arr[self.hashFunc3(el)] = 1

    def add(self, el):
        self.arr[self.hashFunc1(el)] = 1
        self.arr[self.hashFunc2(el)] = 1
        self.arr[self.hashFunc3(el)] = 1

    def check(self, el):
        if(self.arr[self.hashFunc1(el)]==1 and self.arr[self.hashFunc2(el)]==1 and self.arr[self.hashFunc3(el)]==1):
            return True
        return False



# ------------------driver code--------------------
b = []
n = int(input("Enter the number of elements initially"))
for i in range(0,n):
    b.append(int(input("Enter element no. {} ".format(i+1))))
bloom = BloomFilter(b)
toCheck = int(input("Enter the element to be checked"))
if bloom.check(toCheck):
    print("{} may be present".format(toCheck))
else:
    print("{} is definitely not present".format(toCheck))


