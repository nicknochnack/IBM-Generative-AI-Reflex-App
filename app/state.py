# Import reflex
import reflex as rx

# Import IBM Gen 
from genai.model import Credentials
from genai.schemas import GenerateParams 
from genai.model import Model 

# Get reflex config
config = rx.config.get_config()
# Set your APIKEY
APIKEY = config.watsonx_api_key
# Define credentials 
creds = Credentials(APIKEY, api_endpoint=config.watsonx_api_endpoint)
# Define generation parameters 
params = GenerateParams(decoding_method="sample",
                        max_new_tokens=40,
                        min_new_tokens=30,
                        stream=True,
                        temperature=0.9,
                        top_k=100,
                        top_p=0.3, 
                        repetition_penalty=2.0)

llm = Model(config.watsonx_model, params=params, credentials=creds)

class State(rx.State):
    """The app state."""
    question: str = ""
    chat_history: list[tuple[str,str]]

    async def answer(self): 
        answer = ""
        self.chat_history.append((self.question, answer))
        for response in llm.generate_stream([self.question]):
            if hasattr(response, "generated_text"):
                if response.generated_text != None:
                    answer += response.generated_text
                    self.chat_history[-1] = (self.question, answer)
                    yield 