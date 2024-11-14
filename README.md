# oxido
The application generates HTML code for an article based on the provided text. It uses the OpenAI API to process the text and generate properly formatted HTML code, which includes placeholders for images and captions underneath them. The generated HTML code is saved in an article.html file.

To run the application, follow these steps:

1. Make sure you have Python installed on your system.
2. Navigate to the directory where the `main.py` file is located.
3. Create `.env` file with:
    ```
    API_KEY =  'your_api_key'
    ```
4. Run the following commands to start the application:
    ```
    pip install -r requirements.txt
    ```

    ```
    python main.py
    ```
5. Open `artykul.html` and copy content.
6. Duplicate `szablon.html` and paste content between <body> tags.
7. Open duplicated `szablon.html` with any browser.

Thank you!
