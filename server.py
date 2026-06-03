from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route(/emotionDetector)
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(textToAnalyze)

    output = "For the given statement, the system response is "
    output += "'anger': " + str(response['anger']) + ", "
    output += "'disgust': " + str(response['disgust']) + ", "
    output += "'fear': " + str(response['fear']) + ", "
    output += "'joy': " + str(response['joy']) + " and "
    output += "'sadness': " + str(response['sadness']) + ". "
    output += "The dominant emotion is " + response['dominant_emotion'] + "."

    return output