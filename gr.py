from groq import Groq

class Gr:
    def __init__(self, model="llama3-8b-8192"):
        self.client = Groq(api_key = "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")
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