from google import genai
from google.genai import types


__all__ = ["Generator"]


class Generator:
    """Generator class which communicates with model in given parameters"""

    def __init__(self, apiKey:str, modelName:str = "gemini-2.0-flash-001"):
        self.apiKey = apiKey
        self._modelName = modelName
        self.client = genai.Client(api_key=self.apiKey)
        self._config = {
            "temperature":0,
            "top_p":0.95,
            "top_k":20,
            "candidate_count":1,
            "seed":5,
            "max_output_tokens":100,
            "stop_sequences":["STOP!"],
            "presence_penalty":0.0,
            "frequency_penalty":0.0,
        }
    
    @property
    def model(self):
        return self._modelName
    
    @model.setter
    def model(self,new_model_name):
        self._modelName = new_model_name

    @property
    def config(self):
        return self._config
    
    @config.setter
    def config(self, value:str):
        values = value.split()
        if values[0] in self.config.keys():
            self.config[values[0]] = int(values[1])
        else:
            raise KeyError(f"{values[0]} is not valid key-name in config dictionary")

    def generate_text_prompt(self, prompt:str):
        try:
            response = self.client.models.generate_content(
                model=self._modelName,
                contents=types.Part.from_text(
                    text=prompt
                ),
                config=types.GenerateContentConfig(
                    temperature=self.config["temperature"],
                    top_p=self.config["top_p"],
                    top_k=self.config["top_k"],
                    candidate_count=self.config["candidate_count"],
                    seed=self.config["seed"],
                    max_output_tokens=self.config["max_output_tokens"],
                    stop_sequences=self.config["stop_sequences"],
                    presence_penalty=self.config["presence_penalty"],
                    frequency_penalty=self.config["frequency_penalty"],
                    safety_settings= [
                        types.SafetySetting(
                            category="HARM_CATEGORY_HATE_SPEECH",
                            threshold="BLOCK_ONLY_HIGH"
                        )
                    ]
                )
            )
            return response
        
        except Exception as e:
            raise e


    def __repr__(self):
        return f"{self._modelName}{__class__.__name__}"
    
    def __str__(self):
        return f"{__class__.__name__}"
       
