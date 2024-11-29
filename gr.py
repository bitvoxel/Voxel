from groq import Groq

class Gr:
    def __init__(self, api_key, model="llama3-8b-8192"):
        self.api_key = api_key
        self.client = Groq(api_key=self.api_key)
        self.model = model
        self.chat = []

    def set_model(self, model):
        self.model = model

    def ask(self, prompt):
        self.chat.append({"role": "user", "content": prompt})

        try:
            response = self.client.chat.completions.create(
                messages=self.chat,
                model=self.model
            )
            LLM_reply = response.choices[0].message.content
            self.chat.append({"role": "assistant", "content": LLM_reply})
            return LLM_reply
        except Exception as e:
            return f"Error: {str(e)}"

    def reset_chat(self):
        self.chat = []