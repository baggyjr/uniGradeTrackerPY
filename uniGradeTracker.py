gradesY1 = {("Computer Ethics", 50), ("Computer Law and Cyber Security", 61), ("Computer Systems", 59), ("Computer Networks", 44), ("Mathematics for Computing", 60), ("C Programming 1", 54), ("C Programming 2", 46), ("Database Design and Implementation", 42)}
gradesY2 = {("Software and Security Management", 84), ("Windows Forensics", 75), ("Cyber Threat Intel & Incident Response", 64), ("Cryptography", 68), ("Penetration Testing", 40), ("Web Application Development", 60)}

print("Welcome to uni grade tracker!\n")
print("1. Show Y1 grades.")
print("2. Show Y2 grades.")

mainMenu = input("Please input your desired option number.\n")
if mainMenu == '1':
    print(*gradesY1, sep="\n")
    avgY1 = input("Do you want to see the average of these grades? y/n\n")
    if avgY1 == 'y':
        print("52%")
if mainMenu == '2':
    print(*gradesY2, sep="\n")
    avgY2 = input("Do you want to see the average of these grades? y/n\n")
    if avgY2 == 'y':
        print("Waiting for 2 more grades.")


input('Press ENTER to exit')


