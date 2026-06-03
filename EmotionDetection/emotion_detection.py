import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers=header)
    json_response = json.loads(response.text)
    print(json_response)
    response_formatted = json_response['emotionPredictions'][0]['emotion']

    # If the response status code is 400
    if response.status_code == 400:
        for key in response_formatted:
            response_formatted[key] = None
    else:
        dominant_emotion_score = 0
        dominant_emotion_name = ""
        for emotion in response_formatted:
            if response_formatted[emotion] > dominant_emotion_score:
                dominant_emotion_name = emotion
                dominant_emotion_score = response_formatted[emotion]



    response_formatted['dominant_emotion'] = dominant_emotion_name
    return response_formatted