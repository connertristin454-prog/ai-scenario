import random


def generate_scenario(theme='sci-fi'):
    """Generate a random scenario based on the chosen theme."""
    scenarios = {
        'sci-fi': [
            'You wake up on a spaceship heading to Mars. The AI pilot asks for your input.',
            'AI has taken over the world, and you are one of the last humans resisting.',
            'You discover a time-travel device built by rogue AIs.'
        ],
        'fantasy': [
            'A dragon guards the ancient treasure in a forgotten cave.',
            'You discover a magical portal that leads to another realm.',
            'The kingdom is under siege by dark sorcerers.'
        ],
        'horror': [
            'Strange noises come from the basement at midnight.',
            'The shadows in your room start moving on their own.',
            'Everyone in town has the same eerie smile.'
        ],
        'mystery': [
            'A cryptic note appears on your desk with no explanation.',
            'The detective needs your help solving an impossible case.'
        ]
    }
    return random.choice(scenarios.get(theme.lower(), scenarios['sci-fi']))


def main():
    print('🤖 Welcome to the AI Scenario Simulator!')
    print('Choose a theme to begin your adventure.')
    
    themes = ['sci-fi', 'fantasy', 'horror', 'mystery']
    print('Available themes:', ', '.join(themes))
    
    theme = input('\nEnter theme: ').strip().lower()
    if not theme:
        theme = 'sci-fi'
    
    scenario = generate_scenario(theme)
    print(f'\n📖 Scenario: {scenario}')
    print('\nWhat do you do next? (Your choices can expand this simulation!)')

if __name__ == '__main__':
    main()
