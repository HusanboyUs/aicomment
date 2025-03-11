import subprocess
from generator import Generator

apikey:str = ""

try:
    get_changes = subprocess.run("git","diff","HEAD",capture_output=True, text=True)
except Exception as e:
    raise e

generator = Generator(apiKey=apikey)
generator.generate_text_prompt(
    prompt=f"Generate me a meaningfull commit message and description using past tense and passive voice based on these changes: {get_changes} and dont make mistake and be speceif and use easy to understand words")

