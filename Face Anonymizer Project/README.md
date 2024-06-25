# Face Anonymizer Using OpenCV and MediaPipe

## Overview
This project demonstrates how to anonymize faces in video streams using computer vision techniques. By detecting faces with MediaPipe and applying Gaussian blur using OpenCV, this tool can obscure faces in real-time or pre-recorded videos, protecting privacy effectively.


## Features
- **Real-Time Face Detection**: Utilizes MediaPipe's efficient face detection to identify faces in each video frame.
- **Face Anonymization**: Applies Gaussian blur to the detected face regions to obscure identities.
- **Versatile Input**: Can process both live video from a webcam and pre-recorded video files.
- **Customizable**: Allows easy adjustments to blur strength and detection parameters.

## Technologies Used
- **Python**: Primary programming language.
- **OpenCV**: For video capture, processing, and display.
- **MediaPipe**: For face detection capabilities.

## Installation

### Prerequisites
- Python 3.6+
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)

### Install Dependencies
Use pip to install the required libraries:

```bash
pip install opencv-python mediapipe
