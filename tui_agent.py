import subprocess
import sys

def display_ascii_art():
    """Displays a cool ASCII art for the TUI."""
    ascii_art = """
  _   _   _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ / \ / \ 
( C | Y | B | E | R | A | G | E | N )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

    """
    print(ascii_art)
    print("Welcome to CyberAgent - Your Terminal-Based Cybersecurity Assistant!")
    print("Type your cybersecurity problem or question below. Type 'exit' to quit.")
    print("-------------------------------------------------------------------")

def main():
    display_ascii_art()
    # Run the terminal_agent.py as a subprocess
    # We use sys.executable to ensure the correct python interpreter is used
    subprocess.run([sys.executable, "terminal_agent.py"])

if __name__ == '__main__':
    main()
