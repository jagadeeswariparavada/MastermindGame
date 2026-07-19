# 🎯 Mastermind Pro

A web-based number-guessing game built with Flask, styled with a twinkling star background, and celebrated with fireworks/confetti on a win.

## How to Play

1. Choose a difficulty:
   - Easy - guess a 3-digit number
   - Medium - guess a 4-digit number
   - Hard - guess a 5-digit number
2. You have 20 attempts to guess the secret number.
3. After each guess, you'll see green squares for correct positions and white squares for incorrect ones.
4. Guess correctly before your attempts run out to win - the fewer guesses used, the better your medal.

## Tech Stack

- Backend: Python, Flask
- Frontend: HTML, CSS, Jinja2 templating
- Effects: canvas-confetti for the win celebration

## Running Locally

pip install -r requirements.txt
python app.py

Then open http://127.0.0.1:5000 in your browser.

## Deployment

This app deploys on Render using:
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn app:app
- Environment Variable: SECRET_KEY (any random string)
