import configparser
import os

config = configparser.ConfigParser()

if not os.path.isfile('config.ini'):
    
    # Default
    config['Language'] = {
        'blue': 'Python',
        'red': 'C',
        'yellow': 'Java',
        'green': 'Rust'
    }
    
    config['Project'] = {
        '0': 'Discord Bot',
        '1': 'Random API Website',
        '2': 'Secure Notes',
        '3': 'Password Manager',
        '4': 'Authentication System',
        '5': 'Neural Network',
        '6': 'TBD',
        '7': 'TBD',
        '8': 'TBD',
        '9': 'TBD'
    }
    
    with open('config.ini', 'w') as f:
        config.write(f)
        
else:      
    config.read('config.ini')
    
# Tests
if not config['Language']:
    print("Config Error: No Language Section! Exiting...")
    exit(-1)
    
if not config['Project']:
    print("Config Error: No Project Section! Exiting...")
    exit(-1)
    
if len(config['Language'].values()) < 4:
    print("Config Error: Not enough values in Language Section! Exiting...")
    exit(-1)
    
if len(config['Language'].values()) < 4:
    print("Config Error: Not enough values in Project Section! Exiting...")
    exit(-1)
    
def get() -> configparser.ConfigParser:
    """Function to return instance of our config

    Returns:
        configparser.ConfigParser: Our config parsed
    """
    return config