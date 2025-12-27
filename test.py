import google.generativeai as genai

API_KEY = "AIzaSyDpeKU3uqWE4XeGfP23sJPsZdHLhlE1hvE"
genai.configure(api_key=API_KEY)

print("List of available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)