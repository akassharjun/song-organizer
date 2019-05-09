from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC

# Read ID3 tag or create it if not present
import os

import glob
mp3_files = glob.iglob('**/*.mp3', recursive=True)

for fname in mp3_files:
    print("-"*100)
    print(fname)
    try:
        tags = ID3(fname)
    except ID3NoHeaderError:
        print("ERROR", fname)
        continue

    print("-" * 100)
    print()

    print(str(tags["TIT2"]).upper(), "  -  ", str(tags["TPE1"]).upper())

    try:
        artistName = str(tags["TPE1"]).replace(";", ", ")
    except:
        print("ERROR", fname)
        continue

    try:
        genre = str(tags["TCON"]).replace(";", ", ")
    except:
        print("ERROR", fname)
        continue

    print()
    beforeArtistName = tags["TPE1"]
    beforeGenreName = tags["TCON"]
    arrow = "  ->  "

    tags["TPE1"] = TPE1(encoding=3, text=artistName)
    tags["TCON"] = TCON(encoding=3, text=genre)

    afterArtistName = tags["TPE1"]
    afterGenreName = tags["TCON"]

    print(beforeArtistName, arrow, afterArtistName)
    print(beforeGenreName, arrow, afterGenreName)

    print()

    print("COMPLETED", fname)

    tags.save(fname)

    print()
    print()
