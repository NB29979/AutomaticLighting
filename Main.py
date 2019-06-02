#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess

PIRPin =26

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIRPin,GPIO.IN)

def main():
    while True:
        if(GPIO.input(PIRPin)!=0):
            print ('detected!')
            subprocess.call(['python', 'irrp.py', '-p', '-g17', '-f', 'IRCodes',  'light:off'])
            break

        else:
            print ('waiting...')
            time.sleep(1)

    destroy()


def destroy():
    GPIO.cleanup()
if __name__ == '__main__':
    setup()
    try:
            main()
    except KeyboardInterrupt:
        destroy()
        pass
