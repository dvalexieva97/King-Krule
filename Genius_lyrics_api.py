
import lyricsgenius
import csv

data = open('TheOoz.txt')

'''
with open('TheOoz.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


n = 1
for song in data:
    print(f"This is song {n}: {song}\n")
    n+=1
#print(song)
'''

genius = lyricsgenius.Genius("Db2E_D9WvlvvFGqrkMRjc0TEk78w0jzd1KJHhETBlyZ9HXv5b7TJr4tGRADQkgWH")
#artist = genius.search_artist("King Krule", max_songs = 4, sort="title")
#genius.search_song($0)


for title in data:
    print(title)
    song = genius.search_song(title, 'King Krule')
    #.add_song(song)
    #song.save_lyrics() #format='json')
    #print(artist.songs)
    lyrics = song.lyrics
    print(lyrics)
    inp = str(input())
    lyrics_file = open('lyrics_Ooz.txt','a+', encoding="utf-8")
    lyrics_file.write(f"Title of song is: {title} \n")
    lyrics_file.write(str(lyrics))
    lyrics_file.write("\n\n ---------------------\n\n")
    lyrics_file.close()
    continue
'''
    if inp == 'yes':
        lyrics_file = open('lyrics_Ooz.txt','a+', encoding="utf-8")
        lyrics_file.write(f"Title of song is: {title} \n")
        lyrics_file.write(str(lyrics))
        lyrics_file.write("\n\n ---------------------\n\n")
        lyrics_file.close()
    else:
        pass
'''
