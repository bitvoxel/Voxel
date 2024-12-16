from groq import Groq

class Gr:
    """
    A class to interact with the Groq API for chat completions.

    Attributes:
    api_key (str): The API key for the Groq client.
    client (Groq): The Groq client instance.
    model (str): The model to use for chat completions.
    chat (list): A list of chat messages.
    """

    def __init__(self):
        """
        Initializes the Gr class.

        Sets the API key, creates a Groq client instance, and sets the default model.
        """
        self.api_key = "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"
        self.client = Groq(api_key=self.api_key)
        self.model = "llama3-8b-8192"
        self.chat = []

    def setModel(self, model):
        """
        Sets the model to use for chat completions.

        Args:
        model (str): The model to use.
        """
        self.model = model

    def ask(self, prompt):
        """
        Sends a prompt to the chat completion model and returns the response.

        Args:
        prompt (str): The prompt to send to the model.

        Returns:
        str: The response from the model.
        """
        self.chat.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            messages=self.chat,
            model=self.model)
        LLM_reply = response.choices[0].message.content
        self.chat.append({"role": "assistant", "content": LLM_reply})
        return LLM_reply
    
    
