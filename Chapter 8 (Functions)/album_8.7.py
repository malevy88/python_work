# write a function called make_album() that builds a dictionary describing
# a music album. The function should take an artist name and an album name. If
# the calling line includes a value for the number of songs, add that value to
# the album's dictionary. Make at least one new function call that includes the
# number of songs on an album

def make_album(artist_name, album_name, number_of_songs=''):
    """Return a dictionary of information about an album."""
    album = {'artist': artist_name, 'album': album_name}
    if number_of_songs:
        album['number of songs'] = number_of_songs
    return album


album = make_album('Tool', 'Lateralus', '13')
print(album)

album = make_album('Tool', '10,000 Days')
print(album)

album = make_album('Tool', 'Fear Inoculum', '10')
print(album)
