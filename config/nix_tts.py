from pathlib import Path
import os

nix_dir = os.path.join(Path(__file__).parent.parent, 'nix-tts')
audio_dir = Path(__file__).parent.parent / f"audio"

determ_model_path = Path(__file__).parent.parent / f"models/deterministic"
stoch_model_path = Path(__file__).parent.parent / f"models/stochastic"

boot_text = "Welcome to the Arasaka Relic Cyberware System"
long_boot_text = "Welcome to the Arasaka Relic Cyberware System, your consciousness is now fused with someone whos " \
                 "mind was acquired by the soul killer software produced by the arasaka corporation, please enjoy our" \
                 " product "

shutdown_text = "Shutting down the system, please wait"

audio_on = True
file_name = "tts_output.wav"
