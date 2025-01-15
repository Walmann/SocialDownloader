import configparser

class _waitTimes():
    def __init__(self, settings):
        self.afterLoop = settings["Settings"]["waitTimeAfterLoop"]
        self.insideLoop = settings["Settings"]["waitTimeInsideLoop"]

class _files():
    def __init__(self, settings):
        self.downloadDbFile = settings["Files"]["downloadDBFile"]

class Settings():
    def __init__(self):

        # Load Settings
        _settings = configparser.ConfigParser().read("./settings.ini")


        self.WaitTimes = _waitTimes(settings=_settings) # type: _waitTimes
        self.Files = _files(settings=_settings) # type: _files

        self.fullDownloadEveryNLoop = _settings["Settings"]["fullDownloadEveryNLoop"]