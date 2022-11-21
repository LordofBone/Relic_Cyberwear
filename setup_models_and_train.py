import config.submodule_dirs

from Bot_Engine.utils.sentiment_training_suite import train_all as train_all_sentiment

from Bot_Engine.Chatbot_8.bot_8_trainer import bot_trainer as bot_trainer_8


def download_all_models_do_all_training():
    """
    This function will download all pre-trained models/data and train the required models
    :return:
    """
    train_all_sentiment()
    bot_trainer_8(fresh_db=True)


if __name__ == "__main__":
    download_all_models_do_all_training()
