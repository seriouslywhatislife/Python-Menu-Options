#Imports the time library (Used to allow time to read outputs)
import time
#Imports date and time library for the show date and time option
from datetime import datetime
#Imports socket library to show local computers name and IP Address
import socket
#Imports requests library (Used to download web pages in the 'Save web page' option)
import requests
#Takes certain libraries from the netmiko library (Used for option 3 and 4 on the menu to connect to a remote computer)
from netmiko import ( 
    ConnectHandler, 
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
    ssh_dispatcher,
)
#Imports the 'ConnectHandler' from 'ssh_dispatcher' (Also used for connecting to a remote computer)
from netmiko.ssh_dispatcher import(
    ConnectHandler,
)
#I have put the entire program in a 'While True' loop (Used for error handling e.g. if ctrl+C is pressed it won't throw a syntax error)
while True:
    #'Try' is used for the error handling. It runs the the code until ctrl+C is pressed then will jump to the 'KeyboardInturrupt' exception
    try:

        #'currentDateAndTime' is a variable I created for the line of code 'datetime.now()'. 'datetime.now()' will grab the local computers date and time
        currentDateAndTime = datetime.now()

        #'hostName' is a variable I created for 'socket.gethostname()'. 'socket.gethostname()' grabs the name of the local computer (e.g. Dan's-Computer)
        hostName = socket.gethostname()
        #'IPAddress' is a variable I created for 'socket.gethostbyname(hostname)'
        #'socket.gethostbyname(hostName)' pulls the IP address from the host name. This will output the IP address
        IPAddress = socket.gethostbyname(hostName)

        #I have used functions throughout the program - this makes handling a program more manageable, for example a menu, it makes it easier to go back to the menu at any point in the program as all I have to do is write the function anywhere in the program        
        def menu():
            #I have attached a variable named 'menuInput' this is so I can add an imput on a seperate line
            menuInput = print("""
            1. Show date and time (Local Computer)
            2. Show IP address (Local Computer)
            3. Show remote home directory listing
            4. Backup remote file
            5. Save web page

            Q. Quit

            """)

            #I have reffered to the 'menuInput' variable with an input attached to get the user to input an option
            menuInput = input("Please select and option: ")

            #I have used many empty print statements throughout the program to add spaces in the output - makes it cleaner for the end user
            print()

            #Here I have used 'if' and 'else' statements using the variable I attached to the print statement - If option 1 is entered in the input then it will take you to option 1, if option 2 is selected it will take you to option 2 etc.
            #This takes me back to the use of the 'def' function as this defines different parts of the code and makes it easier to jump around the program
            if menuInput == "1":
                dateAndTime()
            #'elif' in plain english means Else if - meaning if the original 'if' statement is not used it will keep jumping through the 'elif' statements until one of the statements has been satisfied
            elif menuInput == "2":
                showIpAddress()
            elif menuInput == "3":
                showRemoteHomeDirectory()
            elif menuInput == "4":
                backup()
            elif menuInput == "5":
                saveWebPage()
            elif menuInput == "Q":
                exit()

        #Define function for date and time option
        def dateAndTime():
            #Simple print statement that outputs 'The current date and time is' - after the comma I have used the variable I created for date and time - this will take the code attached to that variable and output the date and time 
            print("The current date and time is", currentDateAndTime)
            #'time.sleep()' is a line of code I have used a lot through out this program. I have used this through out this program to allow the end user time to read outputs. The number in the brackets refers to the amount of seconds you want the program to wait until it moves on
            time.sleep(5)
            #For your information, I am only going to run through this chunk of code once as I have re-used this chunk of code in every section as it is very simple and just works
            #I have called this variable 'userInput'. It will ask the user if they want to go back to the main menu after each menu option has been run, instead of just exiting the program
            #'userInput = print("Would you like to go back to the menu? (Y/N)")' will output 'Would you like to go back to the main menu
            userInput = print("Would you like to go back to the menu? (Y/N)")
            #This uses the variable attached to the print statement and makes it into an input
            userInput = input()

            #This section will run check to see if either "Y" or "N" has been inputted. Based on the response it will either quit the program or return the user to the main menu
            if userInput == "Y":
                print("Loading main menu...")
                time.sleep(2)
                #Returns you back to the main menu
                menu()
            elif userInput == "y":
                print("Loading main menu...")
                time.sleep(2)
                menu()
            elif userInput == "N":
                print("Closing program...")
                time.sleep(1.5)
                #Quits the program
                exit()
            elif userInput == "n":
                print("Closing program...")
                time.sleep(1.5)
                exit()


        def showIpAddress():
            print("Your Computer Name is " + hostName)
            print("Your Computer IP Address is " + IPAddress)
            time.sleep(5)
            userInput = print("Would you like to go back to the main menu? (Y/N)")
            userInput = input()

            if userInput == "Y":
                print("Loading main menu...")
                time.sleep(2)
                menu()
            elif userInput == "y":
                print("Loading main menu...")
                time.sleep(2)
                menu()
            elif userInput == "N":  
                print("Closing program...")
                time.sleep(1.5)
                exit()
            elif userInput == "n":
                print("Closing program...")
                time.sleep(1.5)
                exit()

        def showRemoteHomeDirectory():
            try:
                linuxDevice = {
                    'device_type': input("Please enter your device type: "),
                    'host': input("Please enter your host: "),
                    'port': input("Please enter your port: "),
                    'username': input("Please enter your username: "),
                    'password': input("Please enter your password: ")
                }

                net_connect = ConnectHandler(**linuxDevice)

                cmd = ['ls']
                output = ''

                for command in cmd:
                    output += net_connect.send_command(command)

                print()
                
                print("This is the contents of the home directory on the remote computer:")
                print(output)

                print()

            except ValueError as err:
                print()
                print("Oops something went wrong - Please try logging in again")
                print()
                showRemoteHomeDirectory()

            except NetMikoTimeoutException as err:
                print()
                print("Oops something went wrong - Please try logging in again")
                print()
                showRemoteHomeDirectory()
            
            except NetMikoAuthenticationException as err:
                print()
                print("Oops something went wrong - Please try logging in again")
                print()
                showRemoteHomeDirectory()

            userInput = print("Would you like to go back to the main menu? (Y/N)")
            userInput = input()

            if userInput == "Y":
                print("Loading main menu...")
                time.sleep(2)
                menu()
            elif userInput == "y":
                print("Loading main menu...")
                time.sleep(2)
                menu()
            elif userInput == "N":
                print("Closing program...")
                time.sleep(1.5)
                exit()
            elif userInput == "n":
                print("Closing program...")
                time.sleep(1.5)
                exit()


        def backup():
            try:
                net_connect = ConnectHandler(
                    device_type = input("Please enter your device type: "),
                    host = input("Please enter your host: "),
                    port = input("Please enter your port number: "),
                    username = input("Please enter your username: "),
                    password = input("Please enter your password: "),
                )         
                
                print()

                command = input("Please enter command to run (Don't include sudo): ")

                output = net_connect.send_command(command)
                print(output)

                print()

            except NetMikoTimeoutException as err:
                print()
                print("Oops something went wrong - Please try again")
                print()
                backup()

            except ValueError as err:
                print()
                print("Oops something went wrong - Please try again")
                print()
                backup()

            except NetMikoAuthenticationException as err:
                print()
                print("Username or Password is incorrect - Please try logging in again")
                print()
                backup()

            userInput = print("Would you like to go back to the main menu? (Y/N)")
            userInput = input()

            if userInput == "Y":
                print("Loading main menu...")
                time.sleep(2)
                menu()
            elif userInput == "y":
                print("Loading main menu...")
                time.sleep(2)
                menu()
            elif userInput == "N":
                print("Closing program...")
                time.sleep(1.5)
                exit()
            elif userInput == "n":
                print("Closing program...")
                time.sleep(1.5)
                exit()

        def saveWebPage():
            try:
                url = input("Please enter the url you would like to backup: ")
                print()
                
                r = requests.get(url, allow_redirects=True)

                fileType = input("Please tell me what extension you would like to use: ")

                open(fileType, 'wb').write(r.content)

            except requests.exceptions.MissingSchema as err:
                print()
                print("Invalid URL - Please try again")
                print()
                saveWebPage()

            except FileNotFoundError as err:
                print()
                print("No such file or directory - Please try again")
                print()
                saveWebPage()

            except requests.exceptions.ConnectionError as err:
                print()
                print("Something went wrong - Please try again")
                print()
                saveWebPage()

            userInput = print("Would you like to go back to the main menu? (Y/N)")
            userInput = input()

            if userInput == "Y":
                print("Loading main menu...")
                time.sleep(2)
                menu()
            elif userInput == "y":
                print("Loading main menu...")
                time.sleep(2)
                menu()
            elif userInput == "N":
                print("Closing program...")
                time.sleep(1.5)
                exit()
            elif userInput == "n":
                print("Closing program...")
                time.sleep(1.5)
                exit()

        menu()
    
    except KeyboardInterrupt as err:
        print("\nClosing program")
        quit()

#########
#SOURCES#
#########

#https://www.c-sharpcorner.com/blogs/how-to-find-ip-address-in-python
#https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/
#https://stackoverflow.com/questions/4028904/what-is-a-cross-platform-way-to-get-the-home-directory