import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


with open("article.txt", "r") as file:
    article_text = file.read()

prompt = """
Generate HTML code for the article with the following guidelines:
- Use appropriate HTML tags to structure the content.
- Indicate places where images should be inserted using the <img> tag with the attribute src="image_placeholder.jpg". Add an alt attribute to each image with a detailed prompt that we can use to generate the image.
- Place captions under images using the appropriate HTML tag.
- No CSS or JavaScript. The returned code should only contain content to be inserted between <body> and </body> tags. Do not include <html>, <head>, or <body> tags.
"""

print(os.getenv("API_KEY"))
client = OpenAI(
    api_key=os.getenv("API_KEY"), 
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt + "\n\n" + article_text,
        }
    ],
    model="gpt-4o",
)

html_content = response.choices[0]

with open("artykul.html", "w") as file:
    file.write(html_content.message.content)