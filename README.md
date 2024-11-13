# OpenAI HTML Generator

A Python application that transforms text-based articles into structured HTML using the OpenAI API. This application generates an HTML structure from the article content, adds designated placeholder images with descriptive prompts, and includes captions, making it easy to enhance the document with images and prepare it for the web.

## Features

- **Structured HTML Output**: Automatically organizes article content using appropriate HTML tags for a clean, accessible layout.
- **Image Placeholders**: Inserts `<img>` tags in strategic locations within the article with `src="image_placeholder.jpg"` and descriptive `alt` attributes to suggest suitable images.
- **Captions for Images**: Adds HTML captions under each placeholder image, allowing easy customization and addition of visuals.
- **Streamlined Output**: The generated HTML contains only the content between `<body>` tags, making it easy to integrate into existing web templates.

## How It Works

1. **Read the Article**: The application reads article content from a text file (`article.txt`).
2. **Send to OpenAI**: It sends the article text to the OpenAI API with a prompt to generate an HTML structure, including placeholders for images.
3. **Generate HTML**: OpenAI responds with an HTML structure, which is then saved as `artykul.html`.
4. **Placeholder Images**: The generated HTML includes `<img>` tags with `src="image_placeholder.jpg"` and `alt` attributes describing the intended image, making it easy to replace with actual visuals.

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