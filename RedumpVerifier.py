import os
import hashlib
import sys


dats = os.listdir("./dat")
read_size = 1024
hash = hashlib.md5()
sha_256 = hashlib.sha256()
gameVerified = False
line_number = 0


def getAllFiles(dirName):
    files = os.listdir(dirName)
    allFiles = list()

    for entry in files:
        fullpath = os.path.join(dirName, entry)
        if os.path.isdir(fullpath):
            allFiles = allFiles + getAllFiles(fullpath)
        else:
            allFiles.append(fullpath)

    return allFiles

def verify(file):
    gameVerified = False
    iso = file.replace("\"","")
    hash = hashlib.md5()
    print("\nCalculating hash...")
    with open(iso, "rb") as f:
        data = f.read(read_size)
        while data:
            hash.update(data)
            data = f.read(read_size)
    hash = hash.hexdigest()

    for dat in dats:
        line_number = 0
        data = ""
        with open("dat/" + dat) as f:
            data = f.readlines()
            for line in data:
                line_number += 1
                if hash in line:
                    print("\n"
                         +"ISO's MD5 hash: " + hash
                         +"\n"
                         +"Game Verified, ISO's MD5 matches Redump hash"
                         )
                    name_line = line_number
                    while "<description>" not in data[name_line]:
                        name_line -= 1
                    gameName = data[name_line].replace("<description>", "").replace("</description>", "").replace("\t", "")
                    print("\nRedump game name: " + gameName)
                    gameVerified = True


        if gameVerified:
            break

    if not gameVerified:
        print("\n"
             +"ISO's MD5: " + hash
             +"\n"
             +"ISO's MD5 doesn't match any Redump hash"
             )

def verify_multiple(files):

    romList = list()
    romListRedumpName = list()
    romListHash = list()

    for file in files:
        gameVerified = False
        iso = file.replace("\"","")
        print("\nISO: " + iso)
        hash = hashlib.md5()
        print("Calculating hash...")
        with open(iso, "rb") as f:
            data = f.read(read_size)
            while data:
                hash.update(data)
                data = f.read(read_size)
        hash = hash.hexdigest()

        romList.append(file)

        for dat in dats:
            line_number = 0
            data = ""
            with open("dat/" + dat) as f:
                data = f.readlines()
                for line in data:
                    line_number += 1
                    if hash in line:
                        print("\n"
                             +"ISO's MD5 hash: " + hash
                             +"\n"
                             +"Game Verified, ISO's MD5 matches Redump hash"
                             )
                        name_line = line_number
                        while "<description>" not in data[name_line]:
                            name_line -= 1
                        gameName = data[name_line].replace("<description>", "").replace("</description>", "").replace("\t", "")
                        print("Redump game name: " + gameName
                             +"\n"
                             +"----------------------------------------")
                        gameVerified = True

            if gameVerified:
                romListRedumpName.append(gameName)
                break

        if not gameVerified:
            print("ISO's MD5: " + hash
                 +"\n"
                 +"ISO's MD5 doesn't match any Redump hash"
                 +"\n"
                 +"\n"
                 +"----------------------------------------"
                 )
            romListRedumpName.append("Not verified")

        romListHash.append(hash)

    print("\n\nSummary:\n")
    for rom in romList:
        print(os.path.basename(rom) + " - " + romListRedumpName[romList.index(rom)])
        print(romListHash[romList.index(rom)])
        print("------------------------------\n")


# --------------------------------------------------------------------------- #

if len(sys.argv > 1):
    if os.path.isfile(sys.argv[1].replace("\"", "")):  # if input is a file
        verify(sys.argv[1])
        input()

    elif os.path.isdir(sys.argv[1].replace("\"", "")):  # if input is a folder
        inputFolder = sys.argv[1].replace("\"", "")
        inputFiles = getAllFiles(inputFolder)
        verify_multiple(inputFiles)

    else:
        print("Something went wrong...")


else:
    print(""
        +"==================    Redump verifier - version 1.7   ====================\n"
        +"------------------       Github.com/normalgamer       --------------------\n"
        +"\n"
        +"Drag 'n Drop your ISO or folder\n"
        +"\n"
        )
    userInput = input("> ")

    if os.path.isfile(userInput.replace("\"","")):  # if input is a file
        verify(userInput)
        input()

    elif os.path.isdir(userInput.replace("\"","")):  # if input is a folder
        inputFolder = userInput.replace("\"","")
        inputFiles = getAllFiles(inputFolder)
        verify_multiple(inputFiles)

    else:
        print("Something went wrong...")
