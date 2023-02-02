import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)
pwm = machine.PWM(machine.Pin(15))
pwm.freq(50)


def blink_onboard_led(num_blinks):
    for i in range(num_blinks):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.2)


def handleGP(item, value):
    pin = machine.Pin(int(item[2:]), machine.Pin.OUT)
    pin.value(int(value))


def handleLed(value):
    if "1" == value:
        led.on()
    if "0" == value:
        led.off()


def handleServo(value):
    try:
        valuesFromToSpeed = value.split(',')

        valueFrom = int(valuesFromToSpeed[0])
        valueTo = int(valuesFromToSpeed[1])

        if (valueFrom < valueTo):
            for position in range(valueFrom, valueTo, 50):
                pwm.duty_u16(position)
                time.sleep(.02)
        else:
            for position in range(valueFrom, valueTo, -50):
                pwm.duty_u16(position)
                time.sleep(.02)
    except:
        print("Something went wrong with servo")


def handleCommands(item, value):
    try:
        if "blink" == item:
            blink_onboard_led(int(value))
        if "led" == item:
            handleLed(value)
        if "servo" == item:
            handleServo(value)
        else:
            handleGP(item, value)
    except:
        print("Something went wrong")
