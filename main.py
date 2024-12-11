# pseudo email system CTF by Benjamin Saravia
# WARNING: THIS CODE CONTAINS EMOJIS THAT SOME COMPILERS OR IDEs MAY NOT BE ABLE TO HANDLE.
# THERE AREN'T ANY TERRIBLE CONSEQUENCES BUT THE EMOJIS MIGHT NOT APPEAR DURING EXECUTION.

import time
import getpass # THIS LIBRARY MAY NOT IMPORT PROPERLY ON CERTAIN COMPILERS AND IDEs

# defining needed lists and variables
menuOptions = ["1. Register",
               "2. Exit"]

registeredMenuOptions = ["1. Log in",
                         "2. Exit"]

loggedinMenuOptions = ["1. View Emails",
                       "2. Submit Flag",]

finalMenu = "1. Submit Flag"

falseEmail1 = "johndoe190242@zmail.com"
falseEmail2 = "leocheektwiddler54@zmail.com"
falseEmail3 = "elizabethcharles@lexisnexis.zmail.com"

falseAddress1 = "notsuspicious@paybuddy.com"

# defining the function that contains the CTF games combined
def CTF():
    
    # try loop for error handling
    try:
        
        while True:
        
            # email test 1
            print("\nChecking for emails...")
            time.sleep(4)
            print("📧 SYSTEM: EMAIL RECEIVED! 📧\n")
            print(f"{falseEmail1} John Doe: Hey! Boss just told me that he needs "
                "an emergency $1,000, can you send it to him through this address: ")
            print(str(falseAddress1)) 
            decision1 = input("\nDo you send the money? (Y / N): >")

            # IF STATEMENT CTF GAME NUMBER 1
            # if the user chooses the WRONG input
            if decision1.upper() == "Y":
            
                time.sleep(1)
                print("\nNo! The email is suspicious and it's a clear scam.")
                print("Always verify the identity of the sender and call your boss "
                    "to verify if the request is true.")

                time.sleep(2)
                print("\n😥 You have failed the CTF. Exiting Z-Mail... ❌")
                break
        
            # if the user chooses the CORRECT input
            elif decision1.upper() == "N":
            
                time.sleep(1)
                print("Good work!")
                print("Always verify the identity of the sender and call your boss "
                    "to verify if the request is true.")
            
                print("\nSYSTEM: The email has been deleted and reported. 🗑️\n")
                
                for option in loggedinMenuOptions:
                    print(option)
                
                menuDecision = int(input('Choose here: '))
                if menuDecision == 2:
                    
                    print("\nYou don't have the flag yet! Try again later.")
                    continue
                
                # IF STATEMENT CTF GAME NUMBER 2
                elif menuDecision == 1:
                    
                    print("\nChecking for emails...")
                    time.sleep(5)
                    print("\n📧 SYSTEM: EMAIL RECEIEVED! 📧\n")
                    print(f"{falseEmail2} Leo C.: Hey fam. I was on my breaktime and I found this "
                          "cool game. Click the link below to download it!")
                    print("Download game here: FUNNYTROJANHORSE.exe")
                    decision2 = input("\nDo you click the link? (Y / N): >")
                    
                    if decision2.upper() == "Y":
                        
                        time.sleep(1)
                        print("SYSTEM ERROR: Your computer has been infected with a malicious program.")
                        print("\nNo! You should always check emails with suspicious links.")
                        print("Also, the link is called TROJAN HOURSE.")
                        
                        print("\n😥 You have failed the CTF. Exiting Z-Mail... ❌")
                        
                        break
                    
                    elif decision2.upper() == "N":
                        
                        time.sleep(1)
                        print("Great work!")
                        print("Always make sure to check any links attached to emails, "
                              "and enable anti-virus so it can scan for anything malicious in the download.")
            
                        print("\nSYSTEM: The email has been deleted and reported. 🗑️")
                        
                        for option in loggedinMenuOptions:
                            print(option)
                
                        menuDecision = int(input('Choose here: '))
                        
                        if menuDecision == 2:

                            print("\nYou don't have the flag yet! Try again later.")
                            
                            continue
                        
                        # IF STATEMENT CTF GAME NUMBER 3
                        elif menuDecision == 1:
                            
                            flag = "CTF{PY03_0807_KLDR}"
                            print("\nChecking for emails...")
                            time.sleep(10)
                            print("\n📧 SYSTEM: EMAIL RECEIEVED! 📧\n")
                            print(f"{falseEmail3} [CEO] Elizabeth Charles ✅: Hey Todd, it's Elizabeth from the "
                                  "meeting last Thursday. I am up to do a Google Meet at 6pm later today to "
                                  "further discuss your position at our company. To accept, click my link below: ")
                            print("https://googlemeet.invitiation/accept/code:WDNG-2094-64DB")
                            print("\nSYSTEM: We have reviewed this email and can confirm the link is safe from any "
                                  "phishing links. ✅")
                            decision3 = input("Do you click the link? (Y / N): >")
                            
                            # whether the uses prompts Y or N, they are right.
                            if decision3.upper() == "Y" or "N":
                                
                                time.sleep(1)
                                print("\nGood work! Always verify that the sender is someone you recognize and "
                                      "that their profile is real and in order before you click any of their "
                                      "links.")
                                time.sleep(5)
                                print("And as stated before, always have an antivirus on to check any links or downloads "
                                      "for malicious scripts or software.")
                                time.sleep(5)
                                print(f"\n🏳️ Here is your flag! {flag} 🏳️")
                                
                                # presenting the user with the final menu so they can submit their flag
                                # DECLARING NEW AND FINAL LOOP FOR THE CTF
                                while(decision3.upper() == "Y" or "N"):
                                    
                                    print("\nPlease choose an option to proceed:")
                                    print(finalMenu)
                                    menuDecision = int(input('Choose here: '))
                                    
                                    # if the user for some reason inputs anything other than 1
                                    if menuDecision != 1:
                                        
                                        print("\n🚨 SYSTEM ERROR: Please input a valid option. 🚨")
                                        continue
                                
                                    # THIS IS WHERE THE CTF ENDS
                                    # if the user inputs 1 as intended
                                    else:
                                        
                                        flagVerification = input("\nSubmit your flag here: ")
                                        
                                        # if the flag submission matches with the real flag
                                        if flagVerification == flag:
                                            
                                            print("\n🎉 You have finished the Z-Mail CTF! Congratulations! 🎉")
                                            break 
                                        
                                        # if it doesn't
                                        else:
                                        
                                            print("\n🚨 SYSTEM ERROR: The flag you entered is incorrect. Please try again. 🚨")      
                                            continue 
                                
                                # code ends here        
                                break
                            
                            # error will be raised if the user doesn't choose a valid input    
                            else:
                                
                                print("\n🚨 SYSTEM ERROR: Please input a valid option: 'Y' OR 'N'. 🚨\n")
                                continue
                            
                        # if the user chooses neither 1 or 2   
                        else:
            
                            continue
                        
                # if the user chooses neither 1 or 2   
                else:
            
                    continue        
                        
            # if the user chooses neither 1 or 2
            else:
            
                continue
        
    # ERROR HANDLING #        
    # if the user inputs any incorrect/invalid values
    except ValueError as Error1:
         
        print("\n")
        print(f"🚨 SYSTEM ERROR: {Error1} 🚨")
        print("Please try again.\n")
        
        main()
        
    # if the user prompts CTRL + C   
    except KeyboardInterrupt:
        
        print("\n")
        print("🚨 SYSTEM: CTRL + C detected. 🚨")
        error_resolve = input("Was this intentional? (Y / N): >")
        
        if error_resolve.upper() == "Y":
            
            print("\nClosing Z-Mail...")
            
        else:
            
            print("\nRe-opening Z-Mail...")
            main()

# defining the menu interface funciton for when the user has made an account
def RegisteredMenu(usernameValue, pinValue, emailValue):
    
    # try loop for error handling
    try: 
        
        while True:
        
            print("\nType:")
            for regOption in registeredMenuOptions:
            
                print(regOption)
        
            regChoice = int(input('> '))
        
            # if the user chooses to log in
            if regChoice == 1:
            
                username_verify = input("Enter your username here: ")
            
                if username_verify == usernameValue:
                
                    pin_verify = getpass.getpass("Confirm your PIN here (it will appear hidden): ")
                
                    if pin_verify == pinValue:
                    
                        print("Verifying...")
                        time.sleep(1)
                        print("\n✅ Verification successful! ✅")
                        print(f"Welcome, {emailValue}!")
                        
                        # calling the main CTF function once verification goes through
                        CTF()
                        break
                
                    else:
                    
                        print("\nVerifying...")
                        time.sleep(1)
                        print("\n❌ The username or PIN you entered was invalid. Please try again. ❌")

                else:
                    
                    print("🚨 SYSTEM: Invalid username. Please try again. 🚨")
            
            # if the user chooses to exit the program    
            elif regChoice == 2:
                
                print("\nExiting Z-Mail...")
                return
            
            # if the user doesn't choose from 1 or 2
            else:
                
                print("Invalid option. Please try again.")
                continue
    
    # if the user inputs something invalid        
    except ValueError:
        
        print("Please enter a valid menu option.")
        main()
    
    # if the user prompts CTRL + C   
    except KeyboardInterrupt:
        
        print("\n🚨 SYSTEM: CTRL + C detected. 🚨")
        error_resolve = input("Was this intentional? (Y / N): >")
        
        if error_resolve.upper() == "Y":
            
            print("\nClosing Z-Mail...")
            
        else:
            
            print("\nRe-opening Z-Mail...")
            main()
    
# defining the main function where other functions will be called in
# most of the main code will be in here
def main(): 
    
    # keeping everything in a try loop for error handling
    try:
        
        while True:
        
            print("🐍 Welcome to Z-Mail. 🐍\n")
            print("Type: ")
            for option in menuOptions:
                print(option)
    
            choice = int(input('> '))
    
            # if the user chooses to register 
            if choice == 1:
        
                print("=======================")
                print("Registeration screen")
                print("=======================\n")
        
                # user chooses their username and PIN for new account 
                username = input("Username: ")
                pin = getpass.getpass('4-digit PIN (it will appear hidden): ')
                pin = str(pin)

                # if the user's PIN is longer than 4 digits
                if len(pin) != 4:
            
                    print("\n🚨 SYSTEM ERROR: Account PIN must be 4 digits long. 🚨")
                    
                    continue
            
                else:
                
                    # concatenating the username with the zmail domain
                    email = f"{username}@zmail.com"
                    time.sleep(1.5)
                    print("\n📧 Account registered! 📧")
                    print(f"Your new Z-Mail account is {email}")
                
                    # calling the function so that the user can log back in and continue
                    # the CTF
                    RegisteredMenu(username, pin, email)
                    break
        
            # if the user chooses to exit out of the program    
            elif choice == 2:
            
                print("==========================")
                print("Thank you for using Z-Mail.")
                print("==========================")
            
                break
       
    # ERROR HANDLING #        
    # if the user inputs any incorrect/invalid values
    except ValueError as Error1:
         
        print("\n")
        print(f"🚨 SYSTEM ERROR: {Error1} 🚨")
        print("Please try again.\n")
        
        main()
        
    # if the user prompts CTRL + C   
    except KeyboardInterrupt:
        
        print("\n")
        print("🚨 SYSTEM: CTRL + C detected. 🚨")
        error_resolve = input("Was this intentional? (Y / N): >")
        
        if error_resolve.upper() == "Y":
            
            print("\nClosing Z-Mail...")
            
        else:
            
            print("\nRe-opening Z-Mail...")
            main()
            
                
main()
