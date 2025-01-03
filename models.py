# functionality

from PIL import Image
from transformers import (
    BlipProcessor, 
    BlipForConditionalGeneration, 
    VisionEncoderDecoderModel, 
    ViTImageProcessor, 
    AutoTokenizer, 
    MarianMTModel, 
    MarianTokenizer
)
import logging
logging.getLogger("transformers").setLevel(logging.ERROR)

# Load BLIP model and processor
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load VinVL model and processor
vinvl_model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
vinvl_feature_processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
vinvl_tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# Load MarianMT models for translation
translator_models = {
    "Arabic": {
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-ar"),
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ar"),
    },
    "French": {
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-fr"),
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr"),
    },
    "Spanish": {
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-es"),
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es"),
    },
    "German": {
        "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-de"),
        "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de"),
    },
}

def translate_caption(caption, language):
    if language == "English":
        return caption

    translator = translator_models[language]
    tokenizer = translator["tokenizer"]
    model = translator["model"]

    inputs = tokenizer(caption, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs)
    translated_caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_caption

def generate_blip_caption(img):
    inputs = blip_processor(Image.fromarray(img), return_tensors="pt")
    out = blip_model.generate(**inputs)
    caption = blip_processor.decode(out[0], skip_special_tokens=True)
    return caption

def generate_vinvl_caption(img):
    inputs = vinvl_feature_processor(images=Image.fromarray(img), return_tensors="pt").pixel_values
    input_ids = vinvl_model.encoder(inputs)
    
    # Generate an attention mask
    attention_mask = (input_ids != vinvl_tokenizer.pad_token_id).long()

    # Pass the attention mask to the model
    outputs = vinvl_model.generate(
        inputs,
        attention_mask=attention_mask,
        max_length=16,
        num_beams=4
    )
    caption = vinvl_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return caption

def generate_caption(img, model_choice, language):
    if model_choice == "BLIP":
        caption = generate_blip_caption(img)
    elif model_choice == "VinVL":
        caption = generate_vinvl_caption(img)
    else:
        caption = "Model not supported."

    return translate_caption(caption, language)


