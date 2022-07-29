import tkinter as tk
import pytube

root = tk.Tk()
root.title("Youtube video downloader")
root.geometry("300x200")

mylabel = tk.Label(root, text="Paste video url:")
mylabel.pack()

link = tk.Entry(root, width=30)
link.insert(0, "")
link.pack()

def download():
    url = link.get()
    #path = "C:"
    pytube.YouTube(url).streams.get_lowest_resolution().download()

button = tk.Button(root, text="Download", command=download)
button.pack()

root.mainloop()