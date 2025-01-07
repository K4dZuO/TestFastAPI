def use_yield(a: int):
    
    a = 5
    yield a
    print("I alresady yielded the value")
    print("Now I'll return the value")
    yield a+1

var = use_yield(1)

for i in var:
    print(i)
# print(var)