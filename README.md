

# Jules' Welcome Party Web App

This project is a Flask web application for Jules' Welcome Party.

## Overview

- Python web app (Flask)
- Main files:
  - `app.py`: Application code
  - `templates/index.html`: HTML template
  - `requirements.txt`: Python dependencies
  - `Dockerfile`: Containerization setup

## Local Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the app:
   ```
   python app.py
   ```


## Docker Usage

1. Build the Docker image:
   ```
   docker build -t my_flask_app .
   ```
2. Run the container:
   ```
   docker run --name my_flask_app_container -p 5000:5000 -p 4040:4040 my_flask_app
   ```


## Exposing the App to the Internet with ngrok

ngrok is installed in the container. To expose your app:

1. (Optional) Set your ngrok auth token (once):
   ```
   docker exec -it my_flask_app_container ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```
2. Start ngrok inside the running container:
   ```
   docker exec -it my_flask_app_container ngrok http 5000
   ```
3. Copy the public URL shown by ngrok (e.g., `https://xxxx.ngrok.io`) and share it to access your app from anywhere.

## Dependencies

- Flask

## Notes
- Update `requirements.txt` if you add more dependencies.
- For documentation, see this README.
