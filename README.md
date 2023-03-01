### Installation

#### Quick Warning
This code AND hardware should not be used for medical diagnosis. It's for fun/novelty use only, so bear that in mind 
while using it. Also bear in mind that ChatGPT will respond with the style of whatever context you have set within 
config/chatgpt_config.py, so I can't be sure what it will say. And I can't take any responsibility for any other context 
that is set or what it says.

Grab the latest RPi OS 64 bit using the Raspberry Pi Imager [here](https://www.raspberrypi.org/software/)

Checkout the code with:

```git clone --recursive https://github.com/LordofBone/Relic_Cyberwear.git```

Install the requirements:

```pip install -r requirements.txt```

Follow the installation instructions for ChatGPT Wrapper [here](https://github.com/mmabrouk/chatgpt-wrapper#installation)

I found the ChatGPT Wrapper wouldn't install properly within a virtual environment on Raspberry Pi (YMMV), so I installed 
it outside the virtual environment with:

```sudo pip install git+https://github.com/mmabrouk/chatgpt-wrapper```

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