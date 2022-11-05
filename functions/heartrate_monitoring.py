from hardware.heartbeart_sensor import display_heartrate
from hardware.pi_operations import PiOperationsAccess
from functions.tts_operations import TTSOperationsAccess

from config.heartrate_config import heart_check_time, time_to_switch_off
from config.nix_tts import *


from time import sleep, time


class HeartRateMonitor:
    def __init__(self):
        self.initial_time = 0
        self.last_rate = 0
        self.timeout_begun = False
        self.check_timer = heart_check_time
        self.switch_off = time_to_switch_off

    def check_rate(self):
        while True:
            current_rate = display_heartrate

            if not self.timeout_begun:
                if current_rate == 0:
                    start_time = time()
                    self.timeout_begun = True
            else:
                if (time() - start_time < self.switch_off) and current_rate == 0:
                    TTSOperationsAccess.generate_tts(shutdown_text)
                    PiOperationsAccess.shutdown()
                else:
                    self.timeout_begun = False

            self.last_rate = current_rate

            sleep(0.01)


HeartRateMonitorAccess = HeartRateMonitor()
