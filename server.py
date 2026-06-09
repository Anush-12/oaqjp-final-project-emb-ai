"""
Server module for the Emotion Detection application.
Provides API endpoints to analyze text emotions and render the home page.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')


@app.route('/emotionDetector')
def emot_detector():
    """
    Analyzes the query text input and returns the formatted emotion scores.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    # Broken into smaller parts to fix Pylint's line-too-long (C0301) warning
    res_str = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return res_str


@app.route('/')
def render_index_page():
    """
    Renders the index.html home page template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
