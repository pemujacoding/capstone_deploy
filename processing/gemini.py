import json
import os
import time
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY tidak ditemukan!")

genai.configure(api_key=GEMINI_API_KEY)

PRIMARY_MODEL = "gemini-2.5-flash"
FALLBACK_MODEL = "gemini-2.0-flash"

def safe_generate(model, prompt, retries=5):
    model_obj = genai.GenerativeModel(model)

    for attempt in range(retries):
        try:
            return model_obj.generate_content(prompt)
        except Exception as e:
            err = str(e)
            if "quota" in err or "resource_exhausted" in err or "429" in err:
                print(f"[ERROR] Gemini quota exceeded: {e}")
                return None
            elif "503" in err or "overloaded" in err or "UNAVAILABLE" in err:
                wait = 2 * (attempt + 1)
                print(f"[Gemini] Overloaded. Retry {attempt+1}/{retries} in {wait}s...")
                time.sleep(wait)
                continue
            else:
                print(f"[ERROR] Unexpected Gemini error: {e}")
                raise

    raise RuntimeError("Gemini failed after retries.")
