''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")
@app.route("/emotionDetector")
def emo_detector():
    '''Emotion Detector function'''

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        statement = "Invalid text! Please try again!"
    else:
        statement = (
    f"For the given statement, the system response is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}.") 

    return statement
@app.route("/")
def render_page():
    '''HTML page rendering function'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
