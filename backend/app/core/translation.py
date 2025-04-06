import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def translate_text(text: str, target_lang: str) -> str:
    """
    Translates a given text to the target language using Gemini Pro.
    """
    prompt = f"Translate the following into {target_lang}:\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Translation failed: {e}")
        return text  # Fallback to original if error
