from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

app = Flask (__name__)

#blue
@app.route("/", methods=["GET","Post"])
def index():
	if request.method == "POSTB":
		GPIO.output(17,GPIO.HIGH)
		msg = request.form.get("submitBtnB")
	else:
		GPIO.output(17,GPIO.LOW)
		msg = "No click yet."
	return render_template("index.html", msg=msg)
#red
@app.route("/", methods=["GET","Post"])
def index():
        if request.method == "POSTR":
                GPIO.output(27,GPIO.HIGH)
                msg = request.form.get("submitBtnR")
        else:
                GPIO.output(27,GPIO.LOW)
                msg = "No click yet."
        return render_template("index.html", msg=msg)
#green
@app.route("/", methods=["GET","Post"])
def index():
        if request.method == "POSTG":
                GPIO.output(22,GPIO.HIGH)
                msg = request.form.get("submitBtnG")
        else:
                GPIO.output(22,GPIO.LOW)
                msg = "No click yet."
        return render_template("index.html", msg=msg)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
