from AaruXMusix.core.bot import AaruX
from AaruXMusix.core.dir import dirr
from AaruXMusix.core.git import git
from AaruXMusix.core.userbot import Userbot
from AaruXMusix.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = AaruX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
