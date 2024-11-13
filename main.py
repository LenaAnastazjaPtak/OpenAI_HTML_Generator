from openai import OpenAI
import os
from dotenv import load_dotenv

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def generate(prompt):
    load_dotenv()
    client = OpenAI(
        api_key = os.getenv("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": prompt,
        }
        ],
        model="gpt-4o",
    )

    return chat_completion.choices[0].message.content

def save_html(file_path, html_content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print("Wygenerowano plik: ", file_path)

def main():
    article_text = read_article("article.txt")

    html_template_prompt = ("Wygeneruj szablon HTML z pustym <body>. Nie wyświetlaj tego jako kod HTML tylko jako tekst.")

    html_content_prompt = (
        "Przygotuj kod dla artykułu zgodnie z następującymi wytycznymi:\n"
        "1. Użyj odpowiednich tagów HTML do strukturyzacji treści.\n"
        "2. W miejscach, gdzie warto umieścić grafikę, użyj tagu <img> z atrybutem src=\"image_placeholder.jpg\".\n"
        "3. Dodaj atrybut alt do każdego obrazka z dokładnym promptem do wygenerowania grafiki.\n"
        "4. Umieść podpisy pod grafikami za pomocą odpowiedniego tagu HTML.\n"
        "5. Wygeneruj wyłącznie zawartość, którą można umieścić między <body> i </body>, bez użycia znaczników <html>, <head> czy <body>.\n\n"
        "6. Nie wyświetlaj tego jako kod HTML tylko jako tekst.\n"
        "Artykuł:\n" + article_text
    )

    html_template = generate(html_template_prompt)
    save_html("szablon.html", html_template)

    html_content = generate(html_content_prompt)
    save_html("artykul.html", html_content)

if __name__ == "__main__":
    main()
