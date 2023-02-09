HELP = '''
start - to start the car
stop - to stop the car
quit - to exit
'''

COMMAND = ""
STARTED = False

while True:
    COMMAND = input("> ").lower()
    if COMMAND == 'start':
        if STARTED:
            print('Car is already STARTED!')
        else:
            STARTED = True
            print('Car STARTED...Ready to go!')
    elif COMMAND == 'stop':
        if not STARTED:
            print('Car is stopped already!')
        else:
            STARTED = False
            print('Car stopped')
    elif COMMAND == 'HELP':
        print(HELP)
    elif COMMAND == 'quit':
        break
    else:
        print("Sorry, I don't understand that..")
