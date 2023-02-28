import logging

from playsound import playsound

from config.nix_tts import *

logger = logging.getLogger("voice-controller-logger")


def talking_start_finish(method):
    """ Using just the tts in-build 'is_talking' method will of course only work for tts, for playing wav files this
    has been added in so that the system knows when words are being spoken """

    def talk_time(*args, **kw):
        """
        This function is used to set the talking variable to True when the system is speaking and False when it is not.
        :param args:
        :param kw:
        :return:
        """
        while AudioEngineAccess.talking:
            pass
        AudioEngineAccess.talking = True
        logger.debug(f'Set talking variable to: {AudioEngineAccess.talking}')
        method(*args, **kw)
        AudioEngineAccess.talking = False
        logger.debug(f'Set talking variable to: {AudioEngineAccess.talking}')

    return talk_time


class AudioEngine:
    def __init__(self):
        self.talking = False

        self.path = Path(__file__).parent / "../audio"
        self.audio_on = audio_on

        self.generated_tts = f'{self.path}/{file_name}'

        self.online = f'{self.path}/online.wav'
        self.training = f'{self.path}/training.wav'

    @talking_start_finish
    def play_tts(self):
        """
        This function is used to play the generated TTS output.
        :return:
        """
        if self.audio_on:
            playsound(self.generated_tts)


AudioEngineAccess = AudioEngine()
