from flask import Flask, render_template, request, jsonify
from chat import get_responses
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.get('/')
def index_get():
    return render_template('index.html')


@app.post('/predict')
def predict():
    text = request.get_json().get("message")
    # Test error with try and catch
    response = get_responses(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
