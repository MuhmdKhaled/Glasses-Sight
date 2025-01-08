import RPi.GPIO as GPIO
import time
import subprocess
import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
from gtts import gTTS
import os
import numpy as np
from skimage import filters
from skimage import morphology
from gpiozero import Button
GPIO.setmode(GPIO.BCM)

# Set up GPIO
BUTTON_PIN = 23
ULTRASONIC_TRIGGER_PIN = 16
ULTRASONIC_ECHO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ULTRASONIC_TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ULTRASONIC_ECHO_PIN, GPIO.IN)

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

button = Button(BUTTON_PIN)

def button_pressed(channel):
    print("Button pressed")
    start_time = time.time()
    while button.is_pressed: # Wait for button release or 3 seconds timeout
        if time.time() - start_time >= 3:
            print("Button pressed for 3 seconds or more. Executing command.")
            os.system("python filename.py")  # Replace 'filename.py' with your script filename
            return
    print("Button pressed for less than 3 seconds.")
    distance = measure_distance()
    if 40 <= distance <= 150:
        image_path = capture_image()
        text = ocr_image(image_path)
        speak_text(text)
    else:
        print("Distance not within range (40cm - 150cm)")

def measure_distance():
    GPIO.output(ULTRASONIC_TRIGGER_PIN, True)
    time.sleep(0.00001)
    GPIO.output(ULTRASONIC_TRIGGER_PIN, False)
    start_time = time.time()
    stop_time = time.time()
    while GPIO.input(ULTRASONIC_ECHO_PIN) == 0:
        start_time = time.time()
    while GPIO.input(ULTRASONIC_ECHO_PIN) == 1:
        stop_time = time.time()
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Speed of sound is 34300 cm/s
    return distance

def capture_image():
    image_path = "/path/to/image.jpg"
    subprocess.run(["fswebcam", "-r", "1280x720", image_path])
    print("Image captured:", image_path)
    
    image = Image.open(image_path)
    image_gray = image.convert('L') #gray
    image_blurred = image_gray.filter(ImageFilter.GaussianBlur(radius=2)) #gaussian blur to reduse noise
    image_enhanced = ImageEnhance.Contrast(image_blurred).enhance(1.5) #enhance contrast
    image_array = np.array(image_enhanced)    # to numpy array for skimage processing
    image_eroded = morphology.binary_erosion(image_array, morphology.disk(5)) # erosion to remove small white regions and enhance dark regions
    image_dilated = morphology.binary_dilation(image_eroded, morphology.disk(5)).astype(np.uint8) * 255 #restore the size of text regions
    image_dilated_pil = Image.fromarray(image_dilated * 255).convert('L')
    image_dilated_pil.save(image_path)
    return image_path


def ocr_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print("OCR Result:", text)
    return text

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")


# Add event detection for button press
#GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_pressed, bouncetime=300)
button.when_pressed = button_pressed
try:
    while True:

        dist = measure_distance()
        print("Distance:", dist, "cm")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
