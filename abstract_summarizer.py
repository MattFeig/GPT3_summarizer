#!/usr/bin/env python3

import sys, os
from PIL import Image
from pytesseract import pytesseract
import openai

def summarizer(arguments):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    image_path = arguments[0]
    img = Image.open(image_path)
    img_text = pytesseract.image_to_string(img)
    img_text = img_text.replace("\n", "")
    prompt = f"Summarize the following science journal abstract in 2 sentences: {img_text}"
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=.2, max_tokens=150)
    text = response["choices"][0]["text"].replace("A:", "").strip()
    print(text)

if __name__ == '__main__':
    sys.exit(summarizer(sys.argv[1:]))
