"""
This module implements a Flask web server for an Emotion Detection application.
It provides web endpoints to analyze text via the emotion_detector and to serve
the application's front-end via Flask's templating engine.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emot_detector():
    """
    Analyze text to detect dominant emotions. Responds with emotion scores and dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    output = emotion_detector(text_to_analyze)
    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Use f-string for better readability and performance
    return (f"For the given statement, the system response is 'anger': {output['anger']}, "
            f"'disgust': {output['disgust']}, 'fear': {output['fear']}, 'joy': {output['joy']}, "
            f"and 'sadness': {output['sadness']}. "
            f"The dominant emotion is {output['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    """
    Renders the index page from a template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
