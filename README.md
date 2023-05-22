# ISS_Satellite_Notifier

A Python application that notifies you if the International Space Station (ISS) is passing near your location during the night time.

## Description

This application retrieves the current location of the ISS and compares it with your specified location. If the ISS is within a certain range of your location and it is currently night time, you will receive a notification via email.

## Features

- Retrieves real-time data of the ISS location
- Calculates sunrise and sunset times for your location
- Notifies you if the ISS is passing near your location during the night time

## Technologies Used

- Python
- Requests library for making HTTP requests
- Datetime library for working with dates and times
- smtplib library for sending email notifications

## Installation

1. Clone the repository: git clone https://github.com/YourUsername/ISS_Satellite_Notifier.git
2. Install the required libraries: pip install requests

## Usage
1. Open the main.py file.
2. Modify the following variables with your own values:
  - MY_EMAIL: Your email address for sending notifications.
  - APP_PASSWORD: The application-specific password for your email account.
  - MY_LAT: Your latitude coordinate.
  - MY_LNG: Your longitude coordinate.
3. Run the script: python main.py
4. Keep the script running in the background to receive notifications when the ISS is passing near your location during the night time.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

The project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course on Udemy by Dr. Angela Yu.

