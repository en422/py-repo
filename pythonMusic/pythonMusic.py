import os
from tkinter import Button, StringVar, Label, LabelFrame, GROOVE, DoubleVar, Scale, Scrollbar, VERTICAL, \
    Listbox, SINGLE, RIGHT, BOTH, Y, END, ACTIVE, Tk
from tkinter import filedialog, messagebox
import pygame


class MusicPlayer(object):
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("MusicPlayer")
        # Window Geometry
        self.root.geometry("1100x200")
        # Initiating Pygame

        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()

        # Creating the Track Frames for Song label & status label
        track_frame = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="Navy blue",
                                 fg="white", bd=5, relief=GROOVE)
        track_frame.place(x=0, y=0, width=800, height=100)
        # Inserting Song Track Label
        song_track = Label(track_frame, textvariable=self.track, width=20, font=("times new roman", 24, "bold"),
                           bg="Orange", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Inserting Status Label
        track_status = Label(track_frame, textvariable=self.status, font=("times new roman", 24, "bold"), bg="orange",
                             fg="gold").grid(row=0, column=1, padx=10, pady=5)

        # Creating Button Frame
        button_frame = LabelFrame(self.root, text="Control Panel", font=("times new roman", 12, "bold"), bg="grey",
                                  fg="white", bd=2, relief=GROOVE)
        button_frame.place(x=0, y=100, width=615, height=100)

        # Inserting Pause Button
        play_btn = Button(button_frame, text="PAUSE", command=self.pause_song, width=8, height=1,
                          font=("times new roman", 12, "bold"), fg="navy blue", bg="pink").grid(row=0, column=1, padx=10
                                                                                                , pady=5)
        # Inserting play Button
        play_btn = Button(button_frame, text="PLAY", command=self.play_song, width=8, height=1,
                          font=("times new roman", 12, "bold"), fg="navy blue", bg="pink").grid(row=0, column=2, padx=10
                                                                                                , pady=5)
        # Inserting Stop Button
        play_btn = Button(button_frame, text="STOP", command=self.stop_song, width=8, height=1,
                          font=("times new roman", 12, "bold"), fg="navy blue", bg="pink").grid(row=0, column=3, padx=10
                                                                                                , pady=5)

        # Inserting Volume Frame
        slider_frame = LabelFrame(self.root, font=("times new roman", 15, "bold"), bg="grey",
                                  fg="white", bd=2, relief=GROOVE)
        slider_frame.place(x=615, y=100, width=100, height=100)
        # Inserting Volume Slider
        self.var = DoubleVar()
        slider = Scale(slider_frame, from_=100, to=0, variable=self.var, orient=VERTICAL, length=180)
        slider.pack()
        # Inserting Set Volume Button
        vol_btn = Button(button_frame, text="Set Volume", command=self.volume_set, width=10, height=1,
                         font=("times new roman", 12, "bold"), fg="green", bg="pink").grid(row=0, column=5, padx=10,
                                                                                           pady=0)
        # INSERTING FILE BROWSING BUTTON
        button_explore = Button(button_frame, text="Browse", command=self.browse_files, width=8, height=1,
                                font=("times new roman", 12, "bold"), fg="blue", bg="pink").grid(row=0, column=6,
                                                                                                 padx=10, pady=5)

        # Creating Playlist Frame
        songs_frame = LabelFrame(self.root, text="Song Playlist", font=("times new roman", 15, "bold"), bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        songs_frame.place(x=700, y=0, width=400, height=200)
        # Inserting scrollbar
        scroll_y = Scrollbar(songs_frame, orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songs_frame, yscrollcommand=scroll_y.set, selectbackground="gold", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"), bg="silver", fg="navy blue", bd=5, relief=GROOVE)
        # Applying Scrollbar to listbox
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs

    def play_song(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()
        # It will Display the  Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()

    def stop_song(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

    def pause_song(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()

    def volume_set(self):
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
        volume = self.var.get()
        pygame.mixer.music.set_volume(volume)

    def browse_files(self):
        i = 0
        filename = filedialog.askopenfilename(initialdir="/", title="Select a File", multiple=True)
        try:
            f = open("C:\\Users\\hp\\Desktop\\songs\\music.txt", "a+")
        except FileNotFoundError:
            f =
        while i <= len(filename)-1:
            f.write(filename[i].replace("/", "\\"))
            i += 1
        f.close()
        f = open("C:\\Users\\hp\\Desktop\\songs\\music.txt", "r")
        # Inserting Songs into Playlist
        for track in f:
            os.chdir(track)
            os.listdir(track)
            self.playlist.insert(END, track)


root = Tk()
MusicPlayer(root)
root.mainloop()
