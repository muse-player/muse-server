import lyricsgenius

genius = lyricsgenius.Genius(
    'CENSORED',  # Client access token from Genius Client API page
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True
)
song = genius.search_song('Never Gonna Give You Up (2022 - Remaster)', 'Rick Astley')

print(song.lyrics)