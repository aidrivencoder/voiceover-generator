import os
import json
import requests
from typing import Dict, List

class ElevenLabsAPI:
    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        self.base_url = "https://api.elevenlabs.io/v1"
        
    def get_voices(self) -> List[Dict]:
        """Retrieve available voices from ElevenLabs API"""
        headers = {
            "Accept": "application/json",
            "xi-api-key": self.api_key
        }
        
        response = requests.get(
            f"{self.base_url}/voices",
            headers=headers
        )
        
        if response.status_code == 200:
            return response.json()["voices"]
        else:
            raise Exception(f"Failed to get voices: {response.text}")
    
    def save_voices_to_json(self, output_file: str = "voices.json"):
        """Retrieve and save available voices to a JSON file"""
        voices = self.get_voices()
        with open(output_file, 'w') as f:
            json.dump(voices, f, indent=2)
        return voices
    
    def generate_audio(self, text: str, voice_id: str, output_file: str):
        """Generate audio using specified voice"""
        headers = {
            "Accept": "application/json",
            "xi-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        
        response = requests.post(
            f"{self.base_url}/text-to-speech/{voice_id}",
            json=data,
            headers=headers
        )
        
        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)
        else:
            raise Exception(f"Failed to generate audio: {response.text}")
