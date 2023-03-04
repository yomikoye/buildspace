import os  
import openai 
from fastapi import FastAPI
from dotenv import load_dotenv # type: ignore 

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = "tell me a random fact."
response = openai.Completion.create( 
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=100,
    top_p=1,
)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the ChatGPT fact app. Visit /facts to get a random fact!"}


@app.get("/fact")
async def prompt():
    return {"random_fact": response.choices[0].text.strip()}