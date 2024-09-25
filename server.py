""" This is the server file """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/emotionDetector')
def sent_emotion():
    """ This function to send emotion """
    text_to_analyze = request.args.get('textToAnalyze')

    emotions = emotion_detector(text_to_analyze)
    if emotions is None:
        return "Invalid text! Please try again!."
    result = f"""For the given statement, the system response is:<br>
    Anger: {emotions['anger']}<br>
    Disgust: {emotions['disgust']}<br>
    Fear: {emotions['fear']}<br>
    Joy: {emotions['joy']}<br>
    Sadness': {emotions['sadness']}.<br>
    The dominant emotion is: {emotions['dominant_emotion']}."""
    return result


@app.route('/')
def render_index_page():
    """ This function render to the html page """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
