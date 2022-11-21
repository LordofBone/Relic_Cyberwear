from pathlib import Path
import sys

bot_engine_dir = Path(__file__).parent.parent / 'Bot_Engine'
chatbot_dir = bot_engine_dir / 'Chatbot_8'
lakul_dir = Path(__file__).parent.parent / 'Lakul'

sys.path.append(str(bot_engine_dir))
sys.path.append(str(chatbot_dir))
sys.path.append(str(lakul_dir))
