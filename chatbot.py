import random 

def chat_bot():
    greetings = ['Hello', 'Hi', 'Hey', 'Hola', 'Greetings']
    questions = ['How are you?', 'What is your name?', 'How old are you?', 'Where do you live?', 'What do you do for a living?']
    answers = ['I am doing great, thank you!', 'My name is John Doe.', 'I am 25 years old.', 'I live in New York.', 'I am a software engineer.']
    while True:
        print(random.choice(greetings))
        user_response = input('User: ')
        if user_response.lower() == 'quit':
            break
        print(random.choice(questions))
        print(random.choice(answers))

if __name__ == '__main__':
    chat_bot()