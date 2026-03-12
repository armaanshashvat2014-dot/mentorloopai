import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY")

def chatbot():
    print("Welcome to the AI Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        try:
            # Call OpenAI API
            response = openai.Completion.create(
                engine="text-davinci-003",  # Use the GPT model
                prompt=user_input,
                max_tokens=150,
                temperature=0.7
            )
            # Print the AI's response
            print("AI:", response.choices[0].text.strip())
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chatbot()
