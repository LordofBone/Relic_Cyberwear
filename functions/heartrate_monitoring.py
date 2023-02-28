import logging

from hardware.heartbeart_sensor import SensorOperationsAccess

logging.basicConfig()
logger = logging.getLogger(__name__)


class HeartRateMonitor:
    def __init__(self):
        self.start_time = 0
        self.initial_time = 0
        self.last_rate = 0
        self.timeout_begun = False

    def get_rate(self):
        """
        This function returns the current heart rate.
        :return:
        """
        return SensorOperationsAccess.bpm_setter.get_bpm()


HeartRateMonitorAccess = HeartRateMonitor()
