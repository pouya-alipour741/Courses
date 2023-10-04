# command = ""
started = False
while True: #while command != 'quit'
    command = input('> ').lower()
    if command == "help":
         print("""start - to start the car
stop - to stop the car
quit - to exit""")
    elif command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print('car started')
    elif command == 'stop':
        if not started:
            print("car already stopped")
        else:
            started = False
            print("car stopped")
    elif command == 'quit':
         break
    else:
        print("sorry I don't understand")




