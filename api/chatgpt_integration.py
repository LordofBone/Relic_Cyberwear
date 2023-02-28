import asyncio
import string

from chatgpt_wrapper import ChatGPT

from config.chatgpt_config import request_context, post_context
from functions.heartrate_monitoring import HeartRateMonitorAccess


def run_chatgpt(text_input):
    """
    This function is used to run the chatgpt wrapper, it also gives context so that ChatGPT will talk like an AI from
    Cyberpunk as well as give the current BPM of the wearers heart rate. These can both be adjusted under
    config/chatgpt_config.py.
    :param text_input:
    :return:
    """
    text_with_context = ""
    text_with_context += f'{request_context}: "{text_input}", ' \
                         f'{string.Template(post_context).substitute(heart_rate=HeartRateMonitorAccess.get_rate())}'

    bot = ChatGPT()

    return asyncio.run(bot.ask(text_with_context))
