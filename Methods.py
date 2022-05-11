#Method definations
def menu():
    print("Bonjour")
    print("i'm giving you 3 options")
    print("1. Tell me joke")
    print("2. Tell me riddle")
    print("3. Exit the selection")
    print("Choice is yours")
    choice = int(input()) 
    return choice





#Main program
menuChoice = menu() 

if menuChoice == 1:
    print("whats brown and sticky?") 
    print("A stick")
    
elif menuChoice == 2:
    print("My wife is leaving me because of my insecuritys.....")
