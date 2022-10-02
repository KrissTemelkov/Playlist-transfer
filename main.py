from SpotifyExtract import spotify_extract
from YoutubeImport import youtube_import

link = input("Spotify playlist link => ")
text_document = input("Do you want to store songs names in a text file? (Y)/(N) ")
gmail = input("gmail => ")
youtube_password = input("yotube_password => ")
playlist_name = input("name of the new playlist => ")


songs = spotify_extract(link)
songs.pop(0)
songs.pop(0)

if text_document.lower() == "y":
    with open("songs.txt", 'w') as f:
        f.write(f"songs = {len(songs)}")
        for song in songs:
            try:
                f.write(f"\n{song}")
            except UnicodeEncodeError:
                print(song)


print(f"songs = {len(songs)}")

youtube_import(gmail, youtube_password, playlist_name, songs)

print("done!")
