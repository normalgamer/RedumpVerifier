import os
import hashlib

dats = os.listdir("./dat")
read_size = 1024
hash = hashlib.md5()
gameVerified = False
line_number=0


print(""
    +"================== Redump verifier - version 1.4.4 ====================\n"
    +"------------------      Github.com/normalgamer     --------------------\n"
    +"\n"
    +"Drag 'n Drop your ISO\n"
    +"\n"
    )
iso = input("> ")
iso = iso.replace("\"","")

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
    f.close()

if not gameVerified:
    print("\n"
         +"ISO's MD5: " + hash
         +"\n"
         +"ISO's MD5 doesn't match any Redump hash"
         )


input()