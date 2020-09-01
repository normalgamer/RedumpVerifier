import os
import hashlib

GCNDatfile = "Nintendo - GameCube - Datfile (1907) (2020-08-28 21-47-09).dat"
WiiDatfile = "Wii Redump(2019-05-04 18-00-53).dat"

read_size = 1024
hash = hashlib.md5()

print(""
    +"==================== Redump verifier - version 1.1 ====================\n"
    +"--------------------    Github.com/normalgamer     --------------------\n"
    +"\n"
    +"Select the ISO's system\n"
    +"\n"
    )
print(""
    +"1 - Gamecube\n"
    +"2 - Wii\n"
    +"\n"
    )

system = input("> ")

if system=="1":
    print(""
        +"\n"
        +"Drag and drop your Gamecube ISO into this window"
        +"\n"
    )
    iso = input("> ")
    iso = iso.replace("\"","")
    
    with open(iso, "rb") as f:
        data = f.read(read_size)
        while data:
            hash.update(data)
            data = f.read(read_size)
    hash = hash.hexdigest()
    
    line_number=0
    name_line=0
    
    with open(GCNDatfile) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 doesn't match any Gamecube game MD5"
            )
        f.close()
        
    with open(GCNDatfile) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(GCNDatfile)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")
    
elif system=="2":
    print(""
        +"\n"
        +"**WARNING**: the Wii Redump is incomplete. Some obscure games might be missing, there shouldn't be any problem though\n"
        +"\n"
        +"Drag and drop your Wii ISO into this window"
        +"\n"
    )
    iso = input("> ")
    iso = iso.replace("\"","")
    
    with open(iso, "rb") as f:
        data = f.read(read_size)
        while data:
            hash.update(data)
            data = f.read(read_size)
    hash = hash.hexdigest()
    
    line_number=0
    name_line=0
    
    with open(WiiDatfile) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 doesn't match any Wii game MD5"
            )
        f.close()
        
    with open(WiiDatfile) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(WiiDatfile)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")
