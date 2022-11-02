import sys
import os

import logging

from config.nix_tts import *

from functions.tts_operations import TTSOperationsAccess
from functions.talk_control import TalkControllerAccess

soran_dir = os.path.join("soran")

sys.path.append(soran_dir)


if __name__ == "__main__":
    TTSOperationsAccess.generate_tts(boot_text)
    # from soran.main import main
    # main()
