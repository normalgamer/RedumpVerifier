import os
import hashlib

dats = os.listdir("./dat")
read_size = 1024
hash = hashlib.md5()
gameVerified = False


print(""
    +"================== Redump verifier - version 1.4 ====================\n"
    +"-------------------    Github.com/normalgamer     --------------------\n"
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

line_number=0
name_line=0


for dat in dats:
    with open("dat/"+dat) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
            gameVerified = True
        else:
            pass
        f.close()
        
    with open("dat/"+dat) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open("dat/"+dat)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("\nRedump game name: " + gameName)
                file.close()
        f.close()
    
    line_number = 0
    name_line = 0

if not gameVerified:
    print("\n"
    +"ISO's MD5: " + hash + "\n"
    +"\n"
    +"ISO's MD5 doesn't match any Redump hash"
    )


input()