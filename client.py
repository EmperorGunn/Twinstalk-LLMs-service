import requests

if __name__ == '__main__':
    while True:
        user_input = input('Please ask your question: ')
        # If the user types "exit", then exit the loop
        if user_input.startswith("exit"):
            print("Exiting...")
            break
        
        try:
            response = requests.post('http://127.0.0.1:5000/ask', json={'question': user_input})
            response_data = response.json()

            # Print the response from the server
            if 'response' in response_data:
                print("Response:", response_data['response'])
            elif 'error' in response_data:
                print("Error:", response_data['error'])
            else:
                print("Unexpected response format:", response_data)
                
        # Handle network errors
        except requests.exceptions.RequestException as e:
            print("Network error:", e)