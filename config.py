#TOKEN = "6449655359:AAEFJ4EQv82HNs5mMWGzGA8Mw0rvyzsycoA"  # token телеграм-бота

#IAM_TOKEN = "t1.9euelZqNmZTNi86KmsuWm8rGjIuXi-3rnpWai5CPzpOMxpaTlcbLlI-QiZnl8_cDTwJO-e8zChIA_t3z90N9f0357zMKEgD-zef1656VmpiMk43ImZeZmsaRxorKksyb7_zF656VmpiMk43ImZeZmsaRxorKksybveuelZrJmsuMy8iJx5icjs6Ol82enrXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.k1wd7tJxylinIUhMopmEmj-AB7tbqhqE1MvSK8M4EEelbJ8tRLQodXEDg1bN3KFPoaX_B8-HZY8rS3_Vqhx_Dw"
#FOLDER_ID = 'b1gl5joq6m5j0s2njv9i'

MAX_USERS = 3  # максимальное кол-во пользователей
MAX_GPT_TOKENS = 120  # максимальное кол-во токенов в ответе GPT
COUNT_LAST_MSG = 4  # кол-во последних сообщений из диалога

# лимиты для пользователя
VOICE = 'zahar'
MAX_USER_STT_BLOCKS = 10  # 10 аудиоблоков
MAX_USER_TTS_SYMBOLS = 5_000  # 5 000 символов
MAX_USER_GPT_TOKENS = 2_000  # 2 000 токенов

#LOGS = 'logs.txt'  # файл для логов
#DB_FILE = 'messages.db'  # файл для базы данных
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты" и используй юмор. '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]  # список с системным промтом

HOME_DIR = '/home/student/gpt_bot'  # путь к папке с проектом
LOGS = f'{HOME_DIR}/logs.txt'  # файл для логов
DB_FILE = f'{HOME_DIR}/messages.db'  # файл для базы данных

IAM_TOKEN_PATH = f'{HOME_DIR}/creds/iam_token.txt'  # файл для хранения iam_token
FOLDER_ID_PATH = f'{HOME_DIR}/creds/folder_id.txt'  # файл для хранения folder_id
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt'  # файл для хранения bot_token