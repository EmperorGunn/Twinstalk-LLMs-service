from flask import Flask, request, jsonify
import logging
import Agent


app = Flask(__name__)


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='server.log', filemode='a')
logger = logging.getLogger(__name__)


class LLMSystem:
    def __init__(self):
        self.twinstalk = Agent.Twinstalk()
        self.voiceTeamLLM = Agent.VoiceTeamLLM()
        self.robotLLM = Agent.RobotLLM()
        self.healthAdvisor = Agent.HealthAdvisor()
        self.financialAdvisor = Agent.FinancialAdvisor()

    def generate_system_response(self, prompt):
        response_twinstalk = self.twinstalk.generate_response(prompt)
        logger.info(f"First-level response (Twinstalk): {response_twinstalk}")

        if response_twinstalk.startswith("[Twinstalk to VoiceTeamLLM]"):
            # If the issues is health and financial related, then generate a second level response from VoiceTeamLLM
            second_level_response = self.voiceTeamLLM.generate_response(response_twinstalk)
            logger.info(f"Second-level response (VoiceTeamLLM): {second_level_response}")

            if second_level_response.startswith("[VoiceTeamLLM to HealthAdvisor]"):
                # Health related issues
                third_level_response = self.healthAdvisor.generate_response(second_level_response)
                logger.info(f"Third-level response (HealthAdvisor): {third_level_response}")
                second_level_response = self.voiceTeamLLM.generate_response(third_level_response)
                logger.info(f"Updated second-level response (VoiceTeamLLM): {second_level_response}")
            elif second_level_response.startswith("[VoiceTeamLLM to FinancialAdvisor]"):
                # Financial related issues
                third_level_response = self.financialAdvisor.generate_response(second_level_response)
                logger.info(f"Third-level response (FinancialAdvisor): {third_level_response}")
                second_level_response = self.voiceTeamLLM.generate_response(third_level_response)
                logger.info(f"Updated second-level response (VoiceTeanLLM): {second_level_response}")
        elif response_twinstalk.startswith("[Twinstalk to Human]"):
            # if the response is directed to human, then no need to generate a second level response
            return response_twinstalk
        else:
            # Robot Manipulation tasks
            second_level_response = self.robotLLM.generate_response(response_twinstalk)
            logger.info(f"Second-level response (RobotLLM): {second_level_response}")

        # Generate the final response through user-interface agent Twinstalk
        response_twinstalk = self.twinstalk.generate_response(second_level_response)
        logger.info(f"Updated first-level response (Twinstalk): {response_twinstalk}")
        
        return response_twinstalk


coordinator = LLMSystem()


'''
This function is called when a client sent a POST request with a question to the /ask endpoint.
'''
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')

    # If the user did not provide a question, return an error response
    if not user_input:
        return jsonify({'error': 'No question provided'}), 400
    
    # Generate a response to the user's question
    response = coordinator.generate_system_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)