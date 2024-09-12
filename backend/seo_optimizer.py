import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_seo_keywords(text):
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates SEO keywords."},
            {"role": "user", "content": f"Generate 5 SEO keywords for the following text:\n\n{text[:1000]}..."}
        ],
        max_tokens=50,
        n=1,
        temperature=0.5,
    )
    
    keywords = response.choices[0].message.content.strip().split('\n')
    return [keyword.strip() for keyword in keywords if keyword.strip()]