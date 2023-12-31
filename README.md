# CardioWave Heartbeat Simulator 💓🔊

## Introduction 🌟
The CardioWave Heartbeat Simulator is an innovative project that intricately blends biology with technology. It aims to simulate the human heart's rhythm using a potentiometer to control a buzzer, creating a range of heartbeat sounds. From a calm, steady pulse to a rapid heartbeat, this project captures the essence of our vital life force in an electronic form. Ideal for educational purposes, the CardioWave offers a unique hands-on experience for understanding heart rates and their variability.

### Components 🛠️
- Microcontroller (e.g., Raspberry Pi Pico)
- Buzzer (PWM compatible)
- Potentiometer (10k ohm)
- Breadboard and connecting wires

## Script Explanation 📝
The Python script for the CardioWave project is designed for microcontrollers like the Raspberry Pi Pico, making use of the `machine` library for Analog-to-Digital Conversion (ADC) and Pulse Width Modulation (PWM) control.

### Key Functions 🗝️
- `heartbeat_signal(frequency, duration)`: Generates a heartbeat sound with a specified frequency and duration.
- `continuous_beep(frequency)`: Emits a continuous high-frequency beep, simulating a flatline.
- `while True` Loop: Continuously reads the potentiometer value to adjust the heartbeat frequency or trigger a flatline simulation.

### Behavior 🚦
- **Potentiometer at 0**: Triggers a continuous high-frequency beep, representing a flatline.
- **Potentiometer above 0**: Generates heartbeat sounds with frequency proportional to the potentiometer's value.

## Demonstration Video 🎥
A comprehensive demonstration of the CardioWave Heartbeat Simulator is available in the attached video, "CardioWave Sim." This video showcases the functionality of the project, providing viewers with a clear understanding of its capabilities.
