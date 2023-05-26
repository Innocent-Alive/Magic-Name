#This Code Can Generate Your Name Into A Digital Art using ASCII codes

import fontstyle
from colorama import *

print(Fore.RED + "Follow the format \'(name)\' or you can use symbols like ! @ # $ % & ^ after or before the name to see magic!")
name = input(Fore.RESET + "Enter Your Name To See Magic:- ")

#add @ symbol first, then write your name, then add a fullstop in the end to see magic...

convert = fontstyle.apply(f"So Your Input Is \"{name}\" \n\n", 'red/blink/underline')
print(convert)
alpha = name.lower()

#Using try block to write the program
try:

    #converted the string into the lower case to use the for loop
    for can in alpha:
        if (can == "#") : #used the if Statement to print a artwork for wishing birthday
                          #use the @ symbol in th input to check
            birthday = fontstyle.apply("                   §§§§§§\n             §§§§  §§  §§ §§§§§§\n     §§  §§ §§  §§ §§§§§§ §§  §§ §§    §§\n"
                  "     §§  §§ §§§§§§ §§     §§§§§§  §§  §§\n     §§§§§§ §§  §§ §§     §§       §§§§\n"
                  "     §§  §§ §§  §§        §§        §§\n     §§  §§                         §§\n\n"
                  "       §§§§§§   §§  §§§§§  §§§§§§ §§  §§\n       §§   §§  §§  §§  §§   §§   §§  §§\n"
                  "       §§§§§§   §§  §§§§§    §§   §§§§§§\n       §§   §§  §§  §§ §§    §§   §§  §§\n"
                  "       §§§§§§   §§  §§  §§   §§   §§  §§\n\n          §§§§§§§          §§    §§\n"
                  "           §§   §§   §§§§§  §§  §§\n           §§   §§  §§   §§  §§§§\n           §§   §§  §§§§§§§   §§\n"
                  "          §§§§§§§   §§   §§   §§\n                    §§   §§\n",'cyan/bold')
            print(birthday)
            cake = fontstyle.apply("\n                ¶¶\n               ¶¶¶¶               ¶¶\n"
                  "              ¶¶S¶¶      ¶¶     ¶¶¶¶\n             ¶¶SS¶     ¶¶¶¶    ¶¶SS¶\n             ¶¶S¶¶    ¶¶SS¶   ¶¶SS¶¶\n"
                  "              ¶¶      ¶SS¶     ¶SS¶\n             ¶¶¶¶¶     ¶¶       ¶¶\n             ¶  ¶¶    ¶¶¶¶¶    ¶¶¶¶¶\n"
                  "             ¶  ¶¶    ¶  ¶¶    ¶  ¶¶\n             ¶  ¶     ¶  ¶¶    ¶  ¶¶\n             ¶  ¶     ¶  ¶¶    ¶  ¶\n"
                  "             ¶  ¶     ¶  ¶     ¶  ¶\n           ¶¶¶  ¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶  ¶\n        ¶¶¶¶¶¶  ¶11111¶  ¶11111¶  ¶¶¶¶\n"
                  "      ¶¶¶1111¶  ¶11111¶  ¶11111¶  ¶11¶¶¶¶\n     ¶¶111$11¶¶¶¶11111¶  ¶11111¶¶¶¶11$11¶¶¶\n    ¶¶111$$$$11111$111¶¶¶¶11$1111111$$$$11¶¶\n"
                  "    ¶¶¶¶111$11111$$$$111111$$$$1111111$11¶¶¶\n    ¶  ¶¶¶¶¶¶¶¶1111$111111111$1111111¶¶¶¶¶ ¶\n   ¶¶      ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶¶\n"
                  " ¶¶¶¶     §§                        §§  ¶¶11¶¶\n¶¶11¶¶  §§ §§   §§     §§    §§   §§ §§ ¶¶111¶\n"
                  "¶111¶¶¶   §§   §§ §§  §§ §§ §§ §§   §§ ¶¶¶111¶\n¶1111¶¶¶¶        §§     §§    §§     ¶¶¶¶111¶¶\n"
                  "¶¶¶¶111¶¶¶¶¶¶¶¶¶¶¶        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶\n  ¶¶¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶\n"
                  "    ¶¶¶11111111111111111111111111111111111¶¶\n     ¶¶¶¶111¶¶¶¶11111111¶¶11111111¶¶¶¶1111¶¶\n"
                  "      ¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶1111¶¶¶ ¶¶¶¶¶¶¶\n               ¶¶¶¶¶¶¶¶   ¶¶¶¶¶¶¶¶\n\n",'purple/blink')
            print(cake)
        elif (can == "a") :    #prints letter A
            print(Fore.BLUE+"           #########\n           ##     ##\n           ##     ##\n           #########\n           ##     ##\n           ##     ##\n           ##     ##\n")
        elif (can == "b") :    #prints letter B
            print(Fore.BLUE+"           ######## \n           ##      ##\n           ##      ##\n           ######## \n           ##      ##\n           ##      ##\n           ######## \n")
        elif (can == "c"):    #prints letter C
            print(Fore.BLUE+"           ###### \n           ##    ##\n           ##     \n           ##     \n           ##     \n           ##    ##\n            ###### \n")
        elif (can == "d"):    #prints letter D
            print(Fore.BLUE+"           ####### \n           ##     ##\n           ##      ##\n           ##      ##\n           ##      ##\n           ##     ##\n           #######\n")
        elif (can == "e"):    #prints letter E
            print(Fore.BLUE+"           #######\n           ##\n           ##\n           #######\n           ##\n           ##\n           #######\n")
        elif (can == "f"):    #prints letter F
            print(Fore.BLUE+"           ########\n           ##\n           ######\n           ##\n           ##\n           ##\n")
        elif (can == "g"):    #prints letter G
            print(Fore.BLUE+"             ####\n           ##    ##\n          ##\n          ##   #####\n          ##      ##\n           ##    ##\n             ####\n")
        elif (can == "h"):    #prints letter H
            print(Fore.BLUE+"           ##     ##\n           ##     ##\n           ##     ##\n           #########\n           ##     ##\n           ##     ##\n           ##     ##\n")
        elif (can == "i"):    #prints letter I
            print(Fore.BLUE+"           ########\n              ##\n              ##\n              ##\n              ##\n              ##\n           ########\n")
        elif (can == "j"):    #prints letter J
            print(Fore.BLUE+"                  ##\n                  ##\n                  ##\n                  ##\n                  ##\n           ##     ##\n            #######\n")
        elif (can == "k"):    #prints letter K
            print(Fore.BLUE+"           ##    ##\n           ##   ##\n           ##  ##\n           ##### \n           ##  ##\n           ##   ##\n           ##    ##\n")
        elif (can == "l"):    #prints letter L
            print(Fore.BLUE+"           ##       \n           ##       \n           ##       \n           ##       \n           ##       \n           ##       \n           ########\n")
        elif (can == "m"):    #prints letter M
            print(Fore.BLUE+"           ##      ##\n          ## ##  ## ##\n          ##  ####  ##\n          ##   ##   ##\n          ##        ##\n          ##        ##\n")
        elif (can == "n"):    #prints letter N
            print(Fore.BLUE+"           ##     ##\n           ###    ##\n           ## #   ##\n           ##  #  ##\n           ##   # ##\n           ##    ###\n           ##     ##\n")
        elif (can == "o"):    #prints letter O
            print(Fore.BLUE+"             #####  \n           ##     ##\n           ##     ##\n           ##     ##\n           ##     ##\n           ##     ##\n             #####  \n")
        elif (can == "p"):    #prints letter P
            print(Fore.BLUE+"           ######## \n           ##     ##\n           ##     ##\n           ######## \n           ##      \n           ##      \n           ##      \n")
        elif (can == "q"):    #prints letter Q
            print(Fore.BLUE+"             ######  \n           ##      ##\n          ##        ##\n          ##        ##\n           ##   ## ##\n             ######  \n                 ## \n")
        elif (can == "r"):    #prints letter R
            print(Fore.BLUE+"           ######## \n           ##     ##\n           ##     ##\n           ####### \n           ##   ##  \n           ##    ## \n           ##     ##\n")
        elif (can == "s"):    #prints letter S
            print(Fore.BLUE+"             ######\n           ##\n           ##\n             ######\n                  ##\n                  ##\n            ######\n")
        elif (can == "t"):    #prints letter T
            print(Fore.BLUE+"           ##########\n               ##\n               ##\n               ##\n               ##\n               ##\n               ##\n")
        elif (can == "u"):    #prints letter U
            print(Fore.BLUE+"           ##     ##\n           ##     ##\n           ##     ##\n           ##     ##\n            ##   ##\n              ###\n")
        elif (can == "v"):    #prints letter V
            print(Fore.BLUE+"          ##       ##\n           ##     ##\n            ##   ##\n             ## ##\n              # #\n               #\n")
        elif (can == "w"):    #prints letter W
            print(Fore.BLUE+"          ##        ##\n          ##        ##\n          ##   ##   ##\n          ##  ####  ##\n          ## ##  ## ##\n           ##      ##\n")
        elif (can == "x"):    #prints letter X
            print(Fore.BLUE+"           ##      ##\n            ##    ##\n             ##  ##\n               ##\n             ##  ##\n            ##    ##\n           ##      ##\n")
        elif (can == "y"):    #prints letter Y
            print(Fore.BLUE+"           ##      ##\n            ##    ##\n             ##  ##\n               ##\n               ##\n               ##\n               ##\n")
        elif (can == "z"):    #prints letter Z
            print(Fore.BLUE+"           #########\n                 ##\n                ##\n               ##\n              ##\n             ##\n            #########\n")
        elif (can == " "):    #used elif statement for making spaces
            print(Fore.BLUE+"        \n        \n        \n        \n        \n")
        elif (can == "%"):   #used the elif statement that shows the I Love You sign
                             #use % symbol in the input to check
            ily = fontstyle.apply("        - - - - - - - - - - - - - -\n"
                  "        |                         |\n        |       ¶¶¶¶¶¶¶¶¶¶        |\n        |         ¶¶¶¶¶¶          |\n        |         ¶¶¶¶¶¶          |\n        |         ¶¶¶¶¶¶          |\n"
                  "        |         ¶¶¶¶¶¶          |\n        |         ¶¶¶¶¶¶          |\n"
                  "        |         ¶¶¶¶¶¶          |\n        |         ¶¶¶¶¶¶          |\n        |         ¶¶¶¶¶¶          |\n        |         ¶¶¶¶¶¶          |\n        |       ¶¶¶¶¶¶¶¶¶¶        |\n        |                         |\n"
                  "        |                         |\n        |    ¶¶¶¶¶       ¶¶¶¶¶    |\n        |  ¶¶¶¶¶¶¶¶¶   ¶¶¶¶¶¶¶¶¶  |\n        | ¶¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶¶ |\n"
                  "        | ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ |\n        |  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  |\n        |    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶    |\n"
                  "        |      ¶¶¶¶¶¶¶¶¶¶¶¶¶      |\n        |        ¶¶¶¶¶¶¶¶¶        |\n        |         ¶¶¶¶¶¶¶         |\n        |          ¶¶¶¶¶          |\n"
                  "        |           ¶¶¶           |\n        |            ¶            |\n        |                         |\n        |                         |\n        | ¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶ |\n        |   ¶¶¶¶¶         ¶¶¶¶¶   |\n"
                  "        |   ¶¶¶¶¶         ¶¶¶¶¶   |\n        |   ¶¶¶¶¶         ¶¶¶¶¶   |\n        |   ¶¶¶¶¶         ¶¶¶¶¶   |\n        |   ¶¶¶¶¶         ¶¶¶¶¶   |\n        |   ¶¶¶¶¶         ¶¶¶¶¶   |\n        |   ¶¶¶¶¶         ¶¶¶¶¶   |\n"
                  "        |   ¶¶¶¶¶¶       ¶¶¶¶¶¶   |\n        |    ¶¶¶¶¶¶     ¶¶¶¶¶¶    |\n        |      ¶¶¶¶¶¶¶¶¶¶¶¶¶      |\n        |        ¶¶¶¶¶¶¶¶¶        |\n"
                  "        |                         |\n        - - - - - - - - - - - - - -\n\n" , 'red/blink')
            print(ily)
        elif (can == "$"):   #used the elif statement that shows the smile emoji
                             #use the $ symbol in the input to check
            smile = ("                     *****************\n                ******               ******\n"
                     "            ****                           ****\n         ****                                 ***\n"
                     "       ***                                       ***\n      **           ***               ***           **\n"
                     "    **           *******           *******          ***\n   **            *******           *******            **\n"
                     "  **             *******           *******             **\n  **               ***               ***               **\n"
                     " **                                                     **\n **       *                                     *       **\n"
                     " **      **                                     **      **\n  **   ****                                     ****   **\n"
                     "  **      **                                   **      **\n   **       ***                             ***       **\n"
                     "    ***       ****                       ****       ***\n      **         ******             ******         **\n"
                     "       ***            ***************            ***\n         ****                                 ****\n"
                     "            ****                           ****\n                ******               ******\n"
                     "                     *****************\n\n")
            print(Fore.YELLOW + smile)
        elif (can == "!"):   #used the elif statement that shows the flower image
                             #use ! symbol in the input to check
            print(Fore.LIGHTMAGENTA_EX + "           .\n     ...  :``..\':\n      : ````.'   :\'\'::\'\n    ..:..  :     .\'\' :\n"
                      " ``.    `:    .\'     :\n     :    :   :        :\n      :   :   :         :\n      :    :   :        :\n"
                      "       :    :   :"+ Fore.LIGHTGREEN_EX +"..\'\'\'\'``::.\n        : ...:..\'     .\'\'\n        .\'   .\'  .::::\'\n"
                      "      :..\'\'\'``:::::::\n                `::::\n                   `::.\n                    `::\n"
                      "                     :::.\n          ..:.:.::\'`. ::\'`.  . : : .\n        ..\'      `:.: ::   :\'       .:\n"
                      "       .:        .:``:::  :       .: ::\n       .:    ..\'\'     :::.\'    :\':    :\n"
                      "        : .\'\'         .:: : : \'\n         :          .\'`::\n                       ::\n"
                      "                       ::\n                       ::\n                       ::\n                       ::\n"
                      "                       ::\n\n")
        elif (can == "@"):   #used the elif statement that shows the Love sign using @
                             #use @ symbol in the input to check
            heart = ("        @@@@@@@           @@@@@@@\n      @@@@@@@@@@@       @@@@@@@@@@@\n    @@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@\n"
                     "  @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@\n @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
                     "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
                     "  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
                     "      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n        @@@@@@@@@@@@@@@@@@@@@@@@@\n          @@@@@@@@@@@@@@@@@@@@@\n            @@@@@@@@@@@@@@@@@\n"
                     "              @@@@@@@@@@@@@\n                @@@@@@@@@\n                  @@@@@\n                   @@@\n                    @\n\n")
            print(Fore.RED + heart)
        elif (can == "&"):   #used the elif statement that shows the Love artwork
                             #use & symbol in the input to check
            love = ("            LoveLoveLov                eLoveLoveLo\n        veLoveLoveLoveLove          LoveLoveLoveLoveLo\n"
                    "     veLoveLoveLoveLoveLoveL      oveLoveLoveLoveLoveLove\n    LoveLoveLoveLoveLoveLoveL    oveLoveLoveLoveLoveLoveLo\n"
                    "   veLoveLoveLoveLoveLoveLoveL  oveLoveLoveLoveLoveLoveLove\n   LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove\n"
                    "   LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove\n    LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo\n"
                    "    veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove\n      LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo\n"
                    "        veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove\n          LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo\n"
                    "            veLoveLoveLoveLoveLoveLoveLoveLoveLove\n              LoveLoveLoveLoveLoveLoveLoveLoveLo\n"
                    "                veLoveLoveLoveLoveLoveLoveLove\n                  LoveLoveLoveLoveLoveLoveLo\n"
                    "                     veLoveLoveLoveLoveLo\n                         veLoveLoveLo\n                              ve\n")
            print(Fore.LIGHTRED_EX+love)
        elif (can == "^"):   #used the elif statement that shows a secret message to the haters
                             #use ^ symbol in the input to check
            print(Fore.LIGHTBLACK_EX + "     _         F U C K         _\n    |_|         Y O U         |_|\n    | |         /^^^\         | |\n   _| |_      (| \"o\" |)      _| |_\n"
                                        " _| | | | _    (_---_)    _ | | | |_\n| | | | |\' |    _| |_    | `| | | | |\n|          |   /     \   |          |\n \        /  / /(. .)\ \  \        /\n"
                                        "   \    /  / /  | . |  \ \  \    /\n     \  \/ /    || ||    \ \/  /\n      \__/      || ||      \__/\n               ooO Ooo\n")
        elif (can == "(" or can == ")"):  #used the elif statement that makes a top or bottom barder design
                                          #use ( ) symbol in the input to check  #you can add the input inside the ( ) symbols to make it look good
            print(Fore.LIGHTYELLOW_EX + ".-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.\n")
        else: #using else I printed a beautiful artwork
            print(Fore.LIGHTRED_EX + "Error!!!  " + Fore.BLUE + "Use Alphabets, @, !, $, #, %, &, ^ to run the program and see the magic")

#Using the exception block to ignore the errors
except ValueError:
    print("Enter Only Letters And Mentioned Symbols Please!!!")

#Using the finally block to print a fixed statement in the end
finally:
    print(Fore.LIGHTBLUE_EX + "\n\nI Hope You Liked It...")
    print(Fore.LIGHTBLUE_EX + "...created by the INNOCENT")
