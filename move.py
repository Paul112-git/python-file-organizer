import os 
import time
import shutil
while True:
    try:
        folder = input("Enter a file path: ").lower()
        if folder == "":
            print ("Please type in your file path")
            exit()
        else:
            files = os.listdir(folder)
            photo = 0
            music = 0
            videos = 0
            Documents = 0
            Archives = 0
            Di = 0
            programs = 0
            ap = 0
            pp = 0
            Excel = 0
            wf = 0
            pf = 0  
            skipped = 0
            for file in files:
                sources = os.path.join(folder, file)
    #----musics----
                if file.endswith((".mp3", ".m4a", ".wav", ".acc", "flac", ".ogg", ".wma")):
                    if not os.path.exists(os.path.join(folder, "Music")):
                         os.mkdir(os.path.join(folder, "Music"))
                    shutil.move(sources, os.path.join(folder, "Music"))
                    music +=1
    #----videos-----
                elif file.endswith((".mp4", ".mkv", ".lrc", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".3gp", ".pls")):
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
                elif file.endswith(( ".pyw", ".py")):
                    if not os.path.exists(os.path.join(folder, "Python_files")):
                        os.mkdir(os.path.join(folder, "Python_files"))
                    shutil.move(sources, os.path.join(folder, "Python_files"))
                    pf +=1
    #----android----
                elif file.endswith(( ".apk")):
                    if not os.path.exists(os.path.join(folder, "Android_apps")):
                        os.mkdir(os.path.join(folder, "Android_apps"))
                    shutil.move(sources, os.path.join(folder, "Android_apps"))
                    ap +=1
    #----disk images----
                elif file.endswith(( ".iso")):
                    if not os.path.exists(os.path.join(folder, "Disk_images")):
                        os.mkdir(os.path.join(folder, "Disk_images"))
                    shutil.move(sources, os.path.join(folder, "Disk_images"))
                    Di +=1
    #-----web files-----
                elif file.endswith(( ".html", ".css", ".js", ".json", ".xml")):
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
    except FileNotFoundError:
        print(f"'{folder}' Not Found!")
        exit()
    except shutil.Error:
        print (f"{file} Already exists in  a folder Skipping.....")
        time.sleep(1)
        skipped +=1
       
    total = photo + music + videos + Archives + ap + Di + programs + Documents + pf + pp + wf + Excel
    skip = skipped
    print (f"Photos: ({photo})")
    time.sleep(0.1) 
    print (f"Videos: ({videos})")
    time.sleep(0.1)  
    print (f"Musics: ({music})")
    time.sleep(0.1) 
    print (f"Archives: ({Archives})")
    time.sleep(0.1) 
    print (f"Photos: ({photo})")
    time.sleep(0.1) 
    print (f"Excel: ({Excel})")
    time.sleep(0.1)
    print (f"Python_Files: ({pf})")
    time.sleep(0.1) 
    print (f"Androids: ({ap})")
    time.sleep(0.1) 
    print (f"Programs: ({programs})")
    time.sleep(0.1) 
    print (f"Web_Files: ({wf})")
    time.sleep(0.1) 
    print (f"Dcouments: ({Documents})")
    time.sleep(0.1)  
    print (f"Power_Point: ({pp})")
    time.sleep(0.1) 
    print (f"Disk_images: ({Di})")
    time.sleep(0.1)
    print (f"Skipped:({skipped})")
    time.sleep(1) 
    print ("Total Moved:", (total) )
    print (f"Total Skipped: ({skip})")
    print (skip, "File Skipped")
    if total == 0:
        print (f"No File Was Found In '({folder})'")
    print (total, f"File organized! \nLocation: ({folder})\n")

    ask = input("Organize Another File (y/n): ").lower()

    if ask == "y":
        continue

    elif ask == "n":
         print ("Bye!")
         break
    else:
        print ("invalid input")
