# import snapchat_dl
import time
import requests
import json 
import argparse


from dep.profileClass import profileClass
from downloaders import snapchatDL
from downloaders import galleryDL



waitTimeAfterLoop = 120 # Wait time inseconds
waitTimeInsideLoop = 0 # Wait time inseconds
def download(fullDownload=False):
    firstLoopFinished = False
    
    currentLoop = 0
    fullDownloadEveryNLoop = 100

    _fullDownload = fullDownload
    while True:
        # Load jsonfile fresh every loop
        with open(downloadDBFile, "r") as dbFile:
            profileDB = json.load(dbFile)
        
        print("Loaded JSON Database")
        print("Current loop: " + str(currentLoop) + ", running full download after every " + str(fullDownloadEveryNLoop) + " loop. Current Fulldownload setting: " + str(_fullDownload))
        
        
        currentLoop = currentLoop + 1
        if currentLoop >= fullDownloadEveryNLoop:
            currentLoop = 0
            _fullDownload = True
        for profileKey in profileDB:

            # Load current profileClass
            profile = profileClass(profileDB= profileDB, profileName= profileKey)
            
            print(f"Downloading {profile.name}")
            if profile.command == "snapchat-dl":
                snapchatDL.profileDownload(profile)
            elif profile.command == "gallery-dl":
                if _fullDownload:
                    galleryDL.profileDownload(profile, fullDownload = True)
                    currentLoop = 0
                else: 
                    galleryDL.profileDownload(profile)
                
            
            
            if waitTimeInsideLoop > 0:
                print(f"Finished current user. Waiting for {waitTimeInsideLoop} seconds.")
                time.sleep(waitTimeInsideLoop)
        
        if waitTimeAfterLoop > 0 or firstLoopFinished == False:
            print(f"Finished loop. Waiting for {waitTimeAfterLoop} seconds.")
            time.sleep(waitTimeAfterLoop)
            firstLoopFinished = True
        
        
        _fullDownload = False
    pass






downloadDBFile = "./downloadDB.json"
if __name__ == "__main__":
    fullDownload = False


    parser = argparse.ArgumentParser(description="Et script som håndterer -f og --full som samme argument.")
    # Legg til argumentet -f / --full
    parser.add_argument(
        "-f", "--fullDownload",
        action="store_true",  # Angir at dette er en flagg-parameter
        help="Utfør en full Download første runde i scriptet."
    )




    try:
        f = open(downloadDBFile, "r")
        f.close()
    except FileNotFoundError:
        f = open(downloadDBFile, "w+")
        f.close()
    
    

    args = parser.parse_args()

    if args.fullDownload:
        fullDownload=True

    download(fullDownload=fullDownload)

