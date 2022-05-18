from flask import Flask, request
import joblib
import numpy

MODEL_PATH = "mlmodels/model.pkl"
SCALER_X_PATH = "mlmodels/scaler_x.pkl"
SCALER_Y_PATH = "mlmodels/scaler_y.pkl"

MODEL_PATH_final = "mlmodels/model2.pkl"
SCALER_X_PATH_final = "mlmodels/scaler_x2.pkl"
SCALER_Y_PATH_final = "mlmodels/scaler_y2.pkl"

app = Flask(__name__)

@app.route('/predict_price', methods = ['GET'])
def predict():
    args = request.args
    model = args.get('model_version', default=-1, type=int)

    floor = args.get('floor', default=-1, type=int)
    open_plan = args.get('open_plan', default=-1, type=int)
    rooms = args.get('rooms', default=-1, type=int)
    area = args.get('area', default=-1, type=float)
    renovation = args.get('renovation', default=-1, type=int)

    if model == 1:

        # response = 'open_plan:{}, rooms:{}, area:{}, renovation:{}'.format(open_plan, rooms, area, renovation)
        model = joblib.load(MODEL_PATH)
        sc_x = joblib.load(SCALER_X_PATH)
        sc_y = joblib.load(SCALER_Y_PATH)

        x = numpy.array([open_plan, rooms, area, renovation]).reshape(1, -1)
        x = sc_x.transform(x)
        result = model.predict(x)
        result = sc_y.inverse_transform(result.reshape(1, -1))

        return str(result[0][0])

    if model == 2:

        # response = 'floor:{}, open_plan:{}, rooms:{}, area:{}.format(floor, open_plan, rooms, area, renovation)

        model2 = joblib.load(MODEL_PATH_final)
        sc_x2 = joblib.load(SCALER_X_PATH_final)
        sc_y2 = joblib.load(SCALER_Y_PATH_final)

        x2 = numpy.array([floor, open_plan, rooms, area]).reshape(1, -1)
        x2 = sc_x2.transform(x2)
        result2 = model2.predict(x2)
        result2 = sc_y2.inverse_transform(result2.reshape(1, -1))

        return str(result2[0][0])

    else:
        return "not a valid model"


if __name__ == '__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')