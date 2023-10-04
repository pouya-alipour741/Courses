
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1,10)

for num in nums:
    print(num)

#######simulating range function
# def my_range(start,end):
#     current = start
#     while current < end:
#         yield current
#         current += 1

######loop until infinity ,caution!
# def my_range(start):
#     current = start
#     while True:
#         yield current
#         current += 1

# nums = my_range(1,10)
#
# for num in nums:
#     print(num)
