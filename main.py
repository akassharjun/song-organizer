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
        self.fileFormat = ""
        self.tags = ID3()

    def initializeID3Tags(self, tags, oldPath, fileFormat):
        # self.tags["TIT2"] = TIT2(encoding=3, text=title)
        # self.tags["TALB"] = TALB(encoding=3, text=u'mutagen Album Name')
        # self.tags["TPE2"] = TPE2(encoding=3, text=u'mutagen Band')
        # self.tags["COMM"] = COMM(encoding=3, lang=u'eng',
        #                     desc='desc', text=u'mutagen comment')
        # self.tags["TPE1"] = TPE1(encoding=3, text=u'mutagen Artist')
        # self.tags["TCOM"] = TCOM(encoding=3, text=u'mutagen Composer')
        # self.tags["TCON"] = TCON(encoding=3, text=u'mutagen Genre')
        # self.tags["TDRC"] = TDRC(encoding=3, text=u'2010')
        # self.tags["TRCK"] = TRCK(encoding=3, text=u'track_number')
        self.title = str(tags["TIT2"]).replace("\\", "").replace("/", "")
        self.artist = str(tags["TPE1"]).replace(
            '/\\', "&").replace("/", "").replace('\\', '').split(',')[0]
        self.album = tags["TALB"]
        try:
            self.genre = tags["TCON"]
        except KeyError:
            print("EEEEE" * 100)
        self.oldPath = oldPath
        self.fileFormat = fileFormat
        self.tags = tags

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
        print()
        print(self.newPath)
        print()
        shutil.move(self.newName, self.newPath)

    # def renameArtistField(self):
    #     print("-"*100)
    #     print(self.oldPath)

    #     print("-" * 100)
    #     print()

    #     print({0} - {1}, self.artist, self.title)

    #     try:
    #         artistName = str(self.artist).replace(";", ", ")
    #     except:
    #         print("ERROR ", self.oldPath)

    #     try:
    #         genre = str(self.artist).replace(";", ", ")
    #     except:
    #         print("ERROR ", self.oldPath)

    #     print()
    #     beforeArtistName = self.artist
    #     beforeGenreName = self.genre
    #     arrow = "  ->  "

    #     if (beforeArtistName != ""):
    #         self.tags["TPE1"] = TPE1(encoding=3, text=artistName)
    #         afterArtistName = self.tags["TPE1"]
    #         print(beforeArtistName, arrow, afterArtistName)

    #     if (beforeGenreName != ""):
    #         self.tags["TCON"] = TCON(encoding=3, text=genre)
    #         afterGenreName = self.tags["TCON"]
    #         print(beforeGenreName, arrow, afterGenreName)

    #     print()

    #     print("COMPLETED", self.oldPath)

    #     self.tags.save(self.oldPath)

    #     print()
    #     print()


songOrganizer = SongOrganizer()
mp3_files = glob.iglob('**/*.mp3', recursive=True)
# flac_files = glob.iglob('**/*.flac', recursive=True)

for fname in mp3_files:
    try:
        tags = ID3(fname)
        songOrganizer.initializeID3Tags(tags, fname, 'mp3')
        # songOrganizer.renameArtistField()
        songOrganizer.createDirectories()
        songOrganizer.renameFile()
        songOrganizer.moveFile()
    except ID3NoHeaderError:
        print("Error")
        continue


# for fname in flac_files:
#     try:
#         tags = ID3(fname)
#         songOrganizer.initializeID3Tags(tags, fname, 'flac')
#         songOrganizer.renameArtistField()
#         songOrganizer.createDirectories()
#         songOrganizer.renameFile()
#         songOrganizer.moveFile()
#     except ID3NoHeaderError:
#         print("Error")
#         continue
