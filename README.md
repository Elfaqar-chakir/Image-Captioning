# Multilingual Image Captioning App

This repository contains a Python-based application for generating multilingual captions for images using advanced AI models like BLIP and VinVL. The application provides a user-friendly interface powered by Gradio.

## Features

- **Image Captioning Models**: Supports BLIP and VinVL models for generating captions.
- **Multilingual Support**: Captions can be translated into English, Arabic, or French.
- **User-Friendly Interface**: Enhanced web interface for easy interaction with the application.

## Code Structure

The project has been modularized into three main parts:

### 1. `main.py`
The entry point of the application. It initializes and launches the Gradio interface.

### 2. `interface.py`
Contains the Gradio-based web interface code. Handles user interactions, image uploads, and connects the interface to the caption generation functions.

### 3. `models.py`
Responsible for loading and managing all models and their associated logic. This includes:
- Loading BLIP and VinVL models.
- Handling caption generation logic.
- Translating captions into multiple languages using MarianMT models.

## Installation

1. **Download  the Repository**
   
   Download the repository manually and then navigate to the project folder in your terminal.

2. **Set Up a Virtual Environment**
   Ensure you have Python installed (version 3.8 or later). Then, set up a virtual environment:

   For Bash:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   For Windows Command Prompt:
   ```cmd
   virtual venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   With the virtual environment activated, install the required dependencies:

   For Bash:
   ```bash
   pip install -r requirements.txt
   ```

   For Windows Command Prompt:
   ```cmd
   pip install -r requirements.txt
   ```

4. **Download Pretrained Models**
   The necessary pretrained models are automatically downloaded 
   when the application is run for the first time.

## Usage

1. **Run the Application**

   For Bash:
   ```bash
   python main.py
   ```

   For Windows Command Prompt:
   ```cmd
   python main.py
   ```

2. **Access the Interface**
   Open the local server URL (displayed in the terminal) in your web browser to interact with the application.

3. **Generate Captions**
   - Upload an image.
   - Select the model (BLIP or VinVL).
   - Choose the language for the caption.
   - Click "Generate Caption" to view the output.

## File Overview

- `main.py`: Initializes the application.
- `interface.py`: Contains the Gradio interface.
- `models.py`: Manages all model-related logic and functions.
- `requirements.txt`: Lists all required Python libraries.

## Dependencies

- `Pillow`
- `transformers`
- `gradio`
- `torch`
- `pandas`
- `MarianMTModel` and `MarianTokenizer` for translation.

## Acknowledgments

This project utilizes models and libraries from:
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Gradio](https://gradio.app/)

