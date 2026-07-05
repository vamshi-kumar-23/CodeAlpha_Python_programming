def start_chat():
    print("CodeAlpha Chatbot - Task 4")
    print("Student: Battu Vamshi Kumar")
    print("Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    # This loop keeps the chat running continuously
    while True:
        # Get input from the user and convert it to lowercase
        user_input = input("You: ").lower()
        
        # Rule 1: Greetings
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
            
        # Rule 2: How are you?
        elif "how are you" in user_input:
            print("Chatbot: I'm just a computer program, but I'm doing great! Thanks for asking.")
            
        # Rule 3: Exit condition
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break # This stops the while loop
            
        # Fallback rule
        else:
            print("Chatbot: I'm sorry, I don't understand that yet.")

# Run the chatbot function
start_chat()