import importlib
import sys
from fakeyou.fakeyou import FakeYou
from config.launch_config import fakeyou_mode
from config.fakeyou_config import *
import soundfile as sf
from time import sleep

from config.nix_tts import *
from functions.audio_output import AudioEngineAccess

sys.path.append(nix_dir)

mod = importlib.import_module('nix-tts.nix.models.TTS')
klass = getattr(mod, 'NixTTSInference')


class TTSOperations:
    def __init__(self):
        self.sampling_frequency = 22050
        self.filename = f'{audio_dir}/{file_name}'

        # Initiate Nix-TTS
        self.nix = klass(model_dir=stoch_model_path)

    def generate_tts(self, text_input):
        """
        Generate TTS output.
        :param text_input:
        :return:
        """
        # Tokenize input text
        c, c_length, phoneme = self.nix.tokenize(text_input)
        # Convert text to raw speech
        xw = self.nix.vocalize(c, c_length)
        sf.write(self.filename, xw[0, 0], self.sampling_frequency)
        # Play TTS output
        AudioEngineAccess.play_tts()


class TTSOperationsFakeYou:
    def __init__(self):
        self.tts_runner = FakeYou()
        self.tts_runner.login(username, password)

        self.filename = f'{audio_dir}/{file_name}'

    def generate_tts(self, text_input):
        """
        Generate TTS output.
        :param text_input:
        :return:
        """
        output = self.tts_runner.say(text_input, voice_model)

        output.save(self.filename)

        AudioEngineAccess.play_tts()


if fakeyou_mode:
    TTSOperationsAccess = TTSOperationsFakeYou()
else:
    TTSOperationsAccess = TTSOperations()
