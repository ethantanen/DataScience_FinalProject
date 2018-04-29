import spotipy as spt
import spotipy.util as util

#update with current user
username = 'ethantanen'

#scope of queries, api thing
scope = 'user-library-read'

#get token
token = util.prompt_for_user_token(username, scope)

#instantiate a spotify object with the token
#TODO: should check if token is null
spotify = spt.Spotify(auth=token)

#get featured playlists from spotify
result = spotify.featured_playlists()

#Architecture of returned data is in another file
playlist = result['playlists']['items']

#Cycle through the list of playlists and add tracks to the list below
playlist_tracks = {}
for plist in playlist:
	#Get the tracks from the playlist
	playlist_tracks[plist['name']] = spotify.user_playlist(plist['owner']['id'], plist['id'], fields="tracks")


for i in playlist_tracks:
	print(playlist_tracks[i]['tracks']['items'][1]['track']['track'])
	break
