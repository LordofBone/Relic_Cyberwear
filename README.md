### Installation

Grab the latest RPi OS 64 bit using the Raspberry Pi Imager [here](https://www.raspberrypi.org/software/)

Checkout the code with:

```git clone --recursive https://github.com/LordofBone/Relic_Cyberwear.git```

Install the requirements:

```pip install -r requirements.txt```

Follow the installation instructions for ChatGPT Wrapper [here](https://github.com/mmabrouk/chatgpt-wrapper#installation)

I found the ChatGPT Wrapper wouldn't install properly within a virtual environment on Raspberry Pi (YMMV), so I installed 
it outside the virtual environment with:

```sudo pip install git+https://github.com/mmabrouk/chatgpt-wrapper```

and also found that it would only install and login with:

```python -m chatgpt install```

Follow the installation for the Audio DAC Shim [here](https://shop.pimoroni.com/products/audio-dac-shim-line-out)

### Hardware

Got to my Hackster page [here](https://www.hackster.io/314reactor/relic-cyberware-7fafb9)
Or my Electromaker page [here](https://www.electromaker.io/profile/314Reactor)

For instructions on how the Hardware was made.

### Configuration

Check the context for the ChatGPT Wrapper under config/chatgpt_config.py and adjust depending on the persona you want
the Cyberware to have. Bear in mind I can't be sure what ChatGPT will say, especially with different contexts added in.

You can also change what it says on boot in config/nix_tts.py

### Running

Run the program with:
```python main.py```