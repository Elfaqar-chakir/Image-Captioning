# interface.py
import gradio as gr
from models import generate_caption

def create_interface():
    with gr.Blocks(css="""
        body {
            font-family: 'Arial', sans-serif;
            background-color: #121212;
            color: #f5f5f5;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #FFA500;
        }
        .gr-button {
            background-color: #FFA500;
            color: #121212;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        .gr-button:hover {
            background-color: #ffb347;
        }
        .gr-input {
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #FFA500;
        }
    """) as demo:

        # Title section
        with gr.Row():
            gr.Markdown(
                """
                <div class="container">
                    <h1>Multilingual Image Captioning App</h1>
                    <p style="text-align: center; font-size: 18px;">Generate captions for your images using BLIP or VinVL models in English, Arabic, or French.</p>
                </div>
                """
            )

        # Image upload and options
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown(
                    """
                    <div class="container">
                        <h2>Select Model</h2>
                    </div>
                    """
                )
                model_dropdown = gr.Dropdown(
                    label="Select Model", 
                    choices=["BLIP", "VinVL"], 
                    value="BLIP"
                )

                language_dropdown = gr.Dropdown(
                    label="Select Language", 
                    choices=["English", "Arabic", "French", "Spanish", "German"], 
                    value="English"
                )


            with gr.Column(scale=2):
                gr.Markdown(
                    """
                    <div class="container">
                        <h2>Upload Your Image</h2>
                    </div>
                    """
                )
                image_input = gr.Image(label="Upload Image", type="numpy")

                generate_button = gr.Button("Generate Caption")
                caption_output = gr.Text(label="Generated Caption", lines=3)

        # Footer
        with gr.Row():
            gr.Markdown(
                """
                <div class="footer">
                    <p>Created by</p>
                    <p>BENLAHCEN Souad & ELFAQAR Chakir</p>
                </div>
                """
            )

        # Connect button to function
        generate_button.click(fn=generate_caption, inputs=[image_input, model_dropdown, language_dropdown], outputs=caption_output)

    return demo

