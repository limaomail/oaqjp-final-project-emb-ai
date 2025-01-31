import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonn = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = jsonn, headers=header)
    json_response = json.loads(response.text)

    if (response.status_code == 200):
        anger = json_response['emotionPredictions'][0]['emotion']['anger']
        disgust = json_response['emotionPredictions'][0]['emotion']['disgust']
        fear = json_response['emotionPredictions'][0]['emotion']['fear']
        joy = json_response['emotionPredictions'][0]['emotion']['joy']
        sadness = json_response['emotionPredictions'][0]['emotion']['sadness']
        emotion_dict = {'anger':anger, 'disgust':disgust, 'fear':fear, 'joy':joy, 'sadness':sadness}
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    elif (response.status_code == 400):
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    return {'anger': anger, 'disgust': disgust, 'fear':fear, 'joy':joy, 'sadness':sadness, 'dominant_emotion':dominant_emotion}
