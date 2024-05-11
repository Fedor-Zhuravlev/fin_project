import requests
from config import VOICE
from creds import get_creds
def text_to_speech(text):
    iam_token, folder_id = get_creds()
    headers = {'Authorization': f"Bearer {iam_token}"}
    data = {'text': text,  # текст, который нужно преобразовать в голосовое сообщение
            'lang': 'ru-RU',  # язык текста - русский
            'voice': VOICE,  # мужской голос Филиппа
            'folderId': folder_id}
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return True, response.content
    else:
        return False, "При запросе в SpeechKit возникла ошибка"


def speech_to_text(data):
    # iam_token, folder_id для доступа к Yandex SpeechKit
    iam_token, folder_id = get_creds()

    params = "&".join([
        "topic=general",
        f"folderId={folder_id}",
        "lang=ru-RU"
    ])

    headers = {
        'Authorization': f'Bearer {iam_token}',
    }

    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )

    decoded_data = response.json()

    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result")
    else:
        return False, "При запросе в SpeechKit возникла ошибка"



