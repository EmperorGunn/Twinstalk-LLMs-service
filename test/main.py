import Agent

class LLMSystem:
    def __init__(self):
        self.twinstalk = Agent.Twinstalk()
        self.voiceTeamLLM = Agent.VoiceTeamLLM()
        self.robotLLM = Agent.RobotLLM()
        self.healthAdvisor = Agent.HealthAdvisor()
        self.financialAdvisor = Agent.FinancialAdvisor()

    def generate_system_response(self, prompt):
        response_twinstalk = self.twinstalk.generate_response(prompt)
        print(response_twinstalk)

        if response_twinstalk.startswith("[Twinstalk to VoiceTeamLLM]"):
            # Health and financial related issues
            second_level_response = self.voiceTeamLLM.generate_response(response_twinstalk)
            print(second_level_response)
            if second_level_response.startswith("[VoiceTeamLLM to HealthAdvisor]"):
                # Health related issues
                third_level_response = self.healthAdvisor.generate_response(second_level_response)
                print(third_level_response)
                second_level_response = self.voiceTeamLLM.generate_response(third_level_response)
                print(second_level_response)
            elif second_level_response.startswith("[VoiceTeamLLM to FinancialAdvisor]"):
                # Financial related issues
                third_level_response = self.financialAdvisor.generate_response(second_level_response)
                print(third_level_response)
                second_level_response = self.voiceTeamLLM.generate_response(third_level_response)
                print(second_level_response)

        elif response_twinstalk.startswith("[Twinstalk to Human]"):
            # if the response is directed to human, then no need to generate a second level response
            return response_twinstalk
        else:
            # Robot Manipulation tasks
            second_level_response = self.robotLLM.generate_response(response_twinstalk)
            print(second_level_response)

        # From the second level response, generate the final response
        response_twinstalk = self.twinstalk.generate_response(second_level_response)
        
        return response_twinstalk

print('system start')
coordinator = LLMSystem()

'''
myOption = 1
VOICEOPTION = 1
ROBOTOPTION = 2

if myOption == VOICEOPTION:
    user_input = "My BMI is 19.6. Is this within the normal range for adult males?"
elif myOption == ROBOTOPTION:
    user_input = "Bring me the coffee from the table"
'''

while(True):
    user_input = input('Please ask your question：')
    if user_input.startswith("exit"):
        break
    response_twinstalk = coordinator.generate_system_response(user_input)
    print(response_twinstalk)
    user_input = ""


'''
user_input = "What was my first question to you? What was its answer?"
response_twinstalk = coordinator.generate_system_response(user_input)
print(response_twinstalk)
'''

print('system end')