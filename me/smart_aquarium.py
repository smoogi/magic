import sys
import cayenne.client
import RPi.GPIO as GPIO
import bh1750 as BH1750

from time import sleep,time
from DHT11_Python.dht11 import DHT11

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Setup GPIO pin
dht_pin = DHT11(pin=4) # setup pin for DHT11 sensor
GPIO.setup(16, GPIO.OUT) # setup pin for light control relay
GPIO.setup(20, GPIO.OUT) # setup pin for food dispensor
GPIO.setup(21, GPIO.OUT) # setup pin for oxygen pump

def on_message(message):
	""" The callback for when a message is received from Cayenne. """
	print("message received: " + str(message))
	if message.channel == 4:
		GPIO.output(20, False)
		sleep(4)
		GPIO.output(20, True)
	elif message.channel == 5:
		if message.value == '1':
			GPIO.output(21, True)
		elif message.value == '0':
			GPIO.output(21, False)
# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "4ab38130-12c7-11e8-aa1d-e5677d2125ce"
MQTT_PASSWORD  = "89b952119800eec482c9b0deb394fa23946493f8"
MQTT_CLIENT_ID = "e0b30150-1df9-11e8-af7b-4f8845dd6501"

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)

temp = None # variable for temparature
light = None # variable for light level
i = 0 # counter for debugging
light_state = False
light_last_state = False

try:
	while True:	
		# Always call this method every time to send data properly 
		client.loop()
		
		# Read data from DHT11 and BH1750
		result = dht_pin.read()	
		if result.is_valid():
			temp = result.temperature
		if BH1750.readLight() is not None:
			light = BH1750.readLight()
		
		# Setup data for sending to cloud server via MQTT
		client.celsiusWrite(1,temp)
		client.luxWrite(2, light)
		
		# Turn light On-Off according to environment light
		if light < 25:
			light_state = False 
		else:
			light_state = True
		GPIO.output(16,light_state)
		
		# Notify user when light state change
		if light_state is not light_last_state:
			print("Environment light: %.2f" % light)
			if light_state is False:
				print("Below light level treshold")
				print("Turn light on")
			else:
				print("Turn light off")
		light_last_state = light_state

		# Print counter 'i' for debugging
		print(i)
		i += 1
		if i > sys.maxsize:
			i = 0
		
		# delay for 1 second	
		sleep(1)
	
except (KeyboardInterrupt, SystemExit):
	print("\nExit by user")
	GPIO.cleanup() # clean up GPIO on CTRL+C exit
	
except Exception as e:
	print("\nError occured: %s" % e)
