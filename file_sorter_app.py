import os 
import shutil as sh
from pathlib import Path


class sorter():
    def __init__(self, link):
        """ 
        Test the entry for validity
        Dowload file by default
        Y/N message box before starting
        """
        self.link = link
        self.folder = ['Excel', 'Images', 'Apps', 'Videos', 'Music', 'Text_docs', 'Presentations']
        self.ext = {
           'Text_docs': ('.pdf', '.docx', '.txt', '.odt', '.doc', '.docm', '.pdf'),
           'Presentations' : ('.pub', '.pptx', '.rtf'),
           'Excel': ('.xlsx', '.xlsm', '.xls', '.csv', '.sql'), 
           'Apps': ('.exe', '.kml', '.zip', '.nex', '.whl'),
           'Images': ('.jpg', '.gif', '.png', '.pdn'), 
           'Videos': ('.mkv', '.mp4', ".avi"), 
           'Music': (".mp3")
           }

        if self.link == "":
            exit()
        if self.link == "a":
            self.link = str(os.path.join(Path.home(), "Downloads"))
            #if input("Lancer le l'application dans le fichier 'Téléchargements' ? (y:1/n:0) : "):
            if 3>2:
                os.chdir(self.link)
                self.dir_list = os.listdir(self.link)
                self.main_loop()
        else:
            try:
                os.chdir(self.link)
            except OSError:
                print("Folder not found")
                exit()
    
            self.dir_list = os.listdir(self.link)
            self.main_loop()

    def main_loop(self):
        """
        Base loop and extension dictionnaries
        """
        for fich in self.dir_list:
            source = os.path.join(self.link, fich)
            if os.path.isfile(source):
                try:
                    self.sort(fich, source)
                except FileNotFoundError:
                    print("Issue with the copy of : " + fich)
                    pass
            else:
                pass

    def sort(self, file, source):
        """
        Extract extension and put files in correct folder
        If extension not found, create an "Other" folder
        """
        for z in self.folder:
            if os.path.splitext(file)[1] in self.ext[z]:
                self.new_folder(z)
                sh.move(source, os.path.join(self.link, z, file))
        if os.path.exists(os.path.join(self.link, file)):
            self.new_folder('Others')
            sh.move(source, os.path.join(self.link, "Others", file))
            print(f"{file} couldn't be sorted and will be placed in the 'Others' folder ")



    def new_folder(self, name):
        """
        Create the folders for sorting only if they don't exist already
        """
        if not os.path.exists(os.path.join(self.link, name)):
            try:
                os.mkdir(os.path.join(self.link, name))
                print(f"Creating folder " + name)
            except OSError:
                print(f"Folder's {name} creation failed")
                pass


if __name__ == '__main__':
    #link = input("Enter the folder's adress (download folder by default, x to leave) : ")
    act = sorter("a")