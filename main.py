import threading
import config.submodule_dirs

import logging
import argparse

from functions.talk_control import TalkControllerAccess
from functions.heartrate_monitoring import HeartRateMonitorAccess
from functions.mission_processor_systems import MissionProcessorAccess

from events.event_queue import queue_adder
from config.event_types import TALK_SYSTEMS, INTRO_SPEECH

from config.parameters import logging_level, testing_mode


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Artificial Life')

    parser.add_argument('-l', '--log-level', action="store", dest="log_level", type=str, default=logging_level,
                        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'], help='Logging level')

    parser.add_argument('-t', '--test_mode', action="store_true", dest="test_mode", default=testing_mode,
                        help='Stops the system from shutting down when no more heartbeats are detected')

    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    logger = logging.getLogger("relic-cyberware-system")
    logger.setLevel(args.log_level)

    threading.Thread(target=HeartRateMonitorAccess.check_rate, args=(args.test_mode,), daemon=False).start()

    logger.info("Started Heart Rate Monitoring")

    # Start talk control as a thread
    threading.Thread(target=TalkControllerAccess.queue_checker, daemon=False).start()

    logger.info("Started Talk Controller")

    # # Welcome the user to the Relic System
    # queue_adder(TALK_SYSTEMS, INTRO_SPEECH, 1)

    # Start the mission parameteriser parameter getter as a thread
    threading.Thread(target=MissionProcessorAccess.objective_processor, daemon=False).start()

    threading.Thread(target=MissionProcessorAccess.standing_order_refresher, daemon=False).start()

    logger.info("Started Mission Processor")

