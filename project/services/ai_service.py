
import os
from flask import jsonify
from huggingface_hub import InferenceClient

# Initialize the client with the token from environment variables
HF_TOKEN = os.environ.get("HF_TOKEN")
# Use Mistral-7B-Instruct-v0.3
REPO_ID = "Qwen/Qwen2.5-72B-Instruct"

# Initialize Client only if token is present, else handle gracefully in function
client = InferenceClient(api_key=HF_TOKEN) if HF_TOKEN else None

def generate_itinerary_content(city, weather, temp):
    """
    Generates a 1-day travel itinerary using Hugging Face's Inference API.
    """
    if not client:
        print("Error: HF_TOKEN not found in environment variables.")
        return "⚠️ AI Configuration Error: HF_TOKEN is missing. Please check server logs."

    # 1. Construct the Prompt
    system_instruction = "You are an expert local travel guide. Be concise and practical."
    
    user_prompt = f"""
    Create a 1-day travel itinerary for {city}.
    Current weather: {weather}, {temp}°C.
    
    Rules:
    - If raining/cold: focus on indoor activities.
    - If sunny: focus on outdoor activities.
    - Structure: Morning, Afternoon, Evening.
    - IMPORTANT FORMATTING: Do NOT use "Morning:", "Afternoon:" labels. 
    - Separate the three sections ONLY with the string "###". 
    - Example output: "Visit the museum... ### Go to the park... ### Dinner at..."
    """

    try:
        # 2. Call Hugging Face API (Chat Completion)
        response = client.chat_completion(
            model=REPO_ID,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=500,     # Limit length
            temperature=0.7,    # Balanced creativity
            stream=False
        )
        
        # 3. Extract response
        ai_content = response.choices[0].message.content
        return ai_content

    except Exception as e:
        print(f"Error calling Hugging Face: {e}")
        # Fallback message
        return "⚠️ AI agents are currently busy packing their bags. Please try again in a moment!"
