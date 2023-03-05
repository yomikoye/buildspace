import os  
import openai 
from dotenv import load_dotenv 

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    chat_response = to_yoruba(
                                "Life in Lagos can be quite crazy. Different kinds of individuals with different mentalities and temperaments just make it crazier. You don’t want to be too gentle or calm in Lagos, a little display of craziness is sometimes needed."
    )  
    print(chat_response.choices[0].message)
    
def to_yoruba(text):
    prompt = []
    system_role = {
        "role": "system",
        "content": "You are ChatGPT, a large language model trained by OpenAI and a helpful assistant that translates English to Yoruba."
        }
    prompt.append(system_role)
    
    user_role = {
        "role": "user",
        "content": f"Translate the following English text to Yoruba: {text}"
    }
    prompt.append(user_role)
    print(prompt[1]["content"])
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
    )

    return response

if __name__ == "__main__":
    main()
