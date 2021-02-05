# Redump Verifier
This script verifies game ISOs against the Redump hashes. It supports all the systems with downloadable dats plus the Wii dat, which is missing a few ISOs. Python 3 is needed to run it. [Download latest release](https://github.com/normalgamer/RedumpVerifier/releases/latest).


## Usage
There are three ways of using the script:

- Double-click on it to get a "GUI"

- Run it from the command line, passing the files/folders as arguments
  ```
  C:/RedumpVerifier.py /Gamecube /Wii/MarioKartWii.iso
  ```

- Drag & drop the files/folders you want to verify directly into the script

## Changelog

- 1.8b: typo

- 1.8:

  Code cleanup.

  You can now verify multiple files/folders at once, either from the command line or when double-clicking the script.

  Fixed a bug where the script would close before showing the summary.

- 1.7: You can add the file/folder you want to verify as an argument when you run `RedumpVerifier.py`, for example `RedumpVerifier.py "Super Smash Bros. Melee.iso"`

- 1.6: You can now drop a folder to verify all ISOs in it (note that it will try to verify ALL the files)

- 1.5:

  Optimization:
  - Once an ISO gets verified, the script breaks out of the loop instead of keeping opening the rest of the dats

  Updated a bunch of dats:
  - Apple - Macintosh
  - Arcade - Konami - System GV
  - Arcade - Namco - Sega - Nintendo - Triforce
  - Arcade - Sega - Chihiro
  - Arcade - Sega - Naomi
  - Bandai - Playdia Quick Interactive System
  - Commodore - Amiga CD
  - Commodore - Amiga CD32
  - Fujitsu - FM-Towns
  - IBM - PC Compatible
  - Microsoft - Xbox
  - NEC - PC Engine CD & Turbografx CD
  - NEC - PC-98
  - NEC - PC-FX & PC-FXGA
  - SNK - Neo Geo CD
  - Nintendo - Gamecube
  - Palm
  - Panasonic - 3DO Interactive Multiplayer
  - Philips - CD-i
  - Photo CD
  - Sega - Dreamcast
  - Sega - Mega CD & Sega CD
  - Sega - Saturn
  - Sony - PlayStation
  - Sony - PlayStation 2
  - Sony - PlayStation Portable
  - VTech - V.Flash & V.Smile Pro

- 1.4.4_01: Updated Gamecube dat (old: 2020/08, new 2020/11)

- 1.4.4: Fixed broken multi-file game support (some ISOs come in separated .bin tracks and a .cue file recognized by the emulator. The script was only working for single .iso files)

- 1.4.3: Code cleanup (rather than opening the dat 3 times (noice), open it once and do everything)

- v1.4.2b: Changed version number (I forgot on the previous 2)

- v1.4.2: Updated Wii dat (old: 2020/05, new: 2020/11)

- v1.4.1: Made it easier to add more dats

- v1.4: You no longer need to select the system

- v1.3: Fixed dat typo, MD5 hash is now displayed even if it doesn't match a Redump hash

- v1.2: Added support for all the platforms in the Redump dats

- v1.1: Added Wii game support

- v1.0: Initial commit
