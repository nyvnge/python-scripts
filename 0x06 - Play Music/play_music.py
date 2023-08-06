import random
import os

music_directory = 'D:\Entertainment\Music\COMPILATIONS\90s Love Songs (2022)'
songs = os.listdir(music_directory)

song = random.randint(0, len(songs) - 1)

print(songs[song])

os.startfile(os.path.join(music_directory, songs[song]))
