# Voice-Controlled YouTube Player

A Python-based voice assistant that listens for commands like "Play [song name]" or "Put on [song name]" and plays the top YouTube result using speech recognition and TTS (Text-To-Speech).

## Features

- Voice command recognition using microphone input
- Parses commands like "Play Kulosa" or "Put on Believer"
- Fetches the top video from YouTube using `youtube-search-python`
- Opens the video in the default web browser
- Provides audio feedback using TTS (Text-To-Speech)

## Project Structure

```
.
├── main.py                  # Entry point
├── command_router.py       # Routes voice commands to specific actions
├── recognizer.py           # Captures and transcribes audio input
├── tts_engine.py           # Text-to-speech feedback
├── utils.py                # Utility functions for command processing
├── web_access.py           # Handles YouTube search and browser opening
├── requirements.txt        # Required Python packages
```

## Installation

1. Clone the repository or download the files.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

> **Note:** Ensure `PyAudio` is correctly installed. On Linux, you might need:
> ```bash
> sudo apt-get install portaudio19-dev python3-pyaudio
> ```

3. Make sure your microphone is connected and working.

## Usage

Run the main program:

```bash
python main.py
```

Speak a command like:

- `Play Shape of You`
- `Put on Believer`

The assistant will search YouTube and play the top result.

## Requirements

- Python 3.8+
- Working microphone and internet connection

## Dependencies

- SpeechRecognition
- PyAudio
- pyttsx3
- youtube-search-python
- requests
- webbrowser (standard library)

## License

This project is for educational use only.