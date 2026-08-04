import os
import shutil
import time
while True:
    try:
        folder = input("Enter a File Path (e  to exit): ").lower()
        if folder == "e":
            print("Bye")
            break
        files = os.listdir(folder)
        music = 0
        videos = 0
        doc = 0
        programs = 0
        apk = 0
        excel = 0
        pyfile = 0
        webfiles = 0
        non_ext = 0
        photos =0

        counters={
            "music": 1,
            "videos": 1,
            "photo": 1,
            "doc": 1,
            "programs":1,
            "pyfile": 1,
            "webfile": 1,
            "apk": 1,
            "excel": 1,
            "Non-ext": 1
        }
        for file in files:
            source = os.path.join(folder, file)
            if os.path.isdir(source):
                continue
            name, ext = os.path.splitext(file)
            #Videos
            if file.endswith((".mp4", ".mkv", ".lrc", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".3gp", ".pls")):
                if not os.path.exists(os.path.join(folder, "Videos")):
                    os.mkdir(os.path.join(folder, "Videos"))
                new = f"Videos-{counters["videos"]}-{ext}"
                shutil.move(source, os.path.join(folder, "Videos", new))
                videos+=1
                counters["videos"]+=1
            #music
            elif file.endswith((".mp3", ".m4a", ".wav", ".acc", "flac", ".ogg", ".wma")):
                if not os.path.exists(os.path.join(folder, "Music")):
                    os.mkdir(os.path.join(folder, "Music"))
                new = f"Music-{counters['music']}-{ext}"
                shutil.move(source, os.path.join(folder, "Music"))
                music+=1
                counters["music"]+=1
            #Photo
            elif file.endswith((".png", ".jpeg", ".jpg", ".gif", ".bmp", ".webp", ".svg", ".tiff", ".ico")):
                if not os.path.exists(os.path.join(folder, "Photos")):
                    os.mkdir(os.path.join(folder, "Photos"))
                new = f"Photos-{counters['photo']}-{ext}"
                shutil.move(source, os.path.join(folder, "Photos", new))
                photos +=1
                counters["photo"]+=1
            #Pyfiles
            elif file.endswith((".png", ".jpeg", ".jpg", ".gif", ".bmp", ".webp", ".svg", ".tiff", ".ico")):
                if not os.path.exists(os.path.join(folder, "Projects.py")):
                    os.mkdir(os.path.join(folder, "Projects.py"))
                new = f"Py_files-{counters['pyfiles']}-{ext}"
                shutil.move(source, os.path.join(folder, "Projects.py", new))
                pyfile +=1
                counters["pyfile"]+=1
            #Documents
            elif file.endswith((".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt")):
                if not os.path.exists(os.path.join(folder, "Documents")):
                    os.mkdir(os.path.join(folder, "Documents"))
                new = f"Documents-{counters['doc']}-{ext}"
                shutil.move(source, os.path.join(folder, "Documents", new))
                doc +=1
                counters[doc]+=1
            #Excel
            elif file.endswith((".xls", "csv", "xlsx")):
                if not os.path.exists(os.path.join(folder, "Excel")):
                    os.mkdir(os.path.join(folder, "Excel"))
                new = f"Excel-{counters['excel']}-{ext}"
                shutil.move(source, os.path.join(folder, "Excel", new))
                excel +=1
                counters['excel']+=1
            #apk
            elif file.endswith(".apk"):
                if not os.path.exists(os.path.join(folder, "Apks")):
                    os.mkdir(folder, "Apks")
                new = f"Apks-{counters['doc']}-{ext}"
                shutil.move(source, os.path.join(folder, "Documents", new))
                apk +=1
                counters["apk"]+=1
            #programs
            elif file.endswith((".exe", "msl")):
                if not os.path.exists(os.path.join(folder, "Programs")):
                    os.mkdir(os.path.join(folder, "Programs"))
                new = f"Programs-{counters['doc']}-{ext}"
                shutil.move(source, os.path.join(folder, "Programs", new))
                programs +=1
                counters['programs']+=1
            #Webfiles
            elif file.endswith((".html", ".css", ".js", ".json", ".xml")):
                        if not os.path.exists(os.path.join(folder, "Web-files")):
                            os.mkdir(folder, "Web-files")
                        new = f"{counters['webfile']}-{ext}"
                        shutil.move(source, os.path.join(folder, "Web-files", new))
                        webfiles+=1
                        counters["webfile"]+=1
            else:
                if ext == "":
                    if not os.path.exists(os.path.join(folder, "Non-extension")):
                        os.mkdir(os.path.join(folder, "Non-extension"))
                    new = f"Non-extension{counters["Non-ext"]}"
                    shutil.move(source, os.path.join(folder, "Non-extension", new))
                    counters["Non-ext"]+=1
                    non_ext +=1
    except FileExistsError:
        print (f"{file} Already Found")
    except shutil.Error:
        print (f"{file} already exists skipped")
    except FileNotFoundError:
        print(f"Cannot Locate {folder}. check if the folder was type in correctly")
        continue

    total = programs + excel + pyfile + apk + music + videos + webfiles + doc + non_ext + photos
    print(f"apk >>> {apk}")
    print("-_" * 24)
    time.sleep(0.4)
    print(f"Excel >>> {excel}")
    print("-_" * 24)
    time.sleep(0.4)
    print(f"Photos >>> {photos}")
    print("-_" * 24)
    time.sleep(0.4)
    print(f"Programs >>> {programs}")
    print("-_" * 24)
    time.sleep(0.4)
    print(f"Webfile >>> {webfiles}")
    print("-_" * 24)
    time.sleep(0.4)
    print(f"Pyfiles >>> {pyfile}")
    print("-_" * 24)
    time.sleep(0.4)
    print(f"Musics >>> {music}")
    print("-_" * 24)
    time.sleep(0.4)
    print(f"Videos >>> {videos}")
    print("-_" * 24)
    time.sleep(0.4)
    print(f"Documents >>> {doc}")
    print("-_" * 24)
    time.sleep(0.4)
    print(f"Files with Non-extension >>> {non_ext}")
    print("-_" * 24)
    time.sleep(2)
    print("\n")
    print("-_" * 24)
    print (f"Total: {total} Files Moved")
    if total == 0:
        print (f"No file was Moved in '{folder}'. check if the folder contains any files")
    

