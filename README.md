Glasses Sight Assistance Project
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Overview
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project aims to provide an assistive tool for individuals with visual impairments by combining image processing, text-to-speech conversion, and physical interaction capabilities using a Raspberry Pi.
The system captures images, extracts text from them, and reads the text aloud to the user. 
It also includes proximity detection and button-triggered operations to ensure seamless interaction.


![WhatsApp Image 2024-06-29 at 15 07 04_4f49b12e](https://github.com/user-attachments/assets/dc257e85-acae-432f-977b-559f65867c7d)


![WhatsApp Image 2024-06-29 at 15 07 07_bef2be34](https://github.com/user-attachments/assets/89dc16a3-8deb-4f68-8d1e-f0afa72f84d7)


Features
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Color Detection:
----------------------------------------------------------------------------------------------------------------------------------------

Determines the dominant color in an image using k-means clustering and maps it to the closest CSS3 color name for better recognition.

File: color.py.

Optical Character Recognition (OCR) and Text-to-Speech (TTS):
---------------------------------------------------------------------------------------------------------------------------------

Converts text from images to speech using Tesseract OCR and Google Text-to-Speech (gTTS).

File: GTTS.py.

Interactive Raspberry Pi Integration:
--------------------------------------------------------------------------------------------------------------------------------

Utilizes GPIO pins for button press detection and ultrasonic sensors for measuring distances.

Captures and processes images for text extraction and audio playback.

File: projectcode_version_one.py.

Real-Time Feedback:
-----------------------------------------------------------------------------------------------------------------------------------------------

Provides instant auditory feedback based on detected text or distance measurements.

Technology Stack
---------------------------------------------------------------------------------------------------------------------------------

Hardware:
------------------------------------------------------------------------------------------------------------------------------------------------------

Raspberry Pi

Ultrasonic sensors

Camera module

Physical button

Software:
---------------------------------------------------------------------------------------------------------------------------------------------------------

Python

OpenCV

Tesseract OCR

gTTS (Google Text-to-Speech)

GPIO library for Raspberry Pi

Installation and Setup
-------------------------------------------------------------------------------------------------------------------------------------------------------

Prerequisites
---------------------------------------------------------------------------------------

Install Python and required libraries:
-------------------------------------------------------------------------------------

bash

Copy code

pip install opencv-python webcolors gtts playsound pytesseract gpiozero numpy pillow scikit-image

Ensure Tesseract OCR is installed:
----------------------------------------------------------------------------------------------

bash

Copy code

sudo apt-get install tesseract-ocr

Install additional tools for Raspberry Pi:
----------------------------------------------------------------------------------------------------------

bash

Copy code

sudo apt-get install fswebcam mpg321

Hardware Setup
------------------------------------------------------------------------------------------------------------

Connect the camera module to the Raspberry Pi.

Connect the button to GPIO pin 23 and ultrasonic sensor to pins 16 (trigger) and 18 (echo).

Ensure all components are securely connected.

Usage
-------------------------------------------------------------------------------------------

Clone the repository and navigate to the project directory.

Execute the main script:
-----------------------------------------------------------------------------------------------------

bash

Copy code

python projectcode_version_one.py

Interact with the system by pressing the button or positioning an object within the ultrasonic sensor's range.

Example Workflow

Press the Button:
---------------------------------------------------------------------------------------------------------

Short Press: Captures an image and extracts text for auditory feedback.

Long Press: Executes a custom command or script.

Proximity Detection:
-----------------------------------------------------------------------------------------------------------

Detects objects within a predefined distance range and triggers the text-to-speech functionality.

Color Detection:
----------------------------------------------------------------------------------------------------

Analyzes an uploaded image to determine and announce its dominant color.

Contributing
----------------------------------------------------------------------------------------------------------------

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

Acknowledgments
------------------------------------------------------------------------------------------------------------------

Tesseract OCR

Google Text-to-Speech

Raspberry Pi
