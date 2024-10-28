import re
from typing import List, Dict, Tuple

class ScriptParser:
    def parse_script(self, content: str) -> List[Tuple[str, str]]:
        """
        Parse the script content and return a list of (character, text) tuples
        
        Example format:
        <character>John</character>
        <dialogue>Hello, how are you?</dialogue>
        """
        lines = []
        content = content.strip()
        
        # Find all character-dialogue pairs
        pattern = r'<character>(.*?)</character>\s*<dialogue>(.*?)</dialogue>'
        matches = re.finditer(pattern, content, re.DOTALL)
        
        for match in matches:
            character = match.group(1).strip()
            dialogue = match.group(2).strip()
            lines.append((character, dialogue))
            
        return lines
