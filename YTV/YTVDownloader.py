from pytube import YouTube
import os

active = "y"
while active == "y":
    
    link = YouTube(input("Enter the link: "))
    title = link.title
    
    print()
    print("Title:       ", link.title)
    print("Length:      ", link.length)
    print("Description: ", link.description)
    print()
    
    download = input("do you want to download? (y/n): ")
    
    if (download == "y"):
        print("Preparing to download the video")
        video = link.streams.get_highest_resolution()
        pathway = '/Users/christian/Downloads'
        if os.path.isdir(pathway):
            print('Download folder found')
            print('Download in progress...')
            video.download(pathway, title)
        else:
            print('Downloads folder not found, aborting download')
            break
        print("Download in progress...")
    elif (download == "n"):
        print("Download cancelled")
    else:
        print("Please select 'y' or 'n'")
    active = input("Another video? (y/n): ")
print("Goodbye")