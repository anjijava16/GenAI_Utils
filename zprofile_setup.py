import os
import re

def load_zprofile_to_env(filepath):
    """
    Reads a zsh profile file and loads the environment variables into os.environ.
    :param filepath: Path to the zsh profile file.
    """
    # Expand the tilde (~) to the user's home directory
    filepath = os.path.expanduser(filepath)
    
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        # Regex to match valid environment variable definitions
        pattern = re.compile(r'^\s*export\s+(\w+)=["\']?(.*?)["\']?\s*$')
        
        for line in lines:
            match = pattern.match(line.strip())
            if match:
                key, value = match.groups()
                os.environ[key] = value
                print(f"Set {key}={value}")
    except FileNotFoundError:
        print(f"File {filepath} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
load_zprofile_to_env('~/.zprofile')
