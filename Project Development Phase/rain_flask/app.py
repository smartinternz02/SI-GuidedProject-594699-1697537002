from flask import Flask, render_template,request,redirect,url_for
import pickle
import numpy as np
app = Flask(__name__)
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)
@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        location = int(request.form["s"])  # Get the selected city as an integer
        input_values = [float(request.form[f"input{i}"]) for i in range(2, 9)]  # Updated field names
        input_values.insert(0, location)
        input_array = np.array(input_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        if prediction==0:
            return redirect(url_for('norain'))
        else:
            return redirect(url_for('rainy'))
    return render_template("index.html", prediction=prediction)
@app.route("/norain")
def norain():
    return render_template('norain.html')
@app.route("/rainy")
def rainy():
    return render_template("rain.html")
if __name__ == "__main__":
    app.run(debug=True)
