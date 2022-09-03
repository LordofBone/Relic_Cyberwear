from soran.integrate_stt import SpeechtoTextHandler

from Bot_Engine.functions import core_systems

from events.event_queue import EventQueueAccess, CurrentProcessQueueAccess
from Bot_Engine.functions.voice_controller import VoiceControllerAccess

from events.event_types import LISTEN_STT, TALK_SYSTEMS, SPEAK_TTS, REPEAT_INPUT_TTS, REPEAT_LAST, LISTENING, \
    INFERENCING_SPEECH, PROCESSING_RESPONSES, AUDIO_SYSTEM, ML_SYSTEM, RESPONSE_FOUND

from hardware.pi_operations import *

logger = logging.getLogger("talk-control")

BotControl = core_systems.CoreInterface.integrate()


class TalkController:
    def __init__(self):
        """
        This is the main class that runs the STT and bot interaction.
        """
        self.STT_handler = SpeechtoTextHandler()

        self.inference_output = None

        self.interrupt = False

    def activate_interrupt(self):
        """
        This function is used to interrupt the STT and bot interaction.
        :return:
        """
        self.interrupt = True

    def speak_tts(self):
        """
        This function is used to speak the bot response.
        :return:
        """
        VoiceControllerAccess.tts(self.bot_response)

    def listen_stt(self):
        """
        This is the main function that runs the STT and bot interaction.
        :return:
        """
        # todo: use TalkControllerAccess.STT_handler.listening
        CurrentProcessQueueAccess.queue_addition(AUDIO_SYSTEM, LISTENING, 1)

        self.STT_handler.initiate_recording()

        CurrentProcessQueueAccess.queue_addition(ML_SYSTEM, INFERENCING_SPEECH, 1)

        self.inference_output = self.STT_handler.run_inference()

        CurrentProcessQueueAccess.queue_addition(ML_SYSTEM, f"Heard: {self.inference_output}", 1)

        logger.debug(self.inference_output)

    def get_bot_engine_response(self):
        """
        This function returns the bot response.
        :return:
        """
        CurrentProcessQueueAccess.queue_addition(ML_SYSTEM, PROCESSING_RESPONSES, 1)

        self.bot_response = (BotControl.input_get_response(self.inference_output))

        CurrentProcessQueueAccess.queue_addition(RESPONSE_FOUND, f"REPLY: {self.bot_response}", 1)

        logger.debug(self.bot_response)
