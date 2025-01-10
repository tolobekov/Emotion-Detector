import requests
import json

def emotion_detector(text_to_analyse):
    # URL of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the Emotion prediction service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the Emotion prediction API
    response = requests.post(url, json=myobj, headers=header)
    data = response.json()

    # Extract the first set of emotion data from the response
    emotions = data['emotionPredictions'][0]['emotion']

    # Initialize the dictionary for the output with extracted emotions and their scores
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }

    # Finding the dominant emotion by identifying the emotion with the highest score
    dominant_emotion = max(output, key=output.get)  # Uses the key parameter to find the max value in the dictionary

    # Adding the dominant emotion to the output dictionary
    output['dominant_emotion'] = dominant_emotion

    return output