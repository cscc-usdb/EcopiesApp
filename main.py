#by CSCC Club 2020
#to run this script you need to install pydrive library
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


class EcopiesApp:
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    NumberOfFolders = int(input("how many folders: "))
    for i in range(NumberOfFolders):
        folderName = input("name of folder: ")
        try:
            newFolder = drive.CreateFile({'title': folderName, 'mimeType': 'application/vnd.google-apps.folder'})
            newFolder.Upload()
        except:
            print("error error error")

