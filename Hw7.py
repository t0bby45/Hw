# m = int(input("ved: "))

# for i in range(1, m+1):
#     print(i)



# list = ['a','d',3,4]

# it = iter(list)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# class itres:
#     def __init__(self, value):
#         self.max = value
#         self.cnt = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.cnt +=1
#         if(self.cnt > self.max):
#             raise StopIteration
#         else:
            
#             return self.cnt

# n = int(input("num: "))

# value = itres(n)

# for num in value:
#     if num %2==0:
#         print(num) 
        



# n = int(input("trty"))

# def van(n):
#     for i in range(n+1):
#         yield i*i


# fun = van(n)

# for i in fun:
#     print(i)


# def check_divisi(func):
#     def wra(a, b):
#         if b == 0:
#             return "oshibka"
#         return func(a, b)
#     return wra

# @check_divisi 
# def divide (a, b):
#     return a / b
# print(divide(10, 2))
# print(divide(10, 0))


n = int(input("trty"))

def van(n):
    for i in range(n+1):
        yield i


fun = van(n)

for i in fun:
    print(i)



