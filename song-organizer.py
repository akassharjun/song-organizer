import os
import glob
import shutil
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC


class SongOrganizer:

    def __init__(self):
        self.title = ""
        self.artist = ""
        self.album = ""
        self.genre = ""
        self.oldPath = ""
        self.newPath = ""
        self.newName = ""

    def initializeID3Tags(self, tags, oldPath):
        self.title = str(tags["TIT2"]).replace("\\", "").replace("/", "")
        self.artist = str(tags["TPE1"]).replace(
            '/\\', "&").replace("/", "").replace('\\', '').split(',')[0]
        self.album = tags["TALB"]
        self.oldPath = oldPath
        try:
            self.genre = tags["TCON"]
        except KeyError:
            pass

    def createDirectories(self):
        try:
            self.newPath = "{0}/{0} - {1}".format(self.artist, self.album)
            os.makedirs(self.newPath)

        except FileExistsError:
            pass
        except:
            print("\nERROR : {}".format(self.oldPath))

    def renameFile(self):
        self.newName = "{0} - {1}.{2}".format(self.artist,
                                              self.title, self.fileFormat)

        renamePath = os.getcwd() + "/" + self.newName

        os.rename(self.oldPath, renamePath)

    def moveFile(self):
        self.newPath = "{0}/{1}/{2}".format(os.getcwd(),
                                            self.newPath, self.newName)
        shutil.move(self.newName, self.newPath)


songOrganizer = SongOrganizer()
mp3_files = glob.iglob('**/*.mp3', recursive=True)

for fname in mp3_files:
    try:
        tags = ID3(fname)
        songOrganizer.initializeID3Tags(tags, fname, 'mp3')
        songOrganizer.createDirectories()
        songOrganizer.renameFile()
        songOrganizer.moveFile()
    except ID3NoHeaderError:
        print("Error : ", fname)
        continue
