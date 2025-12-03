# MicroPython_Pong
Pong written in MicroPython

This project was written in an attempt to become more familiar with Python in a (hopefully) fun way.

It has undergone several changes as I have written it. Unfortunately, most of the changes were done without source code control.

## Hardware:

This project utilizes the following hardware:
- WeMos D1 R32 with an ESP32 microcontroller. Any board with an ESP32 microcontroller can be used. Other boards capable of running MicroPython should be compatible
(ESP8266, RP2040, etc.), but the code may require minor modification.
- OLED display module with a resolution of 132 x 64 (I think it is 0.96")
- Analog joystick (PS2 style)
- Breadboard to connect the components together. If the components are soldered together, the breadboard won't be needed.

## Files:

- pong.py - the main program
- paddle.py - handles a paddle
- computerPaddle.py - handles a computer paddle, a subclass of paddle.py
- ball.py - handles moving the ball
- joystick.py - handles processing joystick movement
- oled_joystick.py - the original main program. It was renamed to pong.py to make the name more appropriate.
