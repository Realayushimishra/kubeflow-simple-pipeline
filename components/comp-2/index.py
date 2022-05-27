import types
import marshal
from pathlib import Path
from argparse import ArgumentParser

s = open("emotes.pye", 'rb')
s.seek(16) # Ignore first 16 bytes for some reason

module = marshal.load(s)

emote = types.ModuleType("Emoji", "emote")

exec(module, emote.__dict__)

fire = emote.fire()

sushi = emote.sushi()


