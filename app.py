from flask import Flask, render_template, request, jsonify
from chat import get_responses
from flask_cors import CORS

app = Flask(__name__)

api_v1_cors_config = {
    "origins": ["http://localhost:5000"]
}
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.get('/')
def index_get():
    return render_template('index.html')


@app.post('/predict')
def predict():
    print("hi")
    text = request.get_json().get("message")
    # Test error with try and catch
    response = get_responses(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
