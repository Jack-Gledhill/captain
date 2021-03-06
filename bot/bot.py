from core import Core, version_info
from yaml import safe_load

VERSION = version_info(
	name="captain",
	major=3,
	minor=3,
	patch=0,
	release="stable"
)

class PatchedCore(Core):
	actions = None
	emojis = None

bot = PatchedCore()

bot.actions = bot.config.get("actions", {})
bot.emojis = bot.config.get("emojis", {})

bot.log.info("Running {0.name} v{0.major}.{0.minor}.{0.patch}-{0.release}".format(VERSION))
bot.boot()