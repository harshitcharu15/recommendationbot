import os
import openai

#client = OpenAI(api_key=os.getenv("4w2gf4ReoMWlu9H27ODLWOGW34JuRjUhI2H8fYnuvXIw7MfIU7dXJQQJ99BCACHYHv6XJ3w3AAAAACOGMfh9"))
import os

def recommend(category):
    recommendations = {
        "book": "I recommend reading 'Atomic Habits' by James Clear!",
        "movie": "How about watching 'Inception'? It's a great sci-fi movie!",
        "music": "You might enjoy 'Bohemian Rhapsody' by Queen!",
        "food": "I suggest trying sushi, it's delicious!",
        "travel": "Consider visiting Japan, it has amazing culture and food!"
    }
    return recommendations.get(category.lower(), "I can recommend books, movies, music, food, and travel destinations!")

# Azure OpenAI setup
  # Set your API key
openai.api_key_path="4w2gf4ReoMWlu9H27ODLWOGW34JuRjUhI2H8fYnuvXIw7MfIU7dXJQQJ99BCACHYHv6XJ3w3AAAAACOGMfh9",
openai.api_base = "https://kohli-m8kd5zju-eastus2.openai.azure.com/"  # Set your Azure OpenAI endpoint
model_name = "gpt-4"  # Change this to your deployed model

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(model=model_name,
    messages=[
        {"role": "system", "content": "You are a helpful recommendation assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=100)
    return response.choices[0].message.content.strip()

def chat():
    print("Hello! I am your Azure AI-powered RecommendationBot. Ask me for recommendations on books, movies, music, food, or travel.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye! Have a great day!")
            break
        elif user_input.lower() in ["book", "movie", "music", "food", "travel"]:
            print("Bot:", recommend(user_input))
        else:
            print("Bot:", get_ai_response(user_input))

if __name__ == "__main__":
    chat()

