from pytube import YouTube
import os

class Utb:
    def __init__(self, url, extension : str) -> None:
        self.url = url
        self.extension = extension
        self.path = None
        self.yt = YouTube(self.url)

    
    def set_path(self, new_path):
        self.path = new_path

    def title(self):
        return self.yt.title

    def views(self):
        return self.yt.views 
        

    def download(self): #pass in mp4 or mp3
        yt = self.yt
        self.path = './'

        if self.extension == "mp4":
            ys = yt.streams.get_highest_resolution()
            print("Downloading...")
            ys.download()
            print(f"{self.yt.title} -- Download completed!!")
        elif self.extension == "mp3":
            mp3d = yt.streams.filter(only_audio=True).first().download(output_path =os.chdir(self.path))
            base, ext = os.path.splitext(mp3d)
            new_file = base + '.mp3'
            os.rename(mp3d, new_file)
            print(f"{self.yt.title} -- Downloaded Completed!!")
        else:
            print("Invalid File Extension")