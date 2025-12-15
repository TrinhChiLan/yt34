import os.path
import yt_dlp
from tkinter import *
import tkinter.filedialog
import platform
from pathlib import Path
import opts

main = Tk()
main.title("yt34")
main.geometry("250x240")
main.resizable(False, False)
main.iconbitmap("y34.ico")

def create_message(message: str, color = "green", x=125, y=125):
    message = Message(main, text=message, fg=color, relief="raised", borderwidth=2, width=200)
    message.place(x=x, y=y, anchor="center")
    main.after(2000, message.destroy)

Label(main, text="YT34 Downloader", font=(None, 15, "bold"), bg="#373737", fg="white").place(x=125, y=0, anchor='n', width=250)

Label(main, text="Youtube Link: ", font=(None, 10, "bold")).place(x=25, y=50, anchor='w')
link_entry = Entry()
link_entry.place(x = 125, y=70, anchor='center', width=225)

Label(main, text="Format:", font=(None, 10, "bold")).place(x=25,y=100, anchor="w")
current_option = BooleanVar()
mp3_option = Radiobutton(main, text="mp3(audio)", variable=current_option,value=False)
mp3_option.place(x=75, y=120, anchor="center")
mp4_option = Radiobutton(main, text="mp4(video)", variable=current_option,value=True)
mp4_option.place(x=175, y=120, anchor="center")

Label(main, text="Download To:", font=(None, 10, "bold")).place(x=25, y=150, anchor="w")
target_dir_entry = Entry()
target_dir_entry.place(x=15, y=170, anchor='w', width=190)

dir_retrieve = Button(main, text="📁", command=lambda: retrieve_dir())
dir_retrieve.place(x=235, y=170, anchor='e')

download_button = Button(main, text="DOWNLOAD", bg='#27ae60',
                         fg='white', activebackground="#229954", cursor="hand2",
                         font=(None, 12), command=lambda: download())
download_button.place(x=125, y=210, anchor='center')

def download():
    download_opts = opts.mp4_opts if current_option.get() else opts.mp3_opts
    target_dir = target_dir_entry.get().strip()
    link = link_entry.get().strip()
    #
    if not link:
        create_message("Enter a link!", color="red")
        return
    #
    if not Path(target_dir).exists():
        create_message("Invalid directory!", "red")
        return
    #
    download_button.configure(state="disabled", text="DOWNLOADING...")
    main.update()
    #
    download_opts['outtmpl'] = os.path.join(target_dir, '%(title)s.%(ext)s')
    with yt_dlp.YoutubeDL(download_opts) as ydl:
        try:
            ydl.download([link])
            create_message("Download successful!")
        except Exception as e:
            print("Something went wrong!" + str(e))
            create_message("Download failed", "red")
        finally:
            download_button.configure(state="normal", text='DOWNLOAD')

def retrieve_dir():
    got_dir = tkinter.filedialog.askdirectory(title="Select Music Directory", initialdir=Path.home())
    if got_dir:
        target_dir_entry.delete(0, END)
        target_dir_entry.insert(0, got_dir)

if platform.system() == "Windows":
    target_dir_entry.insert(0, Path.home() / "Downloads")

main.mainloop()


