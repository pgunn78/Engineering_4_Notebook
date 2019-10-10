from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

app = Flask (__name__)

@app.route('/')
def  ledset():
	return render_template('ledset.html')

@app.route("/", methods=["GET","Post"])
def results():

	if request.method == "POST":
		red = request.form['red']
		ledData = {
			'red' : red,
			}
		if red == 'on':
			GPIO.output(17,GPIO.HIGH)
		else:
			GPIO.output(17,GPIO.LOW)
       		return render_template("result.html", **ledData)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
