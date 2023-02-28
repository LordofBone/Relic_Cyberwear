import asyncio
from chatgpt_wrapper import ChatGPT
from functions.heartrate_monitoring import HeartRateMonitorAccess
from config.chatgpt_config import request_context, post_context


def run_chatgpt(text_input):
    text_with_context = ""
    text_with_context += f'{request_context}: "{text_input}", {post_context}'

    bot = ChatGPT()

    return asyncio.run(bot.ask(text_with_context))
