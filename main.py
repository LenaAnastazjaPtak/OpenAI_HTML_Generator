from openai import OpenAI
import os
from dotenv import load_dotenv

def read_article(file_path):
    """Read the content of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return ""
    
def save_html(file_path, html_content):
    """Save the generated HTML content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"File generated: {file_path}")
    
def get_openai_client():
    """Initialize and return the OpenAI client."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key is missing. Ensure it is set in the .env file.")
    return OpenAI(api_key=api_key)

def generate(prompt, client):
    """Send a prompt to OpenAI and retrieve the generated text."""
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4"
    )
    return response.choices[0].message.content

def main():
    client = get_openai_client()
    article_text = read_article("article.txt")

    # Define prompts for different stages
    html_template_prompt = (
        "Wygeneruj szablon HTML z pustym <body>.\n" 
        "Jego tytuł to 'Szablon'\n" 
        "Nie wyświetlaj tego jako kod HTML, tylko jako tekst."
    )

    html_content_prompt = (
        "Przygotuj kod dla artykułu zgodnie z następującymi wytycznymi:\n"
        "1. Użyj odpowiednich tagów HTML do strukturyzacji treści.\n"
        "2. W miejscach, gdzie warto umieścić grafikę, użyj tagu <img> z atrybutem src=\"image_placeholder.jpg\".\n"
        "3. Dodaj atrybut alt do każdego obrazka z dokładnym promptem do wygenerowania grafiki.\n"
        "4. Umieść podpisy pod grafikami za pomocą odpowiedniego tagu HTML.\n"
        "5. Wygeneruj wyłącznie zawartość, którą można umieścić między <body> i </body>, bez użycia znaczników <html>, <head> czy <body>.\n"
        "6. Nie wyświetlaj tego jako kod HTML, tylko jako tekst.\n"
        "Artykuł:\n" + article_text
    )

    # Generate and save template, article HTML, and preview
    html_template = generate(html_template_prompt, client)
    save_html("szablon.html", html_template)

    html_content = generate(html_content_prompt, client)
    save_html("artykul.html", html_content)

    # Combine template and content for a full preview
    html_preview_prompt = (
        "Wstaw tekst '" + html_content + "' w znaczniki <body> w tekście '" + html_template + "'. \n"
        "Bez komentarza.\n" 
        "Nie wyświetlaj tego jako kod HTML, tylko jako tekst.\n"
    )

    html_preview = generate(html_preview_prompt, client)
    save_html("podglad.html", html_preview)

if __name__ == "__main__":
    main()
