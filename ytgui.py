# from sre_parse import State
import tkinter
import customtkinter
import re
from ytdclass import Utb


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title('YTD')
app.geometry("400x240")
app.resizable(False, False)

url_entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Enter Youtube URL",
                               width=300,
                               height=25,
                               border_width=2,
                               corner_radius=10)
url_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkOptionMenu(master=app,
                                       values=["MP4", "MP3"],
                                       command=optionmenu_callback)
combobox.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
combobox.set("MP4")  # set initial value

# def bottom_lable():
#     label = customtkinter.CTkLabel(master=app, text=f"{yt.title()} Downloaded")
#     label.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
#     url_entry.delete(0,tkinter.END)


def dld_button():
    
    url = str(url_entry.get())
    yt_regex = r"http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?"

    if re.match(yt_regex, url):
        download_button.configure(state=tkinter.NORMAL) 
        if combobox.get() == "MP4":
            yt = Utb(url, "mp4")
            yt.download()
            label = customtkinter.CTkLabel(master=app, text=f"{yt.title()} Downloaded")
            label.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
            url_entry.delete(0,tkinter.END)
        else:
            print("it works")
            yt = Utb(url, "mp3")
            yt.download()
            label = customtkinter.CTkLabel(master=app, text=f"{yt.title()} Downloaded")
            label.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
            url_entry.delete(0,tkinter.END)
    else:
        label = customtkinter.CTkLabel(master=app, text="Error, Enter a Valid Link")
        label.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

   

download_button = customtkinter.CTkButton(master=app, text="Download", command=dld_button)
download_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# progress = customtkinter.CTkSlider(master=app, progress_color='#32a85a', width=250)
# progress.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

app.mainloop()



