import os
import hashlib

Archimedes  = "dat/"
Macintosh   = "dat/Apple - Macintosh - Datfile (365) (2020-08-26 18-45-58).dat"
JaguarCD    = "dat/Atari - Jaguar CD Interactive Multimedia System - Datfile (10) (2019-08-27 00-06-32).dat"
Pippin      = "dat/Bandai - Pippin - Datfile (14) (2020-01-26 12-06-14).dat"
Playdia     = "dat/Bandai - Playdia Quick Interactive System - Datfile (38) (2020-05-29 00-09-37).dat"
AmigaCD     = "dat/Commodore - Amiga CD - Datfile (354) (2020-08-01 16-08-34).dat"
AmigaCD32   = "dat/Commodore - Amiga CD32 - Datfile (160) (2020-08-26 18-45-51).dat"
AmigaCDTV   = "dat/Commodore - Amiga CDTV - Datfile (51) (2018-07-07 13-09-10).dat"
FujitsuFM   = "dat/Fujitsu - FM-Towns - Datfile (356) (2020-09-01 02-21-25).dat"
PhotoPlay   = "dat/funworld - Photo Play - Datfile (3) (2020-01-21 18-23-57).dat"
IBMPC       = "dat/IBM - PC compatible - Datfile (23507) (2020-09-01 11-57-10).dat"
Eagle       = "dat/Incredible Technologies - Eagle - Datfile (5) (2018-09-19 09-32-59).dat"
eAmusement  = "dat/Arcade - Konami - e-Amusement - Datfile (7) (2019-04-06 17-00-22).dat"
FireBeat    = "dat/Arcade - Konami - FireBeat - Datfile (8) (2019-04-06 16-58-55).dat"
System573   = "dat/"
SystemGV    = "dat/Arcade - Konami - System GV - Datfile (2) (2020-01-10 00-02-52).dat"
Twinkle     = "dat/"
FisherPrice = "dat/Mattel - Fisher-Price iXL - Datfile (16) (2019-10-05 18-37-18).dat"
HyperScan   = "dat/Mattel - HyperScan - Datfile (5) (2020-01-26 12-31-38).dat"
Memorex     = "dat/Memorex - Visual Information System - Datfile (68) (2019-08-21 08-22-43).dat"
Xbox        = "dat/Microsoft - Xbox - Datfile (2452) (2020-08-31 23-35-30).dat"
Triforce    = "dat/Arcade - Namco - Sega - Nintendo - Triforce - Datfile (20) (2020-01-15 22-48-13).dat"
System12    = "dat/"
System246   = "dat/Arcade - Namco - System 246 - Datfile (7) (2019-10-05 17-31-51).dat"
PCEngCDTurboGrafxCD = "dat/NEC - PC Engine CD & TurboGrafx CD - Datfile (527) (2020-08-23 15-49-38).dat"
PC88        = "dat/NEC - PC-88 series - Datfile (1) (2014-10-07 01-25-20).dat"
PC98        = "dat/NEC - PC-98 series - Datfile (36) (2020-08-29 22-47-56).dat"
PCFX        = "dat/NEC - PC-FX & PC-FXGA - Datfile (78) (2020-02-28 01-31-34).dat"
NeoGeoCD    = "dat/SNK - Neo Geo CD - Datfile (101) (2020-06-12 20-17-25).dat"
GCN         = "dat/Nintendo - GameCube - Datfile (1907) (2020-08-28 21-47-09).dat"
Wii         = "dat/Nintendo - Wii - Datfile (2019-05-04 18-00-53).dat"
PalmOS      = "dat/Palm - Datfile (5) (2020-07-22 18-49-25).dat"
Panasonic3DO = "dat/Panasonic - 3DO Interactive Multiplayer - Datfile (525) (2020-08-29 16-13-35).dat"
CDi         = "dat/Philips - CD-i - Datfile (238) (2020-08-21 14-47-04).dat"
PhotoCD     = "dat/Photo CD - Datfile (18) (2020-08-23 15-36-13).dat"
PSGameShark = "dat/PlayStation GameShark Updates - Datfile (23) (2020-06-27 18-14-10).dat"
SegaChihiro = "dat/Arcade - Sega - Chihiro - Datfile (16) (2020-01-15 19-00-40).dat"
SegaLindbergh = "dat/Arcade - Sega - Lindbergh - Datfile (7) (2018-06-16 09-37-24).dat"
SegaCD      = "dat/Sega - Mega CD & Sega CD - Datfile (531) (2020-08-20 01-26-37).dat"
SegaNaomi   = "dat/Arcade - Sega - Naomi - Datfile (14) (2020-04-12 04-16-05).dat"
SegaNaomi2  = "dat/Arcade - Sega - Naomi 2 - Datfile (6) (2020-04-05 17-25-30).dat"
SegaSaturn  = "dat/Sega - Saturn - Datfile (2315) (2020-08-29 17-07-01).dat"
TitanVideo  = "dat/"
SharpX68000 = "dat/"
PS1         = "dat/Sony - PlayStation - Datfile (10382) (2020-08-31 18-57-18).dat"
PS2         = "dat/Sony - PlayStation 2 - Datfile (9924) (2020-09-01 00-20-41).dat"
PSP         = "dat/Sony - PlayStation Portable - Datfile (2150) (2020-08-25 22-12-51).dat"
TABAustria  = "dat/TAB-Austria - Quizard - Datfile (9) (2018-05-25 07-27-39).dat"
iKTV        = "dat/"
KissSite   = "dat/Tomy - Kiss-Site - Datfile (2) (2017-11-19 19-09-40).dat"
VMLabsNUON  = "dat/VM Labs - NUON - Datfile (5) (2019-06-20 10-56-10).dat"
VTech       = "dat/VTech - V.Flash & V.Smile Pro - Datfile (37) (2020-01-25 16-57-25).dat"
ZAPiT       = "dat/ZAPiT Games - Game Wave Family Entertainment System - Datfile (16) (2018-12-08 16-42-20).dat"


read_size = 1024
hash = hashlib.md5()

print(""
    +"==================== Redump verifier - version 1.2 ====================\n"
    +"--------------------    Github.com/normalgamer     --------------------\n"
    +"\n"
    +"Select the ISO's system\n"
    +"\n"
    )

print(""
    +"1  - Acorn Archimedes                         28 - NEC PC-FX & PC-FXGA\n"
    +"2  - Apple Macintosh                          29 - Neo Geo CD\n"
    +"3  - Atari Jaguar CD                          30 - Nintendo Gamecube\n"
    +"4  - Bandai Pippin                            31 - Nintendo Wii\n"
    +"5  - Bandai Playdia                           32 - Palm OS\n"
    +"6  - Commodore Amiga CD                       33 - Panasonic 3DO Interactive Multiplayer\n"
    +"7  - Commodore Amiga CD32                     34 - Philips CDi\n"
    +"8  - Commodore Amiga CDTV                     35 - Photo CD\n"
    +"9  - Fujitsu FM Towns series                  36 - PlayStation GameShark Updates\n"
    +"10 - funworld Photo Play                      37 - Sega Chihiro\n"
    +"11 - IBM PC Compatible                        38 - Sega Dreamcast\n"
    +"12 - Incredible Technologies Eagle            39 - Sega Lindbergh\n"
    +"13 - Konami e-Amusement                       40 - Sega CD / Mega CD\n"
    +"14 - Konami FireBeat                          41 - Sega Naomi\n"
    +"15 - Konami System 573                        42 - Sega Naomi 2\n"
    +"16 - Konami System GV                         43 - Sega Saturn\n"
    +"17 - Konami Twinkle                           44 - Sega Titan Video\n"
    +"18 - Mattel Fisher-Price iXL                  45 - Sharp X68000\n"
    +"19 - Mattel HyperScan                         46 - Sony PlayStation\n"
    +"20 - Memorex Visual Information System        47 - Sony PlayStation 2\n"
    +"21 - Microsoft Xbox                           48 - PlayStation Portable\n"
    +"22 - Namco·Sega·Nintendo Triforce             49 - TAB-Austria Quizard\n"
    +"23 - Namco System 12                          50 - Tao iKTV\n"
    +"24 - Namco System 246                         51 - Tomy Kiss-Site\n"
    +"25 - NEC PC Engine CD & TurboGrafx CD         52 - VM Labs NUON\n"
    +"26 - NEC PC-88 series                         53 - VTech V.Flash & V.Smile Pro\n"
    +"27 - NEC PC-98 series                         54 - ZAPiT Games Game Wave Family Entertainment System\n"
    )

system = input("> ")

if system=="1":
    print(""
        +"\n"
        +"Acorn Archimedes datfile isn't up yet :C"
        +"\n"
    )
    input("\n")

elif system=="2":
    print(""
        +"\n"
        +"Drag and drop your Macintosh ISO into this window"
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
    
    with open(Macintosh) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Macintosh game MD5"
            )
        f.close()
        
    with open(Macintosh) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(Macintosh)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="3":
    print(""
        +"\n"
        +"Drag and drop your Atari Jaguar CD ISO into this window"
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
    
    with open(JaguarCD) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Jaguar CD game MD5"
            )
        f.close()
        
    with open(JaguarCD) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(JaguarCD)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="4":
    print(""
        +"\n"
        +"Drag and drop your Pippin ISO into this window"
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
    
    with open(Pippin) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Pippin game MD5"
            )
        f.close()
        
    with open(Pippin) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(Pippin)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="5":
    print(""
        +"\n"
        +"Drag and drop your Playdia ISO into this window"
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
    
    with open(Playdia) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Playdia game MD5"
            )
        f.close()
        
    with open(Playdia) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(Playdia)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="6":
    print(""
        +"\n"
        +"Drag and drop your Amiga CD ISO into this window"
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
    
    with open(AmigaCD) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Amiga CD game MD5"
            )
        f.close()
        
    with open(AmigaCD) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(AmigaCD)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="7":
    print(""
        +"\n"
        +"Drag and drop your Amiga CD32 ISO into this window"
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
    
    with open(AmigaCD32) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Amiga CD32 game MD5"
            )
        f.close()
        
    with open(AmigaCD32) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(AmigaCD32)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="8":
    print(""
        +"\n"
        +"Drag and drop your Amiga CDTV ISO into this window"
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
    
    with open(AmigaCD32) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            print("\n"
            +"ISO's MD5 doesn't match any AmigaCD32 game MD5"
            )
        f.close()
        
    with open(AmigaCD32) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(AmigaCD32)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="9":
    print(""
        +"\n"
        +"Drag and drop your Fujitsu FM ISO into this window"
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
    
    with open(FujitsuFM) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Fujitsu FM game MD5"
            )
        f.close()
        
    with open(FujitsuFM) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(FujitsuFM)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="10":
    print(""
        +"\n"
        +"Drag and drop your Photo Play ISO into this window"
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
    
    with open(PhotoPlay) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Photo Play game MD5"
            )
        f.close()
        
    with open(PhotoPlay) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PhotoPlay)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="11":
    print(""
        +"\n"
        +"Drag and drop your IBM PC ISO into this window"
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
    
    with open(IBMPC) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any IBM PC CD game MD5"
            )
        f.close()
        
    with open(IBMPC) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(IBMPC)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="12":
    print(""
        +"\n"
        +"Drag and drop your Eagle ISO into this window"
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
    
    with open(Eagle) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Eagle game MD5"
            )
        f.close()
        
    with open(Eagle) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(Eagle)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="13":
    print(""
        +"\n"
        +"Drag and drop your eAmusement ISO into this window"
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
    
    with open(eAmusement) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any eAmusement game MD5"
            )
        f.close()
        
    with open(eAmusement) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(eAmusement)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="14":
    print(""
        +"\n"
        +"Drag and drop your FireBeat ISO into this window"
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
    
    with open(FireBeat) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any FireBeat game MD5"
            )
        f.close()
        
    with open(FireBeat) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(FireBeat)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="15":
    print(""
        +"\n"
        +"System 573 datfile isn't up yet :C"
        +"\n"
    )   
    input("\n")

elif system=="16":
    print(""
        +"\n"
        +"Drag and drop your System GV ISO into this window"
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
    
    with open(SystemGV) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any System GV game MD5"
            )
        f.close()
        
    with open(SystemGV) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(SystemGV)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="17":
    print(""
        +"\n"
        +"Twinkle datfile isn't up yet :C"
        +"\n"
    )
    input("\n")

elif system=="18":
    print(""
        +"\n"
        +"Drag and drop your Fisher-Price iXL ISO into this window"
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
    
    with open(FisherPrice) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Fisher-Price iXL game MD5"
            )
        f.close()
        
    with open(FisherPrice) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(FisherPrice)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="19":
    print(""
        +"\n"
        +"Drag and drop your HyperScan ISO into this window"
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
    
    with open(HyperScan) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any HyperScan game MD5"
            )
        f.close()
        
    with open(HyperScan) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(HyperScan)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="20":
    print(""
        +"\n"
        +"Drag and drop your Memorex Visual Information System ISO into this window"
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
    
    with open(Memorex) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Memorex Visual Information System game MD5"
            )
        f.close()
        
    with open(Memorex) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(Memorex)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="21":
    print(""
        +"\n"
        +"Drag and drop your Xbox ISO into this window"
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
    
    with open(Xbox) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Xbox game MD5"
            )
        f.close()
        
    with open(Xbox) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(Xbox)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="22":
    print(""
        +"\n"
        +"Drag and drop your Triforce ISO into this window"
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
    
    with open(Triforce) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Triforce game MD5"
            )
        f.close()
        
    with open(Triforce) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(Triforce)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="23":
    print(""
        +"\n"
        +"System 12 datfile isn't up yet :C"
        +"\n"
    )   
    input("\n")

elif system=="24":
    print(""
        +"\n"
        +"Drag and drop your System 246 ISO into this window"
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
    
    with open(System246) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any System 246 game MD5"
            )
        f.close()
        
    with open(System246) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(System246)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="25":
    print(""
        +"\n"
        +"Drag and drop your PC Engine CD / TurboGrafx CD ISO into this window"
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
    
    with open(PCEngCDTurboGrafxCD) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any PC Engine CD / TurboGrafx CD game MD5"
            )
        f.close()
        
    with open(PCEngCDTurboGrafxCD) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PCEngCDTurboGrafxCD)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="26":
    print(""
        +"\n"
        +"Drag and drop your PC-88 ISO into this window"
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
    
    with open(PC88) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any PC-88 game MD5"
            )
        f.close()
        
    with open(PC88) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PC88)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="27":
    print(""
        +"\n"
        +"Drag and drop your PC-98 ISO into this window"
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
    
    with open(PC98) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any PC-98 game MD5"
            )
        f.close()
        
    with open(PC98) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PC98)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="28":
    print(""
        +"\n"
        +"Drag and drop your PC-FX / PC-FXGA ISO into this window"
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
    
    with open(PCFX) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any PC-FX / PC-FXGA game MD5"
            )
        f.close()
        
    with open(PCFX) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PCFX)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="29":
    print(""
        +"\n"
        +"Drag and drop your NeoGeo CD ISO into this window"
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
    
    with open(NeoGeoCD) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any NeoGeo CD game MD5"
            )
        f.close()
        
    with open(NeoGeoCD) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(NeoGeoCD)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="30":
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
    
    with open(GCN) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Gamecube game MD5"
            )
        f.close()
        
    with open(GCN) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(GCN)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="31":
    print(""
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
    
    with open(Wii) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Wii game MD5"
            )
        f.close()
        
    with open(Wii) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(Wii)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="32":
    print(""
        +"\n"
        +"Drag and drop your Palm OS ISO into this window"
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
    
    with open(PalmOS) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Palm OS game MD5"
            )
        f.close()
        
    with open(PalmOS) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PalmOS)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="33":
    print(""
        +"\n"
        +"Drag and drop your 3DO ISO into this window"
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
    
    with open(Panasonic3DO) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Playdia game MD5"
            )
        f.close()
        
    with open(Panasonic3DO) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(Panasonic3DO)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="34":
    print(""
        +"\n"
        +"Drag and drop your Philips CDi ISO into this window"
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
    
    with open(CDi) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Philips CDi game MD5"
            )
        f.close()
        
    with open(CDi) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(CDi)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="35":
    print(""
        +"\n"
        +"Drag and drop your Photo CD ISO into this window"
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
    
    with open(PhotoCD) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Photo CD game MD5"
            )
        f.close()
        
    with open(PhotoCD) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PhotoCD)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="36":
    print(""
        +"\n"
        +"Drag and drop your PlayStation Gameshark Update ISO into this window"
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
    
    with open(PSGameShark) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any PlayStation GameShark Update game MD5"
            )
        f.close()
        
    with open(PSGameShark) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PSGameShark)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="37":
    print(""
        +"\n"
        +"Drag and drop your Sega Chihiro ISO into this window"
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
    
    with open(SegaChihiro) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Sega Chihiro game MD5"
            )
        f.close()
        
    with open(SegaChihiro) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(SegaChihiro)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="38":
    print(""
        +"\n"
        +"Drag and drop your Sega Lindbergh ISO into this window"
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
    
    with open(SegaLindbergh) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Sega Lindbergh game MD5"
            )
        f.close()
        
    with open(SegaLindbergh) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(SegaLindbergh)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="39":
    print(""
        +"\n"
        +"Drag and drop your Sega CD / Mega CD ISO into this window"
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
    
    with open(SegaCD) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Sega CD / Mega CD game MD5"
            )
        f.close()
        
    with open(SegaCD) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(SegaCD)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="40":
    print(""
        +"\n"
        +"Drag and drop your Sega Naomi ISO into this window"
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
    
    with open(SegaNaomi) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Sega Naomi game MD5"
            )
        f.close()
        
    with open(SegaNaomi) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(SegaNaomi)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="41":
    print(""
        +"\n"
        +"Drag and drop your Sega Naomi 2 ISO into this window"
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
    
    with open(SegaNaomi2) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Sega Naomi 2 game MD5"
            )
        f.close()
        
    with open(SegaNaomi2) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(SegaNaomi2)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="42":
    print(""
        +"\n"
        +"Drag and drop your Sega Saturn ISO into this window"
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
    
    with open(SegaSaturn) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Sega Saturn game MD5"
            )
        f.close()
        
    with open(SegaSaturn) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(SegaSaturn)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="43":
    print(""
        +"\n"
        +"Sega Titan Video datfile isn't up yet :C"
        +"\n"
    )
    input("\n")

elif system=="44":
    print(""
        +"\n"
        +"Sharp X68000 datfile isn't up yet"
        +"\n"
    )
    input("\n")

elif system=="45":
    print(""
        +"\n"
        +"Drag and drop your PlayStation 1 ISO into this window"
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
    
    with open(PS1) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any PlayStation 1 game MD5"
            )
        f.close()
        
    with open(PS1) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PS1)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="46":
    print(""
        +"\n"
        +"Drag and drop your PlayStation 2 ISO into this window"
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
    
    with open(PS2) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any PlayStation 2 game MD5"
            )
        f.close()
        
    with open(PS2) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PS2)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="47":
    print(""
        +"\n"
        +"Drag and drop your PlayStation Portable ISO into this window"
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
    
    with open(PSP) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any PlayStation Portable game MD5"
            )
        f.close()
        
    with open(PSP) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(PSP)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="48":
    print(""
        +"\n"
        +"Drag and drop your TAB-Austria Quizard ISO into this window"
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
    
    with open(TABAustria) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any TAB-Austria Quizard game MD5"
            )
        f.close()
        
    with open(TABAustria) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(TABAustria)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="49":
    print(""
        +"\n"
        +"iKTV datfile isn't up yet :C"
        +"\n"
    )
    input("\n")

elif system=="50":
    print(""
        +"\n"
        +"Drag and drop your Kiss-Site ISO into this window"
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
    
    with open(KissSite) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Kiss-Site game MD5"
            )
        f.close()
        
    with open(KissSite) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(KissSite)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="51":
    print(""
        +"\n"
        +"Drag and drop your NUON ISO into this window"
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
    
    with open(VMLabsNUON) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any NUON game MD5"
            )
        f.close()
        
    with open(VMLabsNUON) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(VMLabsNUON)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="52":
    print(""
        +"\n"
        +"Drag and drop your VTech V.Flash / V.Smile ISO into this window"
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
    
    with open(VTech) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any VTech V.Flash / V.Smile game MD5"
            )
        f.close()
        
    with open(VTech) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(VTech)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

elif system=="53":
    print(""
        +"\n"
        +"Drag and drop your Game Wave Family Entertainment System ISO into this window"
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
    
    with open(ZAPiT) as f:
        if hash in f.read():
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"Game verified, ISO's MD5 matches Redump hash"
            )
        else:
            print("\n"
            +"ISO's MD5 hash: " + hash + "\n"
            +"\n"
            +"ISO's MD5 doesn't match any Game Wave Family Entertainment System game MD5"
            )
        f.close()
        
    with open(ZAPiT) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(ZAPiT)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("Redump game name: " + gameName)
                file.close
        f.close()
        
    input("\n")

