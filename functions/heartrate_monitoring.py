from time import sleep, time

from config.heartrate_config import heart_check_time, time_to_switch_off
from config.nix_tts import *
from functions.tts_operations import TTSOperationsAccess
from hardware.heartbeart_sensor import bpm_setter
from hardware.pi_operations import PiOperationsAccess

import logging

logger = logging.getLogger("heartbeart-monitor-logger")


class HeartRateMonitor:
    def __init__(self):
        self.start_time = 0
        self.initial_time = 0
        self.last_rate = 0
        self.timeout_begun = False
        self.check_timer = heart_check_time
        self.switch_off = time_to_switch_off

    def check_rate(self, test_mode=False):
        while True:
            current_rate = bpm_setter.get_bpm()

            print(current_rate)

            if not self.timeout_begun:
                if current_rate == 0:
                    self.start_time = time()
                    self.timeout_begun = True
            else:
                if (time() - self.start_time < self.switch_off) and current_rate == 0:
                    if not test_mode:
                        TTSOperationsAccess.generate_tts(shutdown_text)
                        PiOperationsAccess.shutdown()
                    else:
                        logger.info("Shutdown would be initiated")
                else:
                    self.timeout_begun = False

            self.last_rate = current_rate

            sleep(0.01)


HeartRateMonitorAccess = HeartRateMonitor()
