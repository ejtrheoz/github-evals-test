import yaml
from typing import Optional, Dict, Any


def parse_system_prompt(file_path: str) -> Optional[str]:
    """
    Parse the system prompt from a .prompt.yml file.
    
    Args:
        file_path (str): Path to the .prompt.yml file
        
    Returns:
        Optional[str]: The system prompt content, or None if not found
    """
    try:
        with open(file_path, 'r') as file:
            prompt_data = yaml.safe_load(file)
        
        # Find the system message in the messages array
        if 'messages' in prompt_data:
            for message in prompt_data['messages']:
                if message.get('role') == 'system':
                    return message.get('content')
        
        return None
        
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def parse_prompt_file(file_path: str) -> Dict[str, Any]:
    """
    Parse the entire .prompt.yml file and return all data.
    
    Args:
        file_path (str): Path to the .prompt.yml file
        
    Returns:
        Dict[str, Any]: The entire prompt configuration
    """
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error parsing file {file_path}: {e}")
        return {}


# Example usage
if __name__ == "__main__":
    # Parse system prompt from your current file
    system_prompt = parse_system_prompt('/home/illia/work/git-evals-test/check.prompt.yml')
    if system_prompt:
        print("System prompt found:")
        print(system_prompt)
    else:
        print("No system prompt found")
    
    print("\n" + "="*50 + "\n")
    
    # Parse system prompt from the prompts folder
    system_prompt2 = parse_system_prompt('/home/illia/work/git-evals-test/prompts/check-error.prompt.yml')
    if system_prompt2:
        print("System prompt from prompts folder:")
        print(system_prompt2)
    
    print("\n" + "="*50 + "\n")
    
    # Parse entire file
    full_config = parse_prompt_file('/home/illia/work/git-evals-test/check.prompt.yml')
    print("Full configuration:")
    print(f"Model: {full_config.get('model', 'Not specified')}")
    print(f"Number of messages: {len(full_config.get('messages', []))}")
