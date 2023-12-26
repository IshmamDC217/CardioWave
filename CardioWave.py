from machine import Pin, PWM, ADC
import time

# Set up the Buzzer and Potentiometer
potentiometer = ADC(Pin(27))
buzzer = PWM(Pin(13))

def heartbeat_signal(frequency, duration):
    """Generate a single heartbeat thump"""
    buzzer.freq(frequency)
    buzzer.duty_u16(32767)
    time.sleep(duration)
    buzzer.duty_u16(0)  # Turn off

while True:
    reading = potentiometer.read_u16()
    heartbeat_rate = reading // 6554 + 1  # Range of 1-10

    if reading == 0:
        buzzer.freq(2000) 
        buzzer.duty_u16(32767)
        print("Pulse:0")
        time.sleep(0.5)
    else:
        beat_duration = 0.1
        pause_between_beats = 0.1
        pause_between_heartbeats = max(0.2, 2.0 - heartbeat_rate * 0.2)

        heartbeat_signal(500, beat_duration)
        print("Pulse:1")
        time.sleep(pause_between_beats) 
        heartbeat_signal(500, beat_duration)
        print("Pulse:1")
        time.sleep(pause_between_heartbeats)

        print("Pulse:0")
