import subprocess
from generator import Generator

apikey:str = ""

try:
    result = subprocess.run(["git", "diff","HEAD"], capture_output=True, text=True)
    print(result.stdout)

except Exception as e:
    raise e

generator = Generator(apiKey=apikey)
res = generator.generate_text_prompt(
    prompt=f"Generate me a meaningfull commit message and description using past tense and passive voice based on these changes: {result.stdout} and dont make mistake and be specefic and use easy to understand words")
print(res.text)