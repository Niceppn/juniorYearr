import speech_recognition as sr
import RPi.GPIO as GPIO
import time

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

def blink_led(speed):
    while True:
        GPIO.output(led_pin, True)
        time.sleep(speed)
        GPIO.output(led_pin, False)
        time.sleep(speed)

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language='th-TH')
            if command == "เร็ว":
                blink_led(0.1)
            elif command == "ปานกลาง":
                blink_led(0.5)
            elif command == "ช้า":
                blink_led(1)
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            pass

if __name__ == "__main__":
    try:
        recognize_speech()
    except KeyboardInterrupt:
        GPIO.cleanup()
