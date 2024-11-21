<a id="readme-top"></a>


# FACE-TRACKING-SYSTEM
## Explanatory Video for Sign Language Interpreter
https://github.com/user-attachments/assets/901dd5f5-8022-4d5f-8ac7-d1c9b0e93efd



## Index: 
- [About The Project](#About-The-Project)
- [Requirements](#Requirements)
- [Steps to Implement](#Steps-to-Implement)
- [Applications](#Applications)





  
## About The Project
This face-tracing application combines computer vision and robotics to dynamically track a person's face. It utilizes a webcam to detect and follow facial movements in real-time, adjusting the position of two servo motors mounted on an Arduino board. The motors, controlling the X-axis and Y-axis, align the camera with the face. By leveraging OpenCV for face detection and Mediapipe for precise movement tracking, the application ensures seamless face alignment. Using the Firmata protocol, the servo motors receive angle adjustments from Python code based on detected face coordinates.

This project demonstrates the integration of computer vision and robotics, with applications in security, surveillance, and military systems. Its ability to continuously track and focus on a face showcases the potential of such systems in enhancing interactive technologies for real-world use.

# Requirements:
1. Hardware:
      * Arduino board (e.g., Uno or Mega)
      * 2 servo motors
      * USB cable for Arduino
      * Jumper wires and breadboard
      * Camera (e.g., a webcam)
2. Software:
     * Python
     * Arduino IDE


# Steps to Implement: 

1. Setup Arduino and Servo Motors:
     * Connect the X-axis servo to one pin (e.g., Pin 9) and the Y-axis servo to another pin (e.g., Pin 10).
     * Power the servos through the Arduino board.
  
2. Arduino Code:
   Use the Firmata protocol for communication. Upload the "StandardFirmata" sketch from the Arduino IDE:
     * Open Arduino IDE > File > Examples > Firmata > StandardFirmata.
     * Select your board and port.
     * Upload the code.
  
3.  Python Code:
     * Use OpenCV for detecting faces and Mediapipe for tracking face movement.
     * Control servo angles based on face position.
    
 
Required libraries to run this project:
```bash
pip install cvzone numpy mediapipe pyfirmata opencv-python

```

# Applications:
1. Military and Security:
    * Automated tracking systems for monitoring intruders or potential threats.
    * Integration with weapon systems for precise targeting.
2. Surveillance:
    * Face tracking for camera systems to ensure the subject remains centered.
3. Robotics:
    * Building human-interactive robots that follow users. :smile:
   

<p align="center">(<a href="#readme-top">back to top</a>)</p>
