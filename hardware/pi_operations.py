import logging
from subprocess import call
from time import sleep

logger = logging.getLogger("pi-operations")


class PiOperations:
    def __init__(self):
        # todo: add extra raspberry pi operations here, temp checks etc.
        self.shutdown_wait_seconds = 5

    def shutdown(self):
        """
        Shutdown the Pi
        :return:
        """
        logger.debug(f"Switching Off in {self.shutdown_wait_seconds} seconds")
        sleep(self.shutdown_wait_seconds)
        call('sudo shutdown now', shell=True)

    def reboot(self):
        """
        Restart the Pi
        :return:
        """
        logger.debug(f"Restarting in {self.shutdown_wait_seconds} seconds")
        sleep(self.shutdown_wait_seconds)
        call('sudo reboot now', shell=True)


PiOperationsAccess = PiOperations()

if __name__ == "__main__":
    """
    Run the PiOperations class to test.txt LED function
    """
    PiOperationsAccess.shutdown()
