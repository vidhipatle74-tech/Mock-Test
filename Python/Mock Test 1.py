#(1)--> S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org', 'python.py']
#             Out = {'com': ['jiocinema', 'amazon'], 'py': ['file', 'python'], 'html': ['web'], 'org': ['www']}
#             WAP to get the following output.

"""
S = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org', 'python.py']

def get_data(S):
    result = {}

    for item in S:
        name, extension = item.split('.')

        if extension not in result:
            result[extension] = []

        result[extension].append(name)

    print(result)


get_data(S)
"""
#O/P--> {'com': ['jiocinema', 'amazom'], 'py': ['file', 'python'], 'html': ['web'], 'org': ['www']}

#(2)--> S = 'kabab is love'
#              Out = {'kabab': ['babak', 2, 'kbb'], 'is': ['si', 1, 'i'], 'love': ['evol', 2, 'lv']}
#               WAP to get the following output.

"""
S = 'kabab is love'

def get_data(S):
    result = {}

    for word in S.split():
        reverse = word[::-1]
        count = len(word)

        unique = ''.join(set(word))

        result[word] = [reverse, count, unique]

    print(result)

get_data(S)
"""
#O/P--> {'kabab': ['babak', 5, 'bka'], 'is': ['si', 2, 'is'], 'love': ['evol', 4, 'oevl']}

#(3)--> In = 'bacbcaabbaa'
#              Out = b4a5c2
#              WAP to get the following output.
"""
In = 'bacbcaabbaa'

def count_char(In):
    result = ''

    for ch in In:
        if ch not in result:
            result = result + ch + str(In.count(ch))

    print(result)

count_char(In)
"""
#O/P--> b4a5c2

#(4)--> In = [100, 200, 50, 400, 300]
#              N = 300
#             Out = [[100, 200], [300]]
"""
In = [100, 200, 50, 400, 300]
N = 300

def get_data(In, N):
    result = []
    temp = []
    total = 0

    for num in In:
        if total + num <= N:
            temp.append(num)
            total = total + num
        else:
            result.append(temp)
            temp = [num]
            total = num

    result.append(temp)

    print(result)

get_data(In, N)
"""
#O/P--> [[100, 200], [50], [400], [300]]

#(5)--> WAP to find the HCF of two numbers.
"""
def hcf(a, b):
    while b != 0:
        a, b = b, a % b

    print("HCF =", a)


num1 = 12
num2 = 18

hcf(num1, num2)
"""
#O/P--> HCF = 6

#(6)--> WAP to convert binary to decimal.
"""
def binary_to_decimal(binary):
    decimal = 0
    power = 0

    while binary > 0:
        digit = binary % 10
        decimal = decimal + digit * (2 ** power)
        binary = binary // 10
        power = power + 1

    print("Decimal =", decimal)


num = 1011
binary_to_decimal(num)
"""
#O/P--> Decimal = 11

#(7)--> In = 'hello'
#             Out = {0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'e'}
"""
In = 'hello'

def get_data(In):
    result = {}

    for i in range(len(In)):
        result[i] = In[i]

    print(result)

get_data(In)
"""
#O/P--> {0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}

#(8)--> In = [100, 200, 35, 40, 60]
#             Out = [335, 235, 400, 395, 375]
"""
In = [100, 200, 35, 40, 60]

def get_sum(In):
    result = []

    for i in range(len(In)):
        total = 0

        for j in range(len(In)):
            if i != j:
                total = total + In[j]

        result.append(total)

    print(result)


get_sum(In)
"""
#O/P--> [335, 235, 400, 395, 375]

#(9)--> WAP to get the following output.
#              0 1 2 3 4 5 4 3 2 1
"""
def pattern():
    for i in range(6):
        print(i, end=" ")

    for i in range(4, 0, -1):
        print(i, end=" ")

pattern()
"""
#O/P--> 0 1 2 3 4 5 4 3 2 1

#(10)--> WAP to get the following output.
#                In = [3, 4j+9, 7.8, 5, -1, True, 2]
#               Out = [6, 4j+9, 7.8, 120, -1, True, 2]
"""
In = [3, 4j+9, 7.8, 5, -1, True, 2]

def change_list(In):
    result = []

    for x in In:
        if type(x) == int and x >= 0:
            fact = 1

            for i in range(1, x + 1):
                fact = fact * i

            result.append(fact)
        else:
            result.append(x)

    print(result)


change_list(In)
"""
#O/P-->  [6, (9+4j), 7.8, 120, -1, True, 2]

#(11)--> WAP to get the following output.
#                In = ['hai', [34+j, True, 78, 9+2j], 'sample', (3, 7j+9), {19+20j, 34, 89}, {'a':10}, 'data', [2+4j, 3.8,7.9]]
#                Out = ['iah', [3+4j, 9+2j], 'elpmas', (7+9j), {19+20j}, 'atad', [2+4j]]
"""
In = [
    'hai', [3+4j, True, 78, 9+2j],
    'sample',(3, 9+7j),
    {19+20j, 34, 89},{'a': 10},
    'data',[2+4j, 3.8, 7.9]
]

def get_data(In):
    Out = []

    for x in In:

        if type(x) == str:
            Out.append(x[::-1])

        elif type(x) == list:
            temp = []

            for i in x:
                if type(i) == complex:
                    temp.append(i)

            if temp:
                Out.append(temp)

        elif type(x) == tuple:
            temp = []

            for i in x:
                if type(i) == complex:
                    temp.append(i)

            if temp:
                Out.append(tuple(temp))

        elif type(x) == set:
            temp = set()

            for i in x:
                if type(i) == complex:
                    temp.add(i)

            if temp:
                Out.append(temp)

    print(Out)


get_data(In)
"""
#o/p--> ['iah', [(3+4j), (9+2j)], 'elpmas', ((9+7j),), {(19+20j)}, 'atad', [(2+4j)]]

#(12)--> WAO to get the following output .
#                 In = [10,7.8,323,1111,4j+6,7.8]
#                 Out=[(323,3),(1111,4)]
"""
In = [10, 7.8, 323, 1111, 4j+6, 7.8]

def get_data(In):
    Out = []

    for i in In:
        if type(i) == int:
            count = 0
            n = i

            while n > 0:
                n = n // 10
                count = count + 1

            if count >= 3:
                Out.append((i, count))

    print(Out)


get_data(In)

"""
#o/p-->
#              [(323, 3), (1111, 4)]












