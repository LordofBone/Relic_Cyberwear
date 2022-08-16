import importlib

import sounddevice as sd
import soundfile as sf

from config.nix_tts import *

import sys
import os

nix_dir = os.path.join(os.path.dirname(__file__), 'nix-tts')

sys.path.append(nix_dir)

mod = importlib.import_module('nix-tts.nix.models.TTS')
klass = getattr(mod, 'NixTTSInference')

sampling_frequency = 22050
filename = 'output.wav'

# Initiate Nix-TTS
nix = klass(model_dir=determ_model_path)

# Tokenize input text
c, c_length, phoneme = nix.tokenize(boot_text)
# Convert text to raw speech
xw = nix.vocalize(c, c_length)
# Listen to the generated speech
sd.play(xw[0, 0], sampling_frequency)
sf.write(filename, xw[0, 0], sampling_frequency)
