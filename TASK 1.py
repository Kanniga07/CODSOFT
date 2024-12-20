class NIGAChatbot:
    def __init__(self):
        self.greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
        self.farewells = ["bye", "goodbye", "see you", "take care", "farewell"]

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        if any(greet in user_input for greet in self.greetings):
            return "Hello! I am NIGA, your AI assistant. How can I help you today?"
        elif "how are you" in user_input:
            return "I'm just a bot, but I'm doing great! How about you?"
        elif "what is your name?" in user_input:
            return "I am NIGA, your AI assistant."
        elif "tell me about today's weather" in user_input:
            return "I'm not connected to live data, but I hope the weather is pleasant."
        elif "tell me a joke" in user_input:
            return "Why do scientists not believe in atoms? as they are the foundation of everything!"
        elif "thank you" in user_input or "thanks" in user_input:
            return "You're welcome! Happy to assist you."
        elif any(farewell in user_input for farewell in self.farewells):
            return "Goodbye! I hope you have an amazing day"
        else:
            return "I don't know how to react to that. Would you mind alter the wording?"

    def start_chat(self):
        print("Welcome to NIGA Chatbot! Type 'bye' or any greeting to begin or exit.")
        
        while True:
            user_input = input("USER: ")
            if any(farewell in user_input.lower().strip() for farewell in self.farewells):
                print("NIGA: Goodbye! Have a wonderful day!")
                break
            response = self.get_response(user_input)
            print(f"NIGA: {response}")

if __name__ == "__main__":
    chatbot = NIGAChatbot()
    chatbot.start_chat()
