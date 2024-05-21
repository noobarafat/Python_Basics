command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car Started.. Ready to go")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car Stopped")
    elif command == "help":
        print("""
Start - to start the car
stop- to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand")




# import sys
# startCar = "Car started... Ready to go"
# stopCar = "Car stopped"
#
# userInput = input(">")
# if userInput.lower() == "help":
#     print("Start - to start the car")
#     print("Stop - to stop the car")
#     print("Quit - to exit")
#     helpInput = input(">")
#     if helpInput.lower() == "start":
#         print(startCar)
#     elif helpInput.lower() == 'stop':
#         print(startCar)
#     elif helpInput.lower() == 'quit':
#         sys.exit()
#     else:
#         print("I don't understand that")
# else:
#     print("I don't understand that")
