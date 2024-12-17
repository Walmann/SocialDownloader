import json


class profileClass():
    """
    ProfileDB = Profile Database
    profileName = Name of the profile
    """

    def __init__(self, profileDB, profileName):
        j = profileDB[profileName]
        self.name = profileName
        self.command = j["command"]
        self.link = j["link"]
        self.downloadLocation = j["downloadLocation"]

    pass