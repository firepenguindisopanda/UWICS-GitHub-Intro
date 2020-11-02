
def sayHello(name):
    return f'Hello {name.capitalize()}'

def askQuestion(name):
    message = sayHello(name)
    question = "What colour do you like?"
    return f'{message}, {question}\n'


reply = input("What is your name?:\n")

response = askQuestion(reply)

print(response)

