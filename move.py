import os 
import shutil 
folder = input("Enter a file path: ")
if folder == "":
    print ("please type in your file path")
    exit()
else:
    files = os.listdir(folder)
    photo = 0
    music = 0
    videos = 0
    Documents = 0
    Archives = 0
    Di = 0
    ap = 0
    programs = 0
    wf = 0
    Excel = 0
    pp = 0
    pf = 0



    for file in files:
        sources = os.path.join(folder, file)
    #----musics----
        if file.endswith((".mp3", ".m4a", ".wav", ".acc", "flac", ".ogg", ".wma")):
            if not os.path.exists(os.path.join(folder, "Music")):
                os.mkdir(os.path.join(folder, "Music"))
            shutil.move(sources, os.path.join(folder, "Music"))
            music +=1
        elif file.endswith((".mp4", ".mkv", ".lrc", ".mov", ".wmv", ".flv", "webm", "mpeg", "3gp")):
            if not os.path.exists(os.path.join(folder, "Videos")):
                os.mkdir(os.path.join(folder, "Videos"))
            shutil.move(sources, os.path.join(folder, "Videos"))
            videos +=1
    
        #----photos----
        elif file.endswith((".png", ".jpeg", ".jpg", ".gif", ".bmp", ".webp", ".svg", ".tiff", ".ico")):
            if not os.path.exists(os.path.join(folder, "Photos")):
                os.mkdir(os.path.join(folder, "Photos"))
            shutil.move(sources, os.path.join(folder, "Photos"))
            photo +=1

        #-----archives------
        elif file.endswith(( ".zip", ".rar", ".7z", ".tar", ".gz")):
            if not os.path.exists(os.path.join(folder, "Archives")):
                os.mkdir(os.path.join(folder, "Archives"))
            shutil.move(sources, os.path.join(folder, "Archives"))
            Archives +=1

    #----Documents-----
        elif file.endswith(( ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt")):
            if not os.path.exists(os.path.join(folder, "Documents")):
                os.mkdir(os.path.join(folder, "Documents"))
            shutil.move(sources, os.path.join(folder, "Documents"))
            Documents +=1
    
    #----Excel-----
        elif file.endswith((".csv", ".slsx", ".xls")):
            if not os.path.exists(os.path.join(folder, "Excel")):
                os.mkdir(os.path.join(folder, "Excel"))
            shutil.move(sources, os.path.join(folder, "Excel"))
            Excel +=1
    #----power_point----
        elif file.endswith(("pptx", "ppt")):
            if not os.path.exists(os.path.join(folder, "Power_point")):
                os.mkdir(os.path.join(folder, "Power_point"))
            shutil.move(sources, os.path.join(folder, "Power_point"))
            pp +=1
    #----python_files----
        elif file.endswith((".pyw", ".py")):
            if not os.path.exists(os.path.join(folder, "Python_files")):
                os.mkdir(os.path.join(folder, "Python_files"))
            shutil.move(sources, os.path.join(folder, "Python_files"))
            pf +=1
    #----android----
        elif file.endswith(".apk"):
            if not os.path.exists(os.path.join(folder, "Android_app")):
                os.mkdir(os.path.join(folder, "Android_app"))
            shutil.move(sources, os.path.join(folder, "Android_app"))
            ap +=1
    #----disk images----
        elif file.endswith(".iso"):
            if not os.path.exists(os.path.join(folder, "Disk_images")):
                os.mkdir(os.path.join(folder, "Disk_images"))
            shutil.move(sources, os.path.join(folder, "Disk_images"))
            Di +=1
    #-----web files-----
        elif file.endswith(( ".html", ".css", "js", "json", "xml")):
            if not os.path.exists(os.path.join(folder, "web_file")):
                os.mkdir(os.path.join(folder, "web_file"))
            shutil.move(sources, os.path.join(folder, "web_file"))
            wf +=1
    #-----programs-----
        elif file.endswith((".exe", ".msl")):
            if not os.path.exists(os.path.join(folder, "Programs")):
                os.mkdir(os.path.join(folder, "Programs"))
            shutil.move(sources, os.path.join(folder, "Programs"))
            programs+=1
       
total = photo + music + videos + Archives + ap + Di + programs + Documents + pf + pp + wf + Excel
print (f"Moved {photo} to photos") 
print (f"Moved {videos} to videos") 
print (f"Moved {music} to musics") 
print (f"Moved {Archives} to Archives")
print (f"Moved {Documents} to Documents")
print (f"Moved {pf} to Python_files")
print (f"Moved {wf} to Web_files")
print (f"Moved {Di} to Disk_images")
print (f"Moved {programs} to programs")
print (f"Moved {ap} to Android_apps")
print (f"Moved {pp} to Power_points")
print (f"Moved {Excel} to Excel")
print (f"total: {total}")

print ("Done!")
