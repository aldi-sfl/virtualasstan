import tkinter as tk

class Chatbot:
    def __init__(self, window):
        self.window = window
        self.window.title("Chatbot")
        self.create_widgets()

    def create_widgets(self):
        # Create a text field and a send button
        self.text_field = tk.Entry(self.window)
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)

        # Create a chat log and a scrollbar
        self.chat_log = tk.Text(self.window, state="disabled", bg='gray')
        self.scrollbar = tk.Scrollbar(self.window)

        # Configure the scrollbar and chat log
        self.chat_log.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.chat_log.yview)

        # Pack the widgets
        self.text_field.pack(side="left")
        self.send_button.pack(side="left")
        self.chat_log.pack(side="left")
        self.scrollbar.pack(side="right", fill="y")

    def send_message(self):
        # Get the message from the text field
        message = self.text_field.get()

        # Clear the text field
        self.text_field.delete(0, "end")

        # Insert the message into the chat log
        self.chat_log.configure(state="normal")
        self.chat_log.insert("end", "You: " + message + "\n")
        self.chat_log.configure(state="disabled")

        # Send the message to the chatbot and get a response
        response = self.get_response(message)

        # Insert the response into the chat log
        self.chat_log.configure(state="normal")
        self.chat_log.insert("end", "Bot: " + response + "\n")
        self.chat_log.configure(state="disabled")

    def get_response(self, message):
        # This is where you would write code to process the message and generate a response
        if message == "hi":
            return "Hello!"
        elif message == "how are you":
            return "I'm good, thanks for asking."
        else:
            return "I'm not sure what you mean."

# Create the main window
window = tk.Tk()

# Create the chatbot
chatbot = Chatbot(window)

# Run the main loop
window.mainloop()
