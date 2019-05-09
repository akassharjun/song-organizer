# Song Organizer

## About

Ever had 'em songs with no proper file name and wanted them orgazined properly into folders? Here's a solution for it.

## Example

~~~
Desktop/song.mp3
will be
Desktop/Artist Name/Artist Name - Album Name/Artist Name - Title.mp3
~~~

## Requirements

* [Mutagen - Python Multimedia Tagging Library](https://mutagen.readthedocs.io/en/latest/)
* Python 3.5 or upwards
* Make sure the .mp3 files have proper ID3 tags.

## How To Use

Move the `song-id3-renamer.py` & `song-organizer` file to the directory in which you keep your songs in.

Type, and hit Enter
~~~
python3 song-id3-renamer.py
python3 song-organizer.py
~~~
