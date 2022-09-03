import importlib

import soundfile as sf

from config.nix_tts import *
from functions.audio_output import AudioEngineAccess
import sys

sys.path.append(nix_dir)

mod = importlib.import_module('nix-tts.nix.models.TTS')
klass = getattr(mod, 'NixTTSInference')


class TTSOperations:
    def __init__(self):
        self.sampling_frequency = 22050
        self.filename = f'{audio_dir}/{file_name}'

        # Initiate Nix-TTS
        self.nix = klass(model_dir=determ_model_path)

    def generate_tts(self, text_input):
        # Tokenize input text
        c, c_length, phoneme = self.nix.tokenize(text_input)
        # Convert text to raw speech
        xw = self.nix.vocalize(c, c_length)
        sf.write(self.filename, xw[0, 0], self.sampling_frequency)
        # Play TTS output
        AudioEngineAccess.play_tts()


TTSOperationsAccess = TTSOperations()

if __name__ == "__main__":
    TTSOperationsAccess.generate_tts(boot_text)
