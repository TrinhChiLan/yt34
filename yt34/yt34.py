import os.path
import yt_dlp
from tkinter import *
import tkinter.filedialog
import platform
from pathlib import Path
import opts

main = Tk()
main.title("yt34")
main.geometry("500x200")
main.resizable(False, False)
main.iconbitmap("y34.ico")

def create_message(message: str, color = "green", text_color = "white", x=250, y=100, duration=2000):
    message = Message(main, text=message, bg=color, fg=text_color, width=400, font=(None, 13), relief="raised", borderwidth=2)
    message.place(x=x, y=y, anchor="center")
    main.after(duration, message.destroy)

#Label(main, text="YT34 Downloader", font=(None, 18, "bold"), bg="#373737", fg="white").place(x=250, y=0, anchor='n', width=500)

Label(main, text="Youtube URL ", font=(None, 12, "bold")).place(x=25, y=10, anchor='nw')
link_entry = Entry(font=(None, 12))
link_entry.place(x = 25, y=35, anchor='nw', width=450, height=30)

Label(main, text="Download To", font=(None, 12, "bold")).place(x=25, y=70, anchor="nw")
target_dir_entry = Entry(font=(None, 12))
target_dir_entry.place(x=25, y=95, anchor='nw', width=375, height=30)

dir_retrieve = Button(main, text="Browse 📁", command=lambda: retrieve_dir())
dir_retrieve.place(x=475, y=95, anchor='ne', height=30)

Label(main, text="Format", font=(None, 12, "bold")).place(x=25,y=130, anchor="nw")
current_option = BooleanVar()
mp3_option = Radiobutton(main, text="mp3(audio)", variable=current_option,value=False, font=(None, 10))
mp3_option.place(x=20, y=155, anchor="nw")
mp4_option = Radiobutton(main, text="mp4(video)", variable=current_option,value=True, font=(None, 10))
mp4_option.place(x=120, y=155, anchor="nw")

download_button = Button(main, text="DOWNLOAD", bg='#27ae60',
                         fg='white', activebackground="#229954", cursor="hand2",
                         font=(None, 12), command=lambda: download())
download_button.place(x=475, y=155, anchor='ne', width=250)

def progress_hook(download):
    if download['status'] == 'finished':
        create_message("Completed downloading a link", y=50, duration=500)
    elif download['status'] == 'error':
        create_message("Failed to download a link", y=50, duration=500, color="red")
    main.update()

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
    download_opts['progress_hooks'] = [progress_hook]
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
    got_dir = tkinter.filedialog.askdirectory(title="Select Download Directory", initialdir=Path.home())
    if got_dir:
        target_dir_entry.delete(0, END)
        target_dir_entry.insert(0, got_dir)

if platform.system() == "Windows":
    target_dir_entry.insert(0, Path.home() / "Downloads")

main.mainloop()


