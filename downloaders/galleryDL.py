import gallery_dl
import time
import requests

from dep.profileClass import profileClass

# class UrlJob(Job):

#     def __init__(self, url, parent=None):
#         Job.__init__(self, url, parent)
#         self.urls = []

#     def handle_url(self, url, _):
#         self.urls.append(url)



def profileDownload(profile: profileClass):
    download(profile=profile, downloadDirectory=profile.downloadLocation)
    pass

def download(profile:profileClass, downloadDirectory):
    gConfig = gallery_dl.config

    gConfig.load()

    gallery_dl.config.set(('extractor',), "base-directory", downloadDirectory)
    gallery_dl.config.set(("extractor",), "directory", ["{subcategory}"])
    gallery_dl.config.set(('extractor'), "filename", "{date:%Y-%m-%d} - {title[:50]} {id}{num:?_//}.{extension}")
    gallery_dl.config.set(('extractor', "instagram"), "cursor", True)
    gallery_dl.config.set(('extractor', "instagram"), "include",  "tagged,reels,highlights,info,avatar,posts") #"stories,tagged,reels,highlights,info,avatar,posts"

    try:        
        gallery_dl.job.DownloadJob(profile.link).run()
        print("Download Finished!")
    except Exception as e: 
        print("Error!")
        print(str(e))
    pass
