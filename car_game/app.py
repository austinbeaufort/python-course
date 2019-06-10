help = '''
start - to start the car
stop - to stop the car
quit - to exit
'''

command = ""
started = False

while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car started...Ready to go!')
    elif command == 'stop':
        if not started:
            print('Car is stopped already!')
        else:
            started = False
            print('Car stopped')
    elif command == 'help':
        print(help)
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that..")