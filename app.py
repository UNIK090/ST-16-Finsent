from flask import Flask, render_template, request
from test import TextToNum
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained vectorizer and model
with open("vectorizer.pickle", "rb") as vc_file:
    vectorizer = pickle.load(vc_file)

with open("model.pickle", "rb") as model_file:
    model = pickle.load(model_file)

# Homepage Route
@app.route("/")
def index():
    return render_template("index.html")

# Prediction Route
@app.route("/predict", methods=['POST', 'GET'])
def predict():
    if request.method == "POST":
        try:
            # Get user input
            msg = request.form.get("message")
            if not msg:
                return render_template("predict.html", error="Please enter a valid message.")

            # Process text
            ob = TextToNum(msg)
            ob.cleaner()
            ob.token()
            ob.removeStop()
            st = ob.stemme()
            stem_vector = " ".join(st)

            # Transform text into feature vector
            vcdata = vectorizer.transform([stem_vector]).toarray()

            # Predict sentiment
            pred = model.predict(vcdata)
            sentiment_map = {1: "Positive 😊", 0: "Neutral 😐", -1: "Negative 😢"}
            sentiment = sentiment_map.get(pred[0], "Unknown")

            return render_template("result.html", sentiment=sentiment)

        except Exception as e:
            return render_template("predict.html", error=f"Error processing request: {str(e)}")

    return render_template("predict.html")

# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5054, debug=True)
