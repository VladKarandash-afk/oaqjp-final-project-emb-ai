"""
This file is responsible for the server functionality. 
It runs the server on localhost:5000, takes the input text and gives 
a response of the emotion detection analysis.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

# Executing the emotion detection analysis
@app.route("/emotionDetector", methods = ["GET"])
def detection():
    """
    Function takes arguments from the GET method request, executes
    emotion_detection analysis on it and returns analysis result in
    a text form, highliting the dominant emotion separately.
    """

    # Passing the text as the request argument
    text_to_analyze = request.args.get('textToAnalyze')
    analysis = emotion_detector(text_to_analyze)

    # Handling the blank input error
    if analysis['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        "For the diven statement, the system response is"
        f" 'anger': {analysis['anger']}, 'disgust': "
        f"{analysis['disgust']}, 'fear': {analysis['fear']}"
        f", 'joy': {analysis['joy']} and 'sadness': "
        f"{analysis['sadness']}. The dominant emotion is"
        f" {analysis['dominant_emotion']}."
    )

# Main page rendering
@app.route("/")
def main_page():
    """
    Renders the "index.html" template for the main page
    """

    return render_template("index.html")

# Running the application on "localhost:5000"
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
