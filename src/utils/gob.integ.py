import subprocess
import os

def run_gobuster(target_url,wordlist_path,threads=50):
    #check path
    if not os.path.exists(wordlist_path):

        print(f"Wordlist not found at {wordlist_path}")
        return None    
    

    command=[
    "gobuster","dir",
    "-u" ,target_url,
    "-w" ,wordlist_path,
    "-t" ,str(threads),
    "--no-error"
    ]

    try:
        print(f"Starting enumeration on: {target_url}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as err:
        print(f"An error occurred: {err.stderr}")
        return None
    except FileNotFoundError:
        print("Error: Gobuster is not installed.")
        return None

""" if __name__== "__main__":
    target=input("Please type your targe url (Ensure that you have permisson). : ")
    wordlist_path=input("Wordlist path: ")
    scan_results = run_gobuster(target,wordlist_path)
    print(scan_results)
 """