from groq import Groq

class Gr:
    def __init__(self):
        self.api_key="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"
        self.client= Groq(api_key=self.api_key)
        self.model="llama3-8b-8192"
        self.chat=[]

    def setModel(self,model):
        self.model=model

    def ask(self,prompt):
        self.chat.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
        messages=self.chat,
        model=self.model)
        LLM_reply = response.choices[0].message.content
        self.chat.append({"role": "assistant", "content": LLM_reply})
        return LLM_reply
    
    
