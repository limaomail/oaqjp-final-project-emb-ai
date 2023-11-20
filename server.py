''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' Emotion Detector '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    value = (f"For the given statement, the system repsonse is 'anger': {anger}, "
    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}.")

    return value

@app.route("/")
def render_index_page():
    ''' Render Index Page '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
