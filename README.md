# OpenAI HTML Generator

A Python application that transforms text-based articles into structured HTML using the OpenAI API. This application generates an HTML structure from the article content, adds designated placeholder images with descriptive prompts, and includes captions, making it easy to enhance the document with images and prepare it for the web. Additionally, it generates an HTML template for article previews. The <body> section is left empty and ready for the article content. This empty template is saved as szablon.html, while a full preview of the article is saved as podglad.html.

## Features

- **Structured HTML Output**: Automatically organizes article content using appropriate HTML tags for a clean, accessible layout.
- **Image Placeholders**: Inserts `<img>` tags in strategic locations within the article with `src="image_placeholder.jpg"` and descriptive `alt` attributes to suggest suitable images.
- **Captions for Images**: Adds HTML captions under each placeholder image, allowing easy customization and addition of visuals.
- **Streamlined Output**: The generated HTML contains only the content between `<body>` tags, making it easy to integrate into existing web templates.
- **HTML Template and Preview Generation**: Creates an HTML template (`szablon.html`) with an empty `<body>` section, ready for article insertion, and generates a complete preview (`podglad.html`) for visualization.

## Prerequisites

- Python 3.x
- OpenAI API key
- Git

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd OpenAI_HTML_Generator
   ```

2. **Install Dependencies:** Install required Python packages:
   ```bash
    pip install openai python-dotenv
    ```

3. **Set Up API Key:** Create a `.env`file in the project root and add your OpenAI API key:
   ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Add Your Article:** Add your article content to `article.txt` in the project directory:


## Usage

Run the application using the following command:
```bash
python main.py
```

The HTML output will be saved as `artykul.html`, ready to be used in a web project.