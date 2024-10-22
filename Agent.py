from openai import OpenAI

client = OpenAI(
    api_key = 'Your API Key Here'
)

class Twinstalk:
    def __init__(self, model='gpt-4-turbo', prompt_file='./prompt/Twinstalk.txt'):
        self.model = model
        with open(prompt_file, 'r', encoding='utf-8') as file:
            self.initial_prompt = file.read().strip()
        self.conversation_history = [{"role": "system", "content": self.initial_prompt}]

    def generate_response(self, prompt):
        # remember the user input
        self.conversation_history.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            max_tokens=4096
        )
        message = response.choices[0].message.content.strip()
        # remember the response
        self.conversation_history.append({"role": "assistant", "content": message})
        return message

class RobotLLM:
    def __init__(self, model='gpt-4-turbo', prompt_file='./prompt/RobotLLM.txt'):
        self.model = model
        with open(prompt_file, 'r', encoding='utf-8') as file:
            self.initial_prompt = file.read().strip()

    def generate_response(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": self.initial_prompt}, {"role": "user", "content": prompt}],
            max_tokens=150
        )
        message = response.choices[0].message.content.strip()
        return message
    
class VoiceTeamLLM:
    def __init__(self, model='gpt-4-turbo', prompt_file='./prompt/VoiceTeamLLM.txt'):
        self.model = model
        with open(prompt_file, 'r', encoding='utf-8') as file:
            self.initial_prompt = file.read().strip()

    def generate_response(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": self.initial_prompt}, {"role": "user", "content": prompt}],
            max_tokens=150
        )
        message = response.choices[0].message.content.strip()
        return message
    
class HealthAdvisor:
    def __init__(self, model='gpt-4-turbo', prompt_file='./prompt/HealthAdvisor.txt'):
        self.model = model
        with open(prompt_file, 'r', encoding='utf-8') as file:
            self.initial_prompt = file.read().strip()

    def generate_response(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": self.initial_prompt}, {"role": "user", "content": prompt}],
            max_tokens=150
        )
        message = response.choices[0].message.content.strip()
        return message
    
class FinancialAdvisor:
    def __init__(self, model='gpt-4-turbo', prompt_file='./prompt/FinancialAdvisor.txt'):
        self.model = model
        with open(prompt_file, 'r', encoding='utf-8') as file:
            self.initial_prompt = file.read().strip()

    def generate_response(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": self.initial_prompt}, {"role": "user", "content": prompt}],
            max_tokens=150
        )
        message = response.choices[0].message.content.strip()
        return message