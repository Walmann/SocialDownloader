import snapchat_dl
import time
import requests
import re


from dep.profileClass import profileClass

def profileDownload(profile: profileClass):
    
    profileSnapUsername = findUsername(profile.link)


    # profileSnapUsername = profile.link.strip("https://www.snapchat.com/add/").strip("http://www.snapchat.com/add/")
    download(profile=profileSnapUsername, downloadDirectory=profile.downloadLocation)
    pass

def download(profile, downloadDirectory):
    dl = snapchat_dl.SnapchatDL(directory_prefix=downloadDirectory)


    try:
        dl.download(str(profile))
    except requests.exceptions.ConnectionError as e: 
        print(f"ERROROR! But continue script! Error: {e}")
        pass
    except snapchat_dl.utils.APIResponseError as e:
        print(f"API Error! but continue. Error: {e}")
        pass
    except snapchat_dl.utils.NoStoriesFound:
        print("No stories from user. Continuing.")
        pass
    except snapchat_dl.utils.UserNotFoundError:
        print("User not found! Continuing")
        pass
    pass


def findUsername(lunk):
    # Regex for å finne brukernavn
    regex = r"https?://www\.snapchat\.com/add/([^/?]+)"

    
    match = re.search(regex, lunk)
    if match:
        brukernavn = match.group(1)
        return brukernavn
    else:
        raise ValueError(f"Fant ingen brukernavn i {lunk}")
        