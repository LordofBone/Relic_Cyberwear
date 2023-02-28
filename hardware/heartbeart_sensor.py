# NOTE! This code should not be used for medical diagnosis. It's
# for fun/novelty use only, so bear that in mind while using it.

# This code is based on the MAX30105 library examples by Pimoroni: https://github.com/pimoroni/max30105-python

import logging

from max30105 import MAX30105, HeartRate

logger = logging.getLogger("heartbeart-sensor-logger")


def sensor_setup():
    """
    This function will set up the sensor and return the sensor object
    :return:
    """
    max30105 = MAX30105()

    max30105.setup(leds_enable=2)

    max30105.set_led_pulse_amplitude(1, 0.2)
    max30105.set_led_pulse_amplitude(2, 12.5)
    max30105.set_led_pulse_amplitude(3, 0)

    max30105.set_slot_mode(1, 'red')
    max30105.set_slot_mode(2, 'ir')
    max30105.set_slot_mode(3, 'off')
    max30105.set_slot_mode(4, 'off')

    return max30105


class SensorOperations:
    """
    This class will handle all the sensor operations and allow the bpm to be set and retrieved from other modules
    """

    def __init__(self):
        """
        This function will initialise the sensor and set the bpm to 0
        """
        try:
            self.sensor_init = self.SensorInit()
            self.sensor_core = sensor_setup()
            self.sensor_init.set_sensor(self.sensor_core)
            self.sensor_init.heartbeat_sensor_online = True

        except ModuleNotFoundError as e:
            logger.error(f"MAX30105 could not initialise or is not installed with error {e}. "
                         f"Please check your wiring/libraries.")

        self.bpm_setter = self.BPMSetter()

        logger.info("Heartbeat Sensor Online")

    class SensorInit:
        """
        Sets up the sensor and returns the sensor object for use in other functions
        """

        def __init__(self):
            self.hr = None
            self.heartbeat_sensor_online = False

        def set_sensor(self, max30105):
            self.hr = HeartRate(max30105)

    class BPMSetter:
        """
        Sets the bpm as a value for other functions to use
        """

        def __init__(self):
            self.bpm = 0

        def set_bpm(self, bpm):
            self.bpm = bpm

        def get_bpm(self):
            return self.bpm

    def display_heartrate(self, beat, bpm, avg_bpm):
        """
        This function will set the bpm value and exit the on_beat function if beat detected
        """
        logger.debug("{} BPM: {:.2f}  AVG: {:.2f}".format("<3" if beat else "  ", bpm, avg_bpm))

        self.bpm_setter.set_bpm(bpm)

        if bpm == 0:
            return False
        else:
            return True

    def bpm_handler(self):
        """
        This function will handle the bpm and call the display_heartrate function, recalling the on_beat function when
        heartrate is detected; this is to ensure that if a beat is detected it will not continue returning the same bpm
        even if the heart rate is 0 on subsequent checks. This is because on_beat only updates the bpm when a beat is
        detected
        """

        while True:
            if self.sensor_init.heartbeat_sensor_online:
                self.sensor_init.hr.on_beat(self.display_heartrate, average_over=4)
            else:
                self.bpm_setter.set_bpm(-1)


SensorOperationsAccess = SensorOperations()

print("""
NOTE! This code should not be used for medical diagnosis. It's
for fun/novelty use only, so bear that in mind while using it.
This example shows a readout of your heart rate in BPM (beats per
minute) and heartbeats detected using a heart emoticon <3.
It's best to hold the sensor against your fingertip (the fleshy side)
using a piece of wire or a rubber band looped through the mounting
holes on the breakout, as the sensor is very sensitive to small
movements and it's hard to hold your finger against the sensor with
even pressure.
If you're using your MAX30105 Breakout with Breakout Garden, then
we'd recommend using one of our Breakout Garden Extender Kits with
some female-to-female jumper jerky.
https://shop.pimoroni.com/products/breakout-garden-extender-kit
""")
