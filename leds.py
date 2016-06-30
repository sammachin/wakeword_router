import RPi.GPIO as GPIO


r = 4		# GPIO Pin for the playback/activity light
b = 27		# GPIO Pin for the recording light
g = 17		# GPIO Pin for the recording light

lights = [r, b, g] 


def setup():
	GPIO.setwarnings(False)
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(lights, GPIO.OUT)
	GPIO.output(lights, GPIO.LOW)

def off():
	GPIO.output(lights, GPIO.LOW)

		
def red():
	GPIO.output(lights, GPIO.LOW)
	GPIO.output(r, GPIO.HIGH)


def blue():
	GPIO.output(lights, GPIO.LOW)
	GPIO.output(b, GPIO.HIGH)


def green():
	GPIO.output(lights, GPIO.LOW)
	GPIO.output(g, GPIO.HIGH)


def purple():
	GPIO.output(lights, GPIO.LOW)
	GPIO.output([r, b], GPIO.HIGH)


def white():
	GPIO.output(lights, GPIO.LOW)
	GPIO.output(lights, GPIO.HIGH)
	