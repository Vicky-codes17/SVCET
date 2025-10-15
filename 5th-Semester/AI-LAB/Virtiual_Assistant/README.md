# Virtual Assistant

A Python-based virtual assistant that uses speech recognition and can answer questions using Wolfram Alpha and Wikipedia.

## Features

- Voice recognition using Google Speech Recognition
- Text-to-speech responses
- Query answering using Wolfram Alpha API
- Fallback to Wikipedia for general knowledge questions
- Voice commands to exit

## Prerequisites

### System Dependencies (Linux/Ubuntu)

```bash
sudo apt-get update
sudo apt-get install -y portaudio19-dev
```

### For other operating systems:
- **macOS**: `brew install portaudio`
- **Windows**: PyAudio wheels are available via pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vicky-codes17/SVCET.git
cd SVCET/5th-Semester/AI-LAB/Virtiual_Assistant
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Get your Wolfram Alpha API key from [Wolfram Alpha Developer Portal](https://products.wolframalpha.com/api/)
   - Add your API key to `.env`:
     ```
     WOLFRAM_APP_ID=your_actual_api_key_here
     ```

## Usage

Run the virtual assistant:
```bash
python virtiual_assistant.py
```

### Voice Commands

- Ask any question and the assistant will try to answer using Wolfram Alpha or Wikipedia
- Say "exit" or "stop" to quit the program

## Dependencies

- `wikipedia` - For Wikipedia search functionality
- `wolframalpha` - For Wolfram Alpha API integration
- `SpeechRecognition` - For voice recognition
- `pyttsx3` - For text-to-speech
- `pyaudio` - For audio input
- `python-dotenv` - For environment variable management

## Configuration

The assistant can be configured by modifying the following parameters in `virtiual_assistant.py`:

- Speech rate: Adjust `engine.setProperty("rate", 150)` value (default: 150)
- Wikipedia summary length: Modify `sentences=2` in the `wikipedia.summary()` call

## Troubleshooting

### PyAudio Installation Issues

If you encounter issues installing PyAudio, make sure you have the PortAudio development headers installed:

**Linux/Ubuntu:**
```bash
sudo apt-get install portaudio19-dev
```

**macOS:**
```bash
brew install portaudio
```

### Microphone Access

Ensure your system has a working microphone and that the application has permission to access it.

## Security Note

**Never commit your `.env` file to version control!** It contains your API keys. The `.env.example` file is provided as a template.

## License

This project is for educational purposes.
