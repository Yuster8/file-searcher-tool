import os
import random
import pyfiglet
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def print_banner():
    # Create a big ASCII version of "TINAH AND J4 "
    banner_text = pyfiglet.figlet_format("Tnah and  J4", font="slant")  # You can change the font here
    print(Fore.CYAN + banner_text)
    
    # List of possible decorations (ASCII art)
    decorations = [
        # Tree decoration
        """
           ^^^
          ^^^^^
         ^^^^^^^
        ^^^^^^^^^
       ^^^^^^^^^^^
          |||
          |||
        """,
        
        # Train decoration
        """
          o o o o o o o o o
        _______________________
       /                       \\
      |   o   o   o   o   o   o  |
      |_______________________| 
         |  |   |   |   |  | 
         """,
        
        # Mountain decoration
        """
              /\      
             /  \   /\  
            /    \ /  \    /\  
           /______\____\__/
        """,
        
        # Rocket decoration
        """
           /\\
          |==|
          |  |
         /____\\
        |      |
        |      |
        |______|
        """,
        
        # Cat decoration
        """
        /\_/\  
       ( o.o ) 
        > ^ <
        """
    ]
    
    # Randomly select a decoration
    selected_decoration = random.choice(decorations)
    
    # Print the random decoration
    print(Fore.GREEN + selected_decoration)
    print(Fore.YELLOW + "Welcome to the File Searcher Tool!")
    print(Fore.GREEN + "Developed by: Tnah && Madefuckles\n")

def find_file(file_name, search_dir='/'):
    """
    Scans the system or specified directory for a file and returns its path if found.
    
    :param file_name: The name of the file to search for.
    :param search_dir: The directory to start the search from (default is the root "/").
    :return: The full path of the file if found, else a message saying the file wasn't found.
    """
    print(Fore.MAGENTA + f"Searching for '{file_name}' in {search_dir}...\n")
    for root, dirs, files in os.walk(search_dir):
        if file_name in files:
            print(Fore.GREEN + f"File found! Path: {os.path.join(root, file_name)}")
            return os.path.join(root, file_name)
    
    print(Fore.RED + f"Sorry, the file '{file_name}' was not found.")
    return None

def main():
    print_banner()

    # User input for the file name and search directory
    file_name = input(Fore.YELLOW + "Enter the file name you want to search for: ")
    search_directory = input(Fore.YELLOW + "Enter the directory to search in (e.g., '/home/user', or press Enter for the entire system): ")

    if not search_directory:
        search_directory = '/'  # Default to searching the whole system if not specified

    print(Fore.BLUE + "Starting the search...\n")
    
    file_path = find_file(file_name, search_directory)

    if file_path:
        print(Fore.GREEN + f"File found at: {file_path}")
    else:
        print(Fore.RED + "File not found. Try a different directory or file name.")

if __name__ == "__main__":
    main()
