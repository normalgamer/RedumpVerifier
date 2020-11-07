# Redump Verifier
This script verifies game ISOs against the Redump hashes. It supports all the systems with downloadable dats plus the Wii dat, which is missing a few ISOs. Python 3 is needed to run it. [Download latest release](https://github.com/normalgamer/RedumpVerifier/releases/latest).

## Changelog
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
