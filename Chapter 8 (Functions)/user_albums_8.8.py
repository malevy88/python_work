def make_album(artist_name, album_name, number_of_songs=''):
    """Return a dictionary of information about an album."""
    album = {'artist': artist_name, 'album': album_name}
    if number_of_songs:
        album['number of songs'] = number_of_songs
    return album


while True:
    print("\nPlease enter the album's artist, title, and number of tracks:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
    album_name = input("Album name: ")
    if album_name == 'q':
        break
    number_of_songs = input("Number of songs: ")
    if number_of_songs == 'q':
        break
    album = make_album(artist_name, album_name, number_of_songs='')
    print(album)
