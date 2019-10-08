from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

app = Flask (__name__)

@app.route("/", methods=["GET","Post"])
def index():
	if request.method == "POST":
		GPIO.output(17,GPIO.HIGH)
		msg = request.form.get("submitBtnB")
                GPIO.output(27,GPIO.HIGH)
                msg = request.form.get("submitBtnR")
                GPIO.output(22,GPIO.HIGH)
                msg = request.form.get("submitBtnG")

	else:
		GPIO.output(17,GPIO.LOW)
                GPIO.output(27,GPIO.LOW)
                GPIO.output(22,GPIO.LOW)
                msg = "No click yet."
        return render_template("index.html", msg=msg)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
