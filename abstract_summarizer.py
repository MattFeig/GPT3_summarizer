#!/usr/bin/env python3

import sys, os, argparse
from PIL import Image
from pytesseract import pytesseract
import openai

def abstract_summarizer():


    arg_parser = argparse.ArgumentParser(description="""this script creates a 2 sentence GPT3 summary from an
                image of a scientific abstract --- Example call: python3 abstract_summarizre.py path/to/png""")
    if len(sys.argv[1:])==0:
        print('\nArguments required. Use -h option to print FULL usage.\n')
    arg_parser.add_argument('image_path', type=os.path.abspath, help = 'png file path of a scientific abstract')
    args = arg_parser.parse_args()

    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    img = Image.open(args.image_path)
    img_text = pytesseract.image_to_string(img)
    img_text = img_text.replace("\n", "")
    prompt = f"Summarize the following science journal abstract in 2 sentences: {img_text}"
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=.2, max_tokens=150)
    text = response["choices"][0]["text"].replace("A:", "").strip()
    print(text)

if __name__ == '__main__':
    sys.exit(abstract_summarizer())
