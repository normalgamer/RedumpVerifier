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
gameVerified = False

dats = Macintosh, JaguarCD, Pippin, Playdia, AmigaCD, AmigaCD32, AmigaCDTV, FujitsuFM, PhotoPlay, IBMPC, Eagle, eAmusement, FireBeat, SystemGV, FisherPrice, HyperScan, Memorex, Xbox, Triforce, System246, PCEngCDTurboGrafxCD, PC88, PC98, PCFX, NeoGeoCD, GCN, Wii, PalmOS, Panasonic3DO, CDi, PhotoCD, PSGameShark, SegaChihiro, SegaLindbergh, SegaCD, SegaNaomi, SegaNaomi2, SegaSaturn, PS1, PS2, PSP, TABAustria, KissSite, VMLabsNUON, VTech, ZAPiT

print(""
    +" ================== Redump verifier - version 1.4 ====================\n"
    +" -------------------    Github.com/normalgamer     --------------------\n"
    +"\n"
    +" Drag 'n Drop your ISO\n"
    +"\n"
    )
iso = input(" > ")
iso = iso.replace("\"","")

print("\n Calculating hash...")
with open(iso, "rb") as f:
    data = f.read(read_size)
    while data:
        hash.update(data)
        data = f.read(read_size)
hash = hash.hexdigest()

line_number=0
name_line=0


for dat in dats:
    with open(dat) as f:
        if hash in f.read():
            print("\n"
            +" ISO's MD5 hash: " + hash + "\n"
            +" \n"
            +" Game verified, ISO's MD5 matches Redump hash"
            )
            gameVerified = True
        else:
            pass
        f.close()
        
    with open(dat) as f:
        for line in f:
            line_number+=1
            if hash in line:
                name_line=line_number-1
                file = open(dat)
                all_lines=file.readlines()
                gameName=all_lines[name_line-1].replace("<description>","")
                gameName=gameName.replace("</description>","")
                gameName=gameName.replace("\t","")
                
                print("\n Redump game name: " + gameName)
                file.close()
        f.close()
    
    line_number = 0
    name_line = 0

if not gameVerified:
    print("\n"
    +" ISO's MD5: " + hash + "\n"
    +"\n"
    +" ISO's MD5 doesn't match any Redump hash"
    )


input()