import sys

print('=== AI Scenario Chat ===')
print('Type "quit" to exit.\n')

while True:
    user_input = input('You: ')
    if user_input.lower() in ['quit', 'exit', 'q']:
        print('Goodbye!')
        break
    
    # Simple echo response for now - can be expanded
    if 'scenario' in user_input.lower():
        response = 'Imagine a futuristic city where AI rules the streets... What do you do next?'
    else:
        response = f'Echo: Interesting point about "{user_input}". Tell me more!'
    
    print(f'AI: {response}\n')