
def decimal2bin(decimal):
    stack = []
    while decimal > 0:
        stack.insert(0, str(decimal % 2))
        decimal //= 2

    result =  ''.join(stack)
    print(result)

decimal2bin(5)