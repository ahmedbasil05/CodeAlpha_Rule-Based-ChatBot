import time
from datetime import datetime

# -----------------------------
# ChatPy: Rule-Based Chatbot
# -----------------------------

# Keyword-response mapping
KEYWORD_RESPONSES = {
    # Greetings
    ("hello", "hi", "hey", "greetings"): "Hi there! How can I assist you today?",
    
    # Well-being
    ("how are you", "doing", "feeling", "are you okay"): "I'm doing well, thanks for asking! What about you?",
    
    # Identity
    ("your name", "who are you", "what should i call you"): "You can call me ChatPy – your personal chatbot assistant.",
    
    # Time
    ("time", "clock", "current time"): lambda: f"The current time is {datetime.now().strftime('%I:%M %p')}.",
    
    # Date
    ("date", "day", "today"): lambda: f"Today is {datetime.now().strftime('%A, %B %d, %Y')}.",
    
    # Jokes
    ("joke", "funny", "laugh"): "Why did the computer show up at work late? It had a hard drive! 😄",
    
    # Gratitude
    ("thank", "thanks", "appreciate"): "You're welcome! Always happy to help 😊",
    
    # Help
    ("help", "assist", "support"): "Sure! Feel free to ask anything you'd like help with.",
    
    # Interests
    ("hobby", "like", "do you do"): "I love chatting, answering questions, and helping with Python!",
    
    # Farewell
    ("bye", "goodbye", "see you", "exit", "quit"): "It was a pleasure talking to you. Goodbye and take care!",
}

# Function: Dynamic greeting based on current time
def time_based_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    return "Good evening!"

# Function: Match user input with keywords
def match_keywords(user_input):
    user_input = user_input.lower()
    for keywords, response in KEYWORD_RESPONSES.items():
        if any(keyword in user_input for keyword in keywords):
            return response() if callable(response) else response
    return "I'm not quite sure how to respond to that. Could you try asking something else?"

# Main chatbot loop
def run_chatbot():
    print("\n🤖 ChatPy: Hello! I'm your chatbot assistant.")
    print("💬 You can ask me things like the time, a joke, or just say hi.")
    print("🔚 Type 'bye' anytime to end the chat.\n")
    print("⏰", time_based_greeting(), "\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("ChatPy: Could you please type something?")
            continue

        time.sleep(0.6)  # Simulate typing delay
        response = match_keywords(user_input)
        print("ChatPy:", response)

        # Exit condition
        if any(exit_word in user_input.lower() for exit_word in ("bye", "goodbye", "exit", "quit", "see you")):
            break

    print("\n👋 ChatPy: Session ended. Have a great day!")

# Entry point
if __name__ == "__main__":
    run_chatbot()
