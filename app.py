import os
import streamlit as st
import json
from pathlib import Path
from dotenv import load_dotenv
from utils.elevenlabs_api import ElevenLabsAPI
from utils.script_parser import ScriptParser

# Load environment variables
load_dotenv()

# Initialize API and parser
api = ElevenLabsAPI()
parser = ScriptParser()

def load_voices():
    """Load or fetch available voices"""
    if not os.path.exists("voices.json"):
        st.info("Fetching available voices...")
        voices = api.save_voices_to_json()
        st.success("Voices fetched and saved!")
    else:
        with open("voices.json", 'r') as f:
            voices = json.load(f)
    return voices

def main():
    st.title("Voiceover Generator")
    
    # Sidebar for voice assignments
    st.sidebar.title("Voice Settings")
    
    # Load available voices
    voices = load_voices()
    voice_options = {voice["name"]: voice["voice_id"] for voice in voices}
    
    # File upload
    uploaded_file = st.file_uploader("Upload your script file", type=['txt'])
    
    if uploaded_file:
        content = uploaded_file.getvalue().decode()
        
        # Parse the script
        script_lines = parser.parse_script(content)
        
        # Get unique characters
        characters = list(set(char for char, _ in script_lines))
        
        # Voice assignment
        st.sidebar.subheader("Assign Voices to Characters")
        character_voices = {}
        for character in characters:
            voice_id = st.sidebar.selectbox(
                f"Voice for {character}",
                options=list(voice_options.keys()),
                key=character
            )
            character_voices[character] = voice_options[voice_id]
        
        # Generate button
        if st.button("Generate Voiceovers"):
            output_dir = Path("output")
            output_dir.mkdir(exist_ok=True)
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for idx, (character, text) in enumerate(script_lines):
                status_text.text(f"Generating audio for {character}...")
                output_file = output_dir / f"{idx+1:03d}_{character}.mp3"
                
                try:
                    api.generate_audio(
                        text=text,
                        voice_id=character_voices[character],
                        output_file=str(output_file)
                    )
                    progress_bar.progress((idx + 1) / len(script_lines))
                except Exception as e:
                    st.error(f"Error generating audio for {character}: {str(e)}")
                    return
            
            status_text.text("All audio files generated successfully!")
            st.success(f"Generated {len(script_lines)} audio files in the 'output' directory")

if __name__ == "__main__":
    main()
