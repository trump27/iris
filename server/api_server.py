# run
# python api_server.py
# predict
# curl http://127.0.0.1:8888/predict -X POST -H 'Content-Type:application/json' -d '{"feature":[1, 1, 1, 1]}'

from sklearn.externals import joblib
import flask
from flask_cors import CORS
import numpy as np

MODEL_FILE = './iris_model.pkl'
RUN_PORT = 8888

# initialize our Flask application and pre-trained model
app = flask.Flask(__name__)
CORS(app)
model = None


def load_model():
    global model
    print(" * Loading iris_model ...")
    model = joblib.load(MODEL_FILE)
    print(' * Loading end')


@app.route("/predict", methods=["POST"])
def predict():
    response = {
        "success": False,
        # "Content-Type": "application/json"
    }
    # ensure an feature was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.get_json().get("feature"):
            # read feature from json
            feature = flask.request.get_json().get("feature")

            # preprocess for classification
            # list  -> np.ndarray
            feature = np.array(feature).reshape((1, -1))

            # classify the input feature
            # response["prediction"] = model.predict(feature).tolist()

            proba = model.predict_proba(feature)
            proba = proba.flatten().tolist()

            response["predict"] = proba.index(max(proba))
            response["proba"] = max(proba)


            # indicate that the request was a success
            response["success"] = True
    # return the data dictionary as a JSON response
    return flask.jsonify(response)


if __name__ == "__main__":
    load_model()
    print(" * Flask starting server...")
    app.run(port=RUN_PORT)
