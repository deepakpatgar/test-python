import streamlit as st
import os
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Global variables
playlist_songs = []
current_song = None
is_paused = False

# Function to handle volume change
def update_volume(value):
    pygame.mixer.music.set_volume(float(value) / 100)
    st.session_state['volume'] = value

# Function to add files to the playlist
def add_to_playlist():
    files = st.file_uploader("Select Songs", type=["mp3", "wav"], accept_multiple_files=True)
    if files:
        for file in files:
            playlist_songs.append(file)
        st.session_state['playlist'] = playlist_songs

# Function to remove selected files from the playlist
def remove_from_playlist():
    if 'playlist' in st.session_state:
        playlist_songs = st.session_state['playlist']
        selected_song = st.selectbox("Select Song to Remove", [song.name for song in playlist_songs])
        if selected_song:
            playlist_songs = [song for song in playlist_songs if song.name != selected_song]
            st.session_state['playlist'] = playlist_songs

# Function to shuffle the playlist
def shuffle_playlist():
    if 'playlist' in st.session_state:
        random.shuffle(st.session_state['playlist'])

# Function to play a song
def play_song(song_name=None):
    global current_song, is_paused
    if 'playlist' in st.session_state:
        if song_name:
            song_path = next(song for song in st.session_state['playlist'] if song.name == song_name)
        else:
            selected_song = st.selectbox("Select Song to Play", [song.name for song in st.session_state['playlist']])
            song_path = next(song for song in st.session_state['playlist'] if song.name == selected_song)
        if not is_paused:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()
        is_paused = False
        st.session_state['now_playing'] = song_path.name

# Function to pause a song
def pause_song():
    global is_paused
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        is_paused = True
        st.session_state['now_playing'] = "Paused"

# Function to stop a song
def stop_song():
    global is_paused
    pygame.mixer.music.stop()
    is_paused = False
    st.session_state['now_playing'] = "None"

# Function to handle next button click
def next_song():
    if 'playlist' in st.session_state and st.session_state['now_playing'] != "None":
        current_index = [song.name for song in st.session_state['playlist']].index(st.session_state['now_playing'])
        next_index = (current_index + 1) % len(st.session_state['playlist'])
        play_song(st.session_state['playlist'][next_index].name)

# Function to handle previous button click
def prev_song():
    if 'playlist' in st.session_state and st.session_state['now_playing'] != "None":
        current_index = [song.name for song in st.session_state['playlist']].index(st.session_state['now_playing'])
        prev_index = (current_index - 1) % len(st.session_state['playlist'])
        play_song(st.session_state['playlist'][prev_index].name)

# Function to filter playlist items based on search query
def filter_playlist(search_query):
    if 'playlist' in st.session_state:
        filtered_songs = [song for song in st.session_state['playlist'] if search_query.lower() in song.name.lower()]
        st.session_state['filtered_playlist'] = filtered_songs

# Streamlit UI
st.title("Music Player")

# CSS styling for better UI
st.markdown(
    """
    <style>
    .main {
        background-color: #282828;
        color: white;
    }
    .stButton>button {
        background-color: #1DB954;
        color: white;
        font-size: 16px;
        margin: 5px;
    }
    .stButton>button:hover {
        background-color: #1ED760;
        color: white;
    }
    .stSlider>div>div>div {
        background-color: #1DB954;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Control buttons
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button("Prev"):
        prev_song()
with col2:
    if st.button("Play"):
        play_song()
with col3:
    if st.button("Pause"):
        pause_song()
with col4:
    if st.button("Stop"):
        stop_song()
with col5:
    if st.button("Next"):
        next_song()
with col6:
    if st.button("Shuffle"):
        shuffle_playlist()

# Volume control
volume = st.slider("Volume", 0, 100, 50)
update_volume(volume)

# Playlist management
st.markdown("### Add Songs to Playlist")
add_to_playlist()

st.markdown("### Remove Songs from Playlist")
remove_from_playlist()

# Now playing label
st.markdown(f"### Now Playing: {st.session_state.get('now_playing', 'None')}")

# Search and filter playlist
search_query = st.text_input("Search Playlist")
if search_query:
    filter_playlist(search_query)

# Display playlist
if 'filtered_playlist' in st.session_state:
    st.write([song.name for song in st.session_state['filtered_playlist']])
else:
    st.write([song.name for song in st.session_state.get('playlist', [])])
