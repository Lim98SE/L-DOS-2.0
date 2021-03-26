#wavread function
def wavread(song):
    import winsound
    print("Playing " + song)
    winsound.PlaySound(song, winsound.SND_FILENAME)


#boot function
def boot():
    import os
    import time
    import winsound
    import random
    import webbrowser
    if not os.path.exists("installed.txt"):
        print("Welcome to L-DOS! L-DOS 2.0 is a full")
        print("reprogramming of L-DOS and is meant for")
        print("more professional use. Think Windows NT")
        print("versus Windows 95/98/ME.")
        time.sleep(1)
        print("Well then, let's get this baby installed!")
        f = open("config.txt", "w+")
        f.write("")
        f = open("config.txt", "a")
        print("Let's start off small. What's your name?")
        f.write(input("")[0:20])
        print("Good!")
        f.write("""
""")
        print("Now, what buisness do you belong to?")
        print("It's fine to put nothing.")
        f.write(input("")[0:20])
        f.write("""
""")
        print("And that's it! If you ever need to edit these")
        print("options, go into config.txt.")
        print("L-DOS 2.0 will now reboot...")
        f = open("installed.txt", "w+")
        f.write("WHAT ARE YOU DOING HERE")
        time.sleep(1)
        boot()
    else:
        print("Welcome to L-DOS 2.0.")
        pd = os.getcwd()
        while 1 == 1:
            drive = os.getcwd()[0:3]
            command = input(drive)
            winsound.Beep(880, 100)
            if command == "break":
                print("L-DOS 2 has shut down.")
                break
            elif command == "dir":
                print (os.getcwd())
                for x in os.listdir():
                    print(x)
                    winsound.Beep(888, 10)
            elif "cd" in command:
                if os.path.exists(command[3:len(command)]):
                    pd = os.getcwd()
                    os.chdir(command[3:len(command)])
                else:
                    print("L-DOS 2 cannot find that path.")
            elif "wavfile" in command or "wavread" in command:
                filename = command[8:len(command)]
                if not '.wav' in command:
                    filename = filename + ".wav"
                print("Playing " + filename)
                winsound.PlaySound(filename, winsound.SND_FILENAME)
            elif "dirs" in command:
                tf = command[5:len(command)]
                for x in os.listdir():
                    if tf in x:
                        print(x)
            elif command in os.listdir():
                if ".wav" in command:
                    print("Playing " + command)
                    winsound.PlaySound(command, winsound.SND_FILENAME)
                elif ".txt" in command or ".py" in command or ".rtf" in command or ".ldos" in command:
                    c = command
                    f = open(c, "r")
                    print(f.read())
            elif command == "editor":
                print("Welcome to L-DOS 2.0 Editor.")
                print("Here is a list of keys you can use to do things")
                print("in the program:")
                print("""/ex to exit
/op to open a file
/nf to make a file""")
                txt = ""
                file = ""
                while not txt == "/ex":
                    txt = input("")
                    if txt == "/op":
                        file = input("What file to open? ")
                        if os.path.exists(file):
                            f = open(file, "r")
                        else:
                            print("Can't find that file.")
                    elif txt == "/nf":
                        file = input("What to name this file? " + ".txt")
                        f = open(file, "w+")
                    elif txt == "/ex":
                        print("Finished editing.")
                    else:
                        if not file == "":
                            f = open(file, "a+")
                            f.write(txt)
                            f.write("""
""")
                        else:
                            print("No file initalized.")
            elif "delfile" in command:
                if os.path.exists(command[8:len(command)]):
                    os.remove(command[8:len(command)])
                else:
                    print("File or directory not found: " + command[8:len(command)])
            elif command == "licence":
                f = open("config.txt", "r")
                print("This L-DOS 2.0 product is licenced to " + f.readline())
                print("The user of this L-DOS 2.0 product belongs to " + f.readline())
            elif command == "pd":
                os.chdir(pd)
            elif command == "variables":
                print("NOTE: THIS PROGRAM IS FOR DEBUGGING PURPOSES.")
                x = input("What file to write variable log to? ")
                f = open(x, "w+")
                f.write(os.getcwd())
                f.write("""
""")
                f.write(pd)
                f.write("""
""")
            elif command == "randomgen":
                open("RandomNumbers.ldos", "w+")
                for i in range(int(input("Input ammount of random numbers: "))):
                    f = open("RandomNumbers.ldos", "a+")
                    f.write(str(random.randrange(0, 9)))
                print("Outputted to RandomNumbers.ldos")
                if os.path.exists("decoder.ldos"):
                    print("Inset it into the decoder to see any messages.")
            elif command == "decoder":
                if os.path.exists("decoder.ldos"):
                    f = open("RandomNumbers.ldos", "r")
                    string = f.read()
                    f = open("Decoded.txt", "w+")
                    f = open("Decoded.txt", "a+")
                    for char in string:
                        if char == "0":
                            f.write("A")
                        elif char == "1":
                            f.write("B")
                        elif char == "2":
                            f.write("C")
                        elif char == "3":
                            f.write("D")
                        elif char == "4":
                            f.write("E")
                        elif char == "5":
                            f.write("F")
                        elif char == "6":
                            f.write("G")
                        elif char == "7":
                            f.write("H")
                        elif char == "8":
                            f.write("I")
                        elif char == "9":
                            f.write("J")
                    print("Output saved in decoded.txt.")
                else:
                    print("The decoder is not installed on your system.")
            elif command == "fshop":
                print("Welcome to the FSHOP 2.0!")
                print("Searching for functions...")
                time.sleep(1)
                print("Found two functions.")
                print("""1. RNG Decoder
2. Game Package
3. Calc""")
                print("What do you want to install?")
                c = input("")
                if c == "1":
                    if not os.path.exists("decoder.ldos"):
                        print("Creating decoder.ldos...")
                        open("decoder.ldos", "w+")
                        print("Decoder installed.")
                        f = open("cmdlist.txt", "a+")
                        f.write(""""
decoder - Opens RNG Decoder""")
                    else:
                        print("You already have this installed!")
                elif c == "2":
                    if not os.path.exists("games.ldos"):
                        print("Creating tune.ldos...")
                        open("tune.ldos", "w+")
                        print("Name that Tune installed.")
                        f = open("cmdlist.txt", "a+")
                        f.write(""""
nametune - Opens Name that Tune!""")
                    else:
                        print("You already have this installed!")
                elif c == "3":
                    if not os.path.exists("calc.ldos"):
                        print("Creating calc.ldos...")
                        open("calc.ldos", "w+")
                        print("Calculator installed.")
                        f = open("cmdlist.txt", "a+")
                        f.write("""
calc - Opens calculator""")
            elif command == "nametune":
                if not os.path.exists("tune.ldos"):
                    print("This is not installed on your system.")
                else:
                    print("Name that Tune")
                    score = 0
                    wavread("1.wav")
                    if input("").lower() == "megalovania":
                        print("Correct!")
                        score = score + 1
                    wavread("2.wav")
                    if input("").lower() == "big blue":
                        print("Correct!")
                        score = score + 1
                    wavread("3.wav")
                    if input("").lower() == "green hill zone":
                        print("Correct!")
                        score = score + 1
                    wavread("4.wav")
                    if input("").lower() == "title.wma":
                        print("Correct!")
                        score = score + 1
                    wavread("5.wav")
                    if input("").lower() == "mii maker theme":
                        print("Correct!")
                        score = score + 1
                    print("You got " + str(score) + " points!")
            elif command == "cmdlist":
                f = open("cmdlist.txt", "r")
                print(f.read())
            elif command == "website":
              print("Opening the L-DOS Website...")
              webbrowser.open("https://sites.google.com/view/l-dos-offical/home")
            elif command == "search":
              print("Opening Google...")
              webbrowser.open("https://www.google.com")
