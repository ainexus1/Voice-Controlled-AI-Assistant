# Jarvis Voice Assistant

Jarvis Voice Assistant is a simple Python voice-controlled assistant that can perform various tasks based on voice commands. It utilizes text-to-speech (TTS) and speech recognition to interact with the user.

## Features

- **Time and Date:** Get the current time and date.
- **Wikipedia Search:** Search and retrieve information from Wikipedia.
- **Send Email:** Send emails using your Gmail account.
- **Search in Chrome:** Open a search query in Google Chrome.
- **System Commands:** Log out, shut down, or restart the computer.
- **Play Songs:** Play songs from a specified directory.
- **Remember Command:** Save and retrieve user reminders.
- **Take Screenshots:** Capture and save screenshots.
- **CPU Usage:** Check CPU usage and battery percentage.

## How to Use

1. **Install Dependencies:**
   ```bash
   pip install pyttsx3 SpeechRecognition wikipedia smtplib pyautogui psutil


2. **Configure Email:**
   - Update the `sendemail` function with your Gmail credentials and recipient's email.

3. **Run the Code:**
   ```bash
   python jarvis_voice_assistant.py
   ```

4. **Voice Commands:**
   - Trigger Jarvis by saying "Jarvis" or "Hey Jarvis," followed by your command.

## Libraries Used

- `pyttsx3`: Text-to-speech library for voice output.
- `SpeechRecognition`: Library for recognizing speech input.
- `wikipedia`: Access Wikipedia articles and summaries.
- `smtplib`: Simple Mail Transfer Protocol for sending emails.
- `pyautogui`: GUI automation library for taking screenshots.
- `psutil`: Provides information on system utilization.

Feel free to contribute, report issues, or suggest improvements. Happy coding!
