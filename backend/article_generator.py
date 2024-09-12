import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_article(text, keywords):
    prompt = f"""
    Generate a well-structured blog article based on the following text and SEO keywords:

    Text: {text[:1000]}...

    SEO Keywords: {', '.join(keywords)}

    The article should:
    1. Have an engaging title
    2. Include an introduction, main body, and conclusion
    3. Use subheadings to organize the content
    4. Naturally incorporate the SEO keywords
    5. Be around 800 words long

    Please format the article in HTML, using appropriate tags such as <h1> for the title, <h2> for subheadings, <p> for paragraphs, and <ul> or <ol> for lists if needed.
    """

    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates blog articles in HTML format."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        n=1,
        temperature=0.7,
    )
    
    article_html = response.choices[0].message.content.strip()
    
    # Wrap the entire article in a div for easier styling if needed
    return f"<div class='generated-article'>{article_html}</div>"