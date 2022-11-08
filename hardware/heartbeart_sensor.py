# NOTE! This code should not be used for medical diagnosis. It's
# for fun/novelty use only, so bear that in mind while using it.

# This code is based on the MAX30105 library examples by Pimoroni: https://github.com/pimoroni/max30105-python

from max30105 import MAX30105, HeartRate

import logging
import threading

logger = logging.getLogger("heartbeart-sensor-logger")


class SensorInit:
    """
    Sets up the sensor and returns the sensor object for use in other functions
    """

    def __init__(self):
        self.hr = None

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


def display_heartrate(beat, bpm, avg_bpm):
    """
    This function will display the bpm on the console and set the bpm in the setter class
    :param beat:
    :param bpm:
    :param avg_bpm:
    :return:
    """
    logger.info("{} BPM: {:.2f}  AVG: {:.2f}".format("<3" if beat else "  ", bpm, avg_bpm))

    bpm_setter.set_bpm(bpm)


def return_bpm():
    """
    This function will return the bpm value
    :return:
    """
    if heartbeat_sensor_online:
        sensor_init.hr.on_beat(display_heartrate, average_over=4)
    else:
        return -1


# print("""
# NOTE! This code should not be used for medical diagnosis. It's
# for fun/novelty use only, so bear that in mind while using it.
# This example shows a readout of your heart rate in BPM (beats per
# minute) and heartbeats detected using a heart emoticon <3.
# It's best to hold the sensor against your fingertip (the fleshy side)
# using a piece of wire or a rubber band looped through the mounting
# holes on the breakout, as the sensor is very sensitive to small
# movements and it's hard to hold your finger against the sensor with
# even pressure.
# If you're using your MAX30105 Breakout with Breakout Garden, then
# we'd recommend using one of our Breakout Garden Extender Kits with
# some female-to-female jumper jerky.
# https://shop.pimoroni.com/products/breakout-garden-extender-kit
# """)

try:
    sensor_core = sensor_setup()
    heartbeat_sensor_online = True
    bpm_setter = BPMSetter()
    sensor_init = SensorInit()
    sensor_init.set_sensor(sensor_core)
    threading.Thread(target=return_bpm, daemon=False).start()

except ModuleNotFoundError as e:
    logger.error(f"MAX30105 could not initialise or is not installed with error {e}. "
                 f"Please check your wiring/libraries.")
    heartbeat_sensor_online = False
