# import snapchat_dl
import time
import requests
import json 
import argparse
import configparser

from dep.profileClass import profileClass
from downloaders import snapchatDL
from downloaders import galleryDL
from dep.SettingsClass import Settings





def startScraping(fullDownload=False):
    firstLoopFinished = False
    currentLoop = 0
    _fullDownload = fullDownload
    
    while True:
        # Load jsonfile fresh every loop
        with open(settings.Files.downloadDbFile, "r") as dbFile:
            profileDB = json.load(dbFile)
        
        print("Loaded JSON Database")
        print("Current loop: " + str(currentLoop) + ", running full download after every " + str(settings.fullDownloadEveryNLoop) + " loop. Current Fulldownload setting: " + str(_fullDownload))
        
        
        currentLoop = currentLoop + 1
        if currentLoop >= settings.fullDownloadEveryNLoop:
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
                
            
            
            if settings.WaitTimes.insideLoop > 0:
                print(f"Finished current user. Waiting for {settings.WaitTimes.insideLoop} seconds.")
                time.sleep(settings.WaitTimes.insideLoop)
        
        if settings.WaitTimes.afterLoop > 0 or firstLoopFinished == False:
            print(f"Finished loop. Waiting for {settings.WaitTimes.afterLoop} seconds.")
            time.sleep(settings.WaitTimes.afterLoop)
            firstLoopFinished = True
        
        
        _fullDownload = False




settings = Settings()

if __name__ == "__main__":
    # fullDownload = False


    parser = argparse.ArgumentParser(description="Et script som håndterer -f og --fullDownload som samme argument.")
    # Legg til argumentet -f / --fullDownload
    parser.add_argument(
        "-f", "--fullDownload",
        action="store_false",  # Angir at dette er en flagg-parameter
        help="Utfør en full Download første runde i scriptet."
    )

    args = parser.parse_args()


    try:
        f = open(settings.Files.downloadDbFile, "r")
        f.close()
    except FileNotFoundError:
        f = open(settings.Files.downloadDbFile, "w+")
        f.close()
    
    # if args.fullDownload:
    #     fullDownload=True

    startScraping(fullDownload=args.fullDownload)

