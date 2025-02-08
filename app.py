from flask import Flask, render_template,request,send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/vid/<path:filename>')
def serve_video(filename):
    return send_from_directory('vid', filename)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="POST":
        msg=request.form.get("message")
        print(msg)
    else:
        return render_template("predict.html")


if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5050)