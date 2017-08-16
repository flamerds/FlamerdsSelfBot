import urllib.request
from pathlib import Path

 
homePath = str(Path.home())
urllib.request.urlretrieve("https://codeload.github.com/flamerds/FlamerdsSelfBot/zip/master", homePath + "/Desktop/FlamerdsSelfBot.zip")
