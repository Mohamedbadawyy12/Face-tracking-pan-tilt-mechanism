# Face Tracking with Pan-Tilt Mechanism

This project implements real-time face tracking using OpenCV, Haar Cascade, and an Arduino-based pan-tilt mechanism. It tracks a user's face in a webcam feed and adjusts the pan-tilt mechanism to keep the face centered.

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)


## Introduction

The project aims to create an interactive face tracking system. It detects a user's face in real-time using OpenCV's Haar Cascade classifier and adjusts a pan-tilt mechanism (controlled by an Arduino) to keep the face centered within the frame. This project can be used for various applications, such as surveillance, human-computer interaction, or robotics.

## Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier
- Arduino
- Serial Communication

## Project Structure

The project consists of two main components:

1. **Python Code (`face_tracking.py`):**
   - Captures video from a webcam.
   - Detects and tracks faces using the Haar Cascade classifier.
   - Calculates the error in face position and sends control signals to the Arduino via serial communication to adjust the pan-tilt mechanism.

2. **Arduino Code (`pan_tilt_control.ino`):**
   - Receives serial data from the Python script.
   - Controls two servo motors (pan and tilt) to adjust the camera's orientation based on the received error values.

3. **SolidWorks Design for Pan-Tilt Mechanism:**
   - A SolidWorks design has been created for the pan-tilt mechanism. You can find the design files in the `solidworks` directory.

## Setup

### Python Setup
1. Install Python on your system if not already installed.
2. Install the required Python packages using `pip`:


### Arduino Setup
1. Upload the `pan_tilt_control.ino` code to your Arduino board, which controls the servo motors.
2. Connect the servo motors to the appropriate pins on your Arduino and provide power as needed.

## Usage

1. Connect your Arduino to your computer via USB.
2. Run the Python script `face_tracking.py`.
3. The webcam will start capturing video, and the face tracking will begin.
4. The pan-tilt mechanism will adjust its orientation to keep the detected face centered.


