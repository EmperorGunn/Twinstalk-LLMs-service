from openai import OpenAI

client = OpenAI(
    api_key = 'Your API Key Here'
)

class AgentWithMemory:
    def __init__(self, model='gpt-3.5-turbo'):
        self.model = model
        self.conversation_history = []

    def generate_response(self, prompt):
        self.conversation_history.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            max_tokens=4096
        )
        message = response.choices[0].message.content.strip()
        self.conversation_history.append({"role": "assistant", "content": message})
        return message

myAgent = AgentWithMemory()

user_input = "What is the result of 1 + 3 ?"
response = myAgent.generate_response(user_input)
print(response)

user_input = "What is the result of 2 + 5 ?"
response = myAgent.generate_response(user_input)
print(response)

user_input = "What is the first question I asked you?"
response = myAgent.generate_response(user_input)
print(response)