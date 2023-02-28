from time import sleep, time

from config.heartrate_config import heart_check_time, time_to_switch_off
from config.nix_tts import *
from functions.tts_operations import TTSOperationsAccess
from hardware.heartbeart_sensor import SensorOperationsAccess
from hardware.pi_operations import PiOperationsAccess
from events.event_queue import queue_adder
from config.event_types import LISTEN_STT, TALK_SYSTEMS
import threading
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)


class HeartRateMonitor:
    def __init__(self):
        self.start_time = 0
        self.initial_time = 0
        self.last_rate = 0
        self.timeout_begun = False
        self.check_timer = heart_check_time
        self.switch_off = time_to_switch_off * 60
        threading.Thread(target=SensorOperationsAccess.bpm_handler, daemon=False).start()

    def get_rate(self):
        return self.last_rate

    def check_rate(self, test_mode=False):
        """
        This function will check the bpm and if it is 0 for a certain amount of time it will shut down the system
        :param test_mode:
        :return:
        """
        while True:
            current_rate = SensorOperationsAccess.bpm_setter.get_bpm()

            logger.debug(f"Heart Rate: {current_rate}")
            logger.debug(f"Timer begun: {self.timeout_begun}")

            if not self.timeout_begun:
                if current_rate == 0:
                    self.start_time = time()
                    self.timeout_begun = True
                elif current_rate == -1:
                    queue_adder(TALK_SYSTEMS, LISTEN_STT, 2)
                else:
                    queue_adder(TALK_SYSTEMS, LISTEN_STT, 2)
            else:
                if (time() - self.start_time > self.switch_off) and current_rate == 0:
                    logger.debug(f'No heart beat detected for {time() - self.start_time} seconds')
                    TTSOperationsAccess.generate_tts(shutdown_text)
                    if not test_mode:
                        PiOperationsAccess.shutdown()
                    else:
                        logger.debug("Shutdown would be initiated")
                elif current_rate > 0:
                    self.timeout_begun = False

                logger.debug(f"{time() - self.start_time}")

            self.last_rate = current_rate

            sleep(5)


HeartRateMonitorAccess = HeartRateMonitor()
