import threading
import config.submodule_dirs

import logging

from functions.talk_control import TalkControllerAccess
from functions.heartrate_monitoring import HeartRateMonitorAccess

from events.event_queue import queue_adder
from events.event_types import TALK_SYSTEMS, INTRO_SPEECH

logger = logging.getLogger("relic-cyberwear-system")

threading.Thread(target=TalkControllerAccess.queue_checker, daemon=False).start()


if __name__ == "__main__":
    threading.Thread(target=HeartRateMonitorAccess.check_rate, daemon=False).start()

    logger.info("Started Input Checking")

    # Start talk control as a thread
    threading.Thread(target=TalkControllerAccess.queue_checker, daemon=False).start()

    logger.info("Started Talk Controller")

    # Welcome the user to the Relic System
    queue_adder(TALK_SYSTEMS, INTRO_SPEECH, 1)
