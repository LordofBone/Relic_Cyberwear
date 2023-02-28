import argparse
import logging

import config.submodule_dirs
from config.launch_config import logging_level, testing_mode
from config.nix_tts import boot_text, boot_text_test
from functions.talk_control import TalkControllerAccess

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Relic Cyberware System')

    parser.add_argument('-l', '--log-level', action="store", dest="log_level", type=str, default=logging_level,
                        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'], help='Logging level')

    parser.add_argument('-t', '--test_mode', action="store_true", dest="test_mode", default=testing_mode,
                        help='Stops the system from shutting down when no more heartbeats are detected and does not '
                             'loop')

    args = parser.parse_args()

    print("""
    NOTE 2! Along with the other message shown this code AND hardware should not be used for medical diagnosis. It's
    for fun/novelty use only, so bear that in mind while using it.
    Also bear in mind that ChatGPT will respond with the style of whatever context you have set within 
    config/chatgpt_config.py so I can't be sure what it will say. And I can't take any responsibility for any other 
    context that is set or what it says.
    """)

    logging.basicConfig(level=args.log_level)

    logger = logging.getLogger("relic-cyberware-system")
    logger.setLevel(args.log_level)

    logger.info("Initialising Relic Cyberware System, please stand by...")

    if not args.test_mode:

        while True:
            TalkControllerAccess.speak_tts(boot_text)
            TalkControllerAccess.listen_stt()
            TalkControllerAccess.command_checker()
            TalkControllerAccess.get_bot_engine_response()
            TalkControllerAccess.speak_tts_bot_response()

    else:
        TalkControllerAccess.speak_tts(boot_text_test)
        TalkControllerAccess.listen_stt()
        TalkControllerAccess.get_bot_engine_response()
        TalkControllerAccess.speak_tts_bot_response()
