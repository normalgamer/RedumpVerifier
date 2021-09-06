import os
import hashlib
import sys
import datetime


dats = os.listdir("./dat")
read_size = 1024
hash = hashlib.md5()
gameVerified = False
line_number = 0

romList = list()
romListRedumpName = list()
romListHash = list()


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


def verify(files):
    global romList, romListRedumpName, romListHash
    for file in files:
        gameVerified = False
        iso = file.replace("\"", "")
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
            with open("dat/" + dat, "r") as f:
                data = f.readlines()
                for line in data:
                    line_number += 1
                    if hash in line:
                        print("\n"
                              + "ISO's MD5 hash: " + hash
                              + "\n"
                              + "Game Verified, ISO's MD5 matches Redump hash"
                              )
                        name_line = line_number
                        while "<description>" not in data[name_line]:
                            name_line -= 1
                        gameName = data[name_line]\
                            .replace("<description>", "")\
                            .replace("</description>", "")\
                            .replace("\t", "")
                        print("Redump game name: " + gameName
                              + "\n"
                              + "----------------------------------------")
                        gameVerified = True

            if gameVerified:
                romListRedumpName.append(gameName)
                break

        if not gameVerified:
            print("ISO's MD5: " + hash
                  + "\n"
                  + "ISO's MD5 doesn't match any Redump hash"
                  + "\n"
                  + "\n"
                  + "----------------------------------------"
                  )
            romListRedumpName.append("Not verified")

        romListHash.append(hash)


# --------------------------------------------------------------------------- #
# Check for updates #
with open("dat/_last_update", "r") as f:
    last_update_time = f.read()


if (int(str(datetime.date.today()).split("-")[1]) >
    int(last_update_time.split("-")[1])) \
   | (int(str(datetime.date.today()).split("-")[0]) >
      int(last_update_time.split("-")[0])):
    print("DATs haven't been updated in at least one month")
    i = input("Do you want to update them? (y/n) > ")
    if i == "y":
        exec(open("dat_updater.py").read())
    else:
        pass


if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        if os.path.isfile(i.replace("\"", "")):  # if input is a file
            input_file = list()
            input_file.append(i)
            verify(input_file)

        elif os.path.isdir(i.replace("\"", "")):  # if input is a folder
            inputFolder = i.replace("\"", "")
            inputFiles = getAllFiles(inputFolder)
            verify(inputFiles)

        else:
            print("Something went wrong...")

    # if len(sys.argv) < 2:
    print("\n\nSummary:\n")
    for rom in romList:
        print(os.path.basename(rom) + " - " +
              romListRedumpName[romList.index(rom)])
        print(romListHash[romList.index(rom)])

    input()


else:
    print(""
          + "============   Redump verifier - version 1.9    ==============\n"
          + "------------       Github.com/normalgamer       --------------\n"
          + "\n"
          + "Drag 'n Drop your ISO or folder\n"
          + "If you want to verify multiple items, separate them by an"
          + "asterisk ( * )\n"
          + "\n"
          )

    userInput = input("> ")
    userInput = userInput.split("*")

    for i in userInput:
        print(i)
        if os.path.isfile(i.replace("\"", "")):  # if input is a file
            input_file = list()
            input_file.append(i)
            verify(input_file)

        elif os.path.isdir(i.replace("\"", "")):  # if input is a folder
            inputFolder = i.replace("\"", "")
            inputFiles = getAllFiles(inputFolder)
            verify(inputFiles)

        else:
            print("Something went wrong...")

    # if len(sys.argv) < 2:
    print("\n\nSummary:\n")
    for rom in romList:
        print(os.path.basename(rom) + " - " +
              romListRedumpName[romList.index(rom)])
        print(romListHash[romList.index(rom)])

    input()
