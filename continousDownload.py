# import snapchat_dl
import time
import requests
import json 

from dep.profileClass import profileClass
from downloaders import snapchatDL
from downloaders import galleryDL



waitTimeAfterLoop = 120 # Wait time inseconds
waitTimeInsideLoop = 0 # Wait time inseconds
def download():
    firstLoopFinished = False
    

    while True:
        # Load jsonfile fresh every loop
        with open(downloadDBFile, "r") as dbFile:
            profileDB = json.load(dbFile)
        
        for profileKey in profileDB:

            # Load current profileClass
            profile = profileClass(profileDB= profileDB, profileName= profileKey)
            
            print(f"Downloading {profile.name}")
            if profile.command == "snapchat-dl":
                snapchatDL.profileDownload(profile)
            elif profile.command == "gallery-dl":
                galleryDL.profileDownload(profile)
                
            
            
            if waitTimeInsideLoop > 0:
                print(f"Finished current user. Waiting for {waitTimeInsideLoop} seconds.")
                time.sleep(waitTimeInsideLoop)
        if waitTimeAfterLoop > 0 or firstLoopFinished == False:
            print(f"Finished loop. Waiting for {waitTimeAfterLoop} seconds.")
            time.sleep(waitTimeAfterLoop)
            firstLoopFinished = True
    pass






downloadDBFile = "./downloadDBDEV.json"
if __name__ == "__main__":
    try:
        f = open(downloadDBFile, "r")
        f.close()
    except FileNotFoundError:
        f = open(downloadDBFile, "w+")
        f.close()
    download()
