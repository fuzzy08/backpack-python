import os
from pathlib import Path
import sys


def yaourt():
    print("In order for this program to work, you need to install yaourt.")
    print("Install yaourt? (y/n)")

    if(input() == 'y'):
        os.system("pacman -S yaourt")
    else:
        print("Terminating program...")
        sys.exit()

def install(program):
    print("installing " + program)
    
    # try:
    os.system("yaourt -S --noconfirm " + program)
    # except :


def main():
    devTools = ["base-devel",
                "atom",
                "discord",
                "firefox-developer-edition",
                "htop",
                "neofetch",
                "android-studio",
                "virtualbox",
                "intellij-community-edition"]


    yaourtFile = Path("/usr/bin/yaourt")
    k = 0
    if (yaourtFile.is_file() == False):
        yaourt()

        
    print("A python script by Zachary Quinn that installs preselected software on an arch-based OS")
    print("")
    print("yaourt is installed")
    print("---------------------------------")

    def options():
        print("OPTIONS:")
        print("'l' to list default packages")
        print("'h' for list of available options")
        print("'a' to install all programs")
        print("'s' to search for a package via yaourt")
        print("'[name of program]' to install a program. (warning: --noconfirm option set by defualt)")
        print("'q' to quit.")
        

        
    options()
    
    decision = input()
    
    os.system("clear")
    while(decision != 'q'):
        if (decision == 'l'):
            
            for i in devTools:
                print(i)
        elif (decision == 'a'):
            print("getting gpg keys for libc++ (for discord)")
            os.system("gpg -recv-keys 0fC3042E345AD05D")
            for j in devTools:
                print("installing " + j)
                os.system("yaourt -S --noconfirm " + j)
        elif (decision == 'q'):
            print("terminating program...")
            sys.exit()   
        elif (decision == 'h'):
            options()
        elif (decision == 's'):
            print("searching for '" + decision +"'")
            os.system("yaourt -Ss " + decision)
        else:
            print("attempting to install " + decision + "...")
            os.system("yaourt -S --noconfirm " + decision)
        
        decision = input("please enter a command: ")
        

if __name__ == "__main__":
    main()