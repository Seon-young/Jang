import RPi.GPIO as gpio
import time
import dht11
import datetime

# sensor_sonic's using pin number
trig_pin = 13
echo_pin = 19

# sensor_led's using pin number
red_led_pin = 16
yellow_led_pin = 20
green_led_pin = 21

gpio.setmode(gpio.BCM)
# sensor_sonic's gpio setting
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)
# sensor_led's gpio setting
gpio.setup(red_led_pin, gpio.OUT)
gpio.setup(yellow_led_pin, gpio.OUT)
gpio.setup(green_led_pin, gpio.OUT)

def onLED(distance):
    if distance >= 100 :
        gpio.output(green_led_pin,True)
        time.sleep(0.5)
    elif distance >= 30 :
        gpio.output(yellow_led_pin,True)
        time.sleep(0.5)
    else
        gpio.output(red_led_pin,True)
        time.sleep(0.5)

    gpio.output(red_led_pin,False)
    gpio.output(yellow_led_pin,False)
    gpio.output(green_led_pin,False)

try:
	while True:
        # trig_pin OFF
		gpio.output(trig_pin, False)
		time.sleep(0.5)

        # trig_pin ON, emission sonic signal
		gpio.output(trig_pin, True)
		time.sleep(0.00001)

        # trig_pin OFF
		gpio.output(trig_pin, False)

		while gpio.input(echo_pin) == 0:
			pulse_start = time.time()

        # if echo_pin receive sonic signal, you can measure time
		while gpio.input(echo_pin) == 1:
			pulse_end = time.time()

        # time(s)
		pulse_duration = pulse_end - pulse_start
        # velocity(cm/s) = 17000cm/s = 340m/s / 2 * 100
		distance = pulse_duration * 17000
		distance = round(distance, 2)

		print "Distance : ", distance, "cm"

        onLED(int(distance))

# end
except KeyboardInterrupt as e:
	gpio.cleanup()
