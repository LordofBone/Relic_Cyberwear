import logging

from Lakul.integrate_stt import SpeechtoTextHandler
from api.chatgpt_integration import run_chatgpt
from config.nix_tts import *
from functions.tts_operations import TTSOperationsAccess
from hardware.pi_operations import PiOperationsAccess

logging.basicConfig()
logger = logging.getLogger(__name__)


class TalkController:
    def __init__(self):
        """
        This is the main class that runs the STT and bot interaction.
        """
        self.STT_handler = SpeechtoTextHandler()

        self.inference_output = None

        self.bot_response = None

    def speak_tts(self, text):
        """
        This function is used to speak custom text.
        :return:
        """
        TTSOperationsAccess.generate_tts(text)

    def speak_tts_bot_response(self):
        """
        This function is used to speak the bot response.
        :return:
        """
        TTSOperationsAccess.generate_tts(self.bot_response)

    def listen_stt(self):
        """
        This is the main function that runs the STT and bot interaction.
        :return:
        """

        print("Listening")

        self.STT_handler.initiate_recording()

        print("Inferencing")

        self.inference_output = self.STT_handler.run_inference()

        print("DONE")

        print(self.inference_output)
        logger.debug(self.inference_output)

    def command_checker(self):
        """
        This function checks for commands.
        :return:
        """
        if self.inference_output == "SHUTDOWN":
            TTSOperationsAccess.generate_tts(shutdown_text)
            PiOperationsAccess.shutdown_pi()
        elif self.inference_output == "SHUT DOWN":
            TTSOperationsAccess.generate_tts(shutdown_text)
            PiOperationsAccess.shutdown_pi()
        elif self.inference_output == "REBOOT":
            TTSOperationsAccess.generate_tts(reboot_text)
            PiOperationsAccess.reboot_pi()

    def get_bot_engine_response(self):
        """
        This function returns the bot response.
        :return:
        """
        self.bot_response = run_chatgpt(self.inference_output)

        print(self.bot_response)
        logger.debug(self.bot_response)


TalkControllerAccess = TalkController()
