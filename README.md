# Voiceover Generator

A Streamlit-based application that converts script files into voiceovers using the ElevenLabs API. The application allows you to assign different voices to characters in your script and automatically generates audio files for each dialogue line.

## Features

- Upload script files with character and dialogue markup
- Automatic character detection from script
- Voice assignment interface for each character
- Batch generation of audio files
- Progress tracking during generation
- Organized output with numbered audio files

## Requirements

- Python 3.6+
- Streamlit
- Requests
- python-dotenv
- ElevenLabs API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/voiceover-generator.git
cd voiceover-generator
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file from the template:
```bash
cp .env.template .env
```

4. Add your ElevenLabs API key to the `.env` file:
```
ELEVENLABS_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Upload a script file in the required format (see below)
3. Assign voices to each character using the sidebar
4. Click "Generate Voiceovers" to create audio files
5. Find the generated audio files in the `output` directory

## Script Format

Scripts should be formatted using XML-style tags for characters and dialogue. Example:

```xml
<character>John</character>
<dialogue>Hello there! How are you doing today?</dialogue>

<character>Sarah</character>
<dialogue>I'm doing great, thanks for asking! How about you?</dialogue>

<character>John</character>
<dialogue>I'm fantastic! The weather is perfect for a walk in the park.</dialogue>

<character>Sarah</character>
<dialogue>You're right! We should definitely enjoy this beautiful day.</dialogue>
```

## Output

Generated audio files will be saved in the `output` directory with the following naming convention:
```
001_Character.mp3
002_Character.mp3
...
```

## License

This project is licensed under the terms of the LICENSE file included in the repository.
