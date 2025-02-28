import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import os
import random

# Directory to save the icons
icons_dir = os.path.join(os.getcwd(), "icons")

# Function to load, resize, and convert images using Pillow
def load_image(file_path, size=(32, 32)):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return None
    try:
        image = Image.open(file_path)
        image = image.resize(size, Image.ANTIALIAS)  # Resize the image
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image {file_path}: {e}")
        return None

# Function to handle volume change
def update_volume(value):
    print(f"Volume set to: {value}")

# Function to handle equalizer band changes
def update_equalizer(value, band):
    print(f"Equalizer band {band} set to: {value}")

# Function for button hover effect
def on_enter(event):
    event.widget.config(style="TButtonHover")

def on_leave(event):
    event.widget.config(style="TButton")

# Function to add files to the playlist
def add_to_playlist():
    files = filedialog.askopenfilenames(title="Select Songs", filetypes=[("Audio Files", "*.mp3 *.wav")])
    for file in files:
        playlist.insert(tk.END, os.path.basename(file))
        playlist_songs.append(os.path.basename(file))  # Update playlist songs list

# Function to remove selected files from the playlist
def remove_from_playlist():
    selected_indices = playlist.curselection()
    for index in reversed(selected_indices):
        song = playlist.get(index)
        playlist.delete(index)
        playlist_songs.remove(song)  # Update playlist songs list

# Function to shuffle the playlist
def shuffle_playlist():
    songs = playlist.get(0, tk.END)
    random.shuffle(songs)
    playlist.delete(0, tk.END)
    for song in songs:
        playlist.insert(tk.END, song)

# Function to handle play button click
def play_song():
    selected = playlist.curselection()
    if selected:
        song = playlist.get(selected[0])
        now_playing.config(text=f"Now Playing: {song}")

# Function to handle stop button click
def stop_song():
    now_playing.config(text="Now Playing: None")

# Function to handle next button click
def next_song():
    current_index = playlist.curselection()
    if current_index:
        next_index = (current_index[0] + 1) % playlist.size()
        playlist.select_clear(current_index[0])
        playlist.select_set(next_index)
        play_song()

# Function to handle previous button click
def prev_song():
    current_index = playlist.curselection()
    if current_index:
        prev_index = (current_index[0] - 1) % playlist.size()
        playlist.select_clear(current_index[0])
        playlist.select_set(prev_index)
        play_song()

# Function to filter playlist items based on search query
def filter_playlist(event=None):
    search_query = search_entry.get().lower()
    playlist.delete(0, tk.END)
    for song in playlist_songs:
        if search_query in song.lower():
            playlist.insert(tk.END, song)

# Create the main window
root = tk.Tk()
root.title("Music Player")
root.geometry("700x700")
root.configure(bg="#282828")

# Load icons for buttons with desired size
icon_size = (32, 32)  # Adjust size as needed
play_icon = load_image(os.path.join(icons_dir, "play.png"), size=icon_size)
pause_icon = load_image(os.path.join(icons_dir, "pause.png"), size=icon_size)
stop_icon = load_image(os.path.join(icons_dir, "stop.png"), size=icon_size)
next_icon = load_image(os.path.join(icons_dir, "next.png"), size=icon_size)
prev_icon = load_image(os.path.join(icons_dir, "prev.png"), size=icon_size)
shuffle_icon = load_image(os.path.join(icons_dir, "shuffle.png"), size=icon_size)

# Ensure all icons were loaded successfully
if not all([play_icon, pause_icon, stop_icon, next_icon, prev_icon, shuffle_icon]):
    print("One or more icons failed to load.")
    root.destroy()  # Properly close the root if icons fail to load
    exit()

# Style for buttons and labels
style = ttk.Style()
style.configure("TButton",
                background="#1DB954",
                foreground="black",
                font=("Helvetica", 12),
                borderwidth=0,
                focusthickness=3,
                focuscolor="none")

style.configure("TButtonHover",
                background="#1ED760",  # Lighter green for hover
                foreground="black",
                font=("Helvetica", 12),
                borderwidth=0,
                focusthickness=3,
                focuscolor="none")

style.configure("TLabel",
                background="#282828",
                foreground="white",
                font=("Helvetica", 14))

style.configure("TProgressbar",
                thickness=20,
                troughcolor="#404040",
                background="#1DB954")

style.configure("TScale",
                background="#282828",
                troughcolor="#404040",
                sliderrelief="flat")

# Function to create buttons with icons
def create_button(frame, image, command=None):
    button = ttk.Button(frame, image=image, command=command, style="TButton")
    button.image = image
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button

# Frame for player controls
control_frame = tk.Frame(root, bg="#282828")
control_frame.pack(pady=10)

# Play, Pause, Stop, Previous, Next, Shuffle buttons
prev_button = create_button(control_frame, prev_icon, command=prev_song)
prev_button.grid(row=0, column=0, padx=10)

play_button = create_button(control_frame, play_icon, command=play_song)
play_button.grid(row=0, column=1, padx=10)

pause_button = create_button(control_frame, pause_icon)  # Pause functionality to be added
pause_button.grid(row=0, column=2, padx=10)

stop_button = create_button(control_frame, stop_icon, command=stop_song)
stop_button.grid(row=0, column=3, padx=10)

next_button = create_button(control_frame, next_icon, command=next_song)
next_button.grid(row=0, column=4, padx=10)

shuffle_button = create_button(control_frame, shuffle_icon, command=shuffle_playlist)
shuffle_button.grid(row=0, column=5, padx=10)

# Progress bar
progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", style="TProgressbar")
progress.pack(pady=20)

# Volume control slider
volume_frame = tk.Frame(root, bg="#282828")
volume_frame.pack(pady=10)
volume_label = ttk.Label(volume_frame, text="Volume", style="TLabel")
volume_label.pack(side="left", padx=10)
volume_slider = ttk.Scale(volume_frame, from_=0, to=100, orient="horizontal", style="TScale", command=update_volume)
volume_slider.set(50)  # Set default volume to 50%
volume_slider.pack(side="left")

# Now playing label
now_playing = ttk.Label(root, text="Now Playing: None", style="TLabel")
now_playing.pack(pady=20)

# Playlist management
playlist_frame = tk.Frame(root, bg="#282828")
playlist_frame.pack(pady=10)

# Search Entry
search_frame = tk.Frame(playlist_frame, bg="#282828")
search_frame.pack(pady=5)

search_label = ttk.Label(search_frame, text="Search Playlist", style="TLabel")
search_label.pack(side="left", padx=5)

search_entry = ttk.Entry(search_frame)
search_entry.pack(side="left", fill="x", expand=True)
search_entry.bind("<KeyRelease>", filter_playlist)  # Bind the entry to filter on key release

# Playlist Listbox
playlist_label = ttk.Label(playlist_frame, text="Playlist", style="TLabel")
playlist_label.pack()

playlist = tk.Listbox(playlist_frame, bg="#404040", fg="white", selectbackground="#1DB954", width=60, height=10)
playlist.pack(padx=10, pady=5)

# Add/Remove buttons for playlist
playlist_buttons_frame = tk.Frame(root, bg="#282828")
playlist_buttons_frame.pack(pady=10)

add_button = ttk.Button(playlist_buttons_frame, text="Add to Playlist", command=add_to_playlist, style="TButton")
add_button.pack(side="left", padx=10)

remove_button = ttk.Button(playlist_buttons_frame, text="Remove from Playlist", command=remove_from_playlist, style="TButton")
remove_button.pack(side="left", padx=10)

shuffle_button = ttk.Button(playlist_buttons_frame, text="Shuffle Playlist", command=shuffle_playlist, style="TButton")
shuffle_button.pack(side="left", padx=10)

# Equalizer frame
equalizer_frame = tk.Frame(root, bg="#282828")
equalizer_frame.pack(pady=10)

equalizer_title = ttk.Label(equalizer_frame, text="Equalizer", style="TLabel")
equalizer_title.pack(pady=5)

# Equalizer bands
equalizer_bands = ["60Hz", "150Hz", "400Hz", "1kHz", "2.5kHz", "6kHz", "12kHz", "14kHz"]
equalizer_sliders = {}

for band in equalizer_bands:
    band_label = ttk.Label(equalizer_frame, text=band, style="TLabel")
    band_label.pack(pady=5, anchor="w")
    band_slider = ttk.Scale(equalizer_frame, from_=0, to=100, orient="horizontal", style="TScale",
                            command=lambda value, b=band: update_equalizer(value, b))
    band_slider.set(50)  # Default value
    band_slider.pack(pady=5, fill="x")
    equalizer_sliders[band] = band_slider

# Run the application
root.mainloop()
