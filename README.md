# backpack-python

DESCRIPTION
==================
a program that quickly installs programs to a newly loaded arch OS. 

This script is intended for those who want a more automated "up and running" process with arch distrbutions. The script first 
checks if yaourt is installed, installs it if not (and user agrees), and gives the user the option
to install a pre-made set of programs or to install a program typed in. 

Each program will be installed using the --no-confirm option which ignores all the standard "are you sure" prompts. This is intended
to be used with programs that the user is already familiar with. Using this to install an unfamiliar program is not recommended.

This script is designed to be put on a flash drive, plugged in to a freshly installed os, and executed once per distro install. The 
script does not check if the package is already installed. Dependency errors can arise if the script runs twice. 

LIST OF COMMANDS:
=================

        'l' to list default packages in the devTools array defined at the top of the script
        'h' for list of available options
        'a' to install all programs in the devTools array
        's' to search for a package via yaourt. Color-scheme output not supported yet; meant for a quick search to ensure the user 
        types the name in correctly, not for browsing.
        
        '[name of program]' to install a program. (warning: --noconfirm option set by defualt)
        'q' to quit.
        
