from flask import Flask, render_template, request
from EmotionDetection.emotion_detector import emotion_detector

app = Flask("Emotion Detection")
"""intilize app"""

@app.route("/")
def render_index_page():
    """Render the index page with the text input form."""
    return render_template('index.html')
@app.route("/emotionDetector")
def emotion_analyser():
    """
    Analyze the provided text for emotions.

    Retrieves the 'textToAnalyze' query parameter,
    sends it to the emotion detector, and returns
    a formatted string with emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)
    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!."
    formatted_text = "<br>".join(f"{key} : {value}" for key, value in response.items())
    return f"For the given statement, the system response is:<br>{formatted_text}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    