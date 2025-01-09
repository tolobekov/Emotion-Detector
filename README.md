# Emotion Detector using the Watson NLP library

For this project, you'll use the Emotion Predict function of the Watson NLP Library. For accessing this function, the URL, the headers, and the input json format is as follows.

´´´URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
´´´
Note that the text_to_analyze is being used as a variable that holds the actual written text that needs to be analyzed.
