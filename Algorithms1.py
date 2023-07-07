# def factorial_iterative(n):
#     running_total = 1
#     for i in range(n+1,1,-1):
#         running_total *= i
#     return (running_total)
# print(factorial_iterative(10))


# def Recursion_Factorial1(n):
#     if n == 1:
#         return n
#     else:
#         temp = Recursion_Factorial1(n - 1)
#         temp*=n
#     return temp
# print(Recursion_Factorial1(5))


# START AT 0
# IF NO CARDS RETURN -1
# IF CARD DOES  != QUERY AND IS THE LAST ITEM IN THE LIST, RETURN -1
# IF CARD POSITION == QUERY, RETURN POSITION
# IF CARD != QUERY, POSITION += 1

def locate_cards(cards, query):
    position = 0
    while position < len(cards):
        if len(cards) == 0:
            return -1
        if position > len(cards):
            return -1
        if cards[position] == query:
            return position
        else:
            position += 1
    return -1








tests = []

tests.append({
    'input': {
    'cards': [14,12,1,9],
    'query': 12
    },
    'output': 1
})

tests.append({
    'input': {
    'cards': [],
    'query': 12
},
    'output': -1
})

tests.append({'input':{
    'cards': [6],
    'query': 6
},
    'output': 0
})

tests.append({
    'input': {
        'cards':[10,10,10,3,2,-1],
        'query':3
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [10,9,8,8,3,3,3,3,1],
        'query': 3
    },
    'output': 4
})

tests.append({
    'input': {
        'cards': [10,9,2,1,-10],
        'query': 19
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [-11,-1234,-1000000],
        'query': -11
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [-11],
        'query': -10
    },
    'output': -1
})

tests.append({
    'input':{
        'cards': [100,99,22,11,1],
        'query': 1
    },
    'output': 4
})

def testing():
    for test in tests:
        print(locate_cards(**test['input']) == test['output'])
    return
testing()

#Create a dictionary of "tests" with specific conditions and an expected result, then use this output to compare with the results of the function to determine if it is successful or not.