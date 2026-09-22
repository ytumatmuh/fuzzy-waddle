"""
İlgili Task: (Nmap Integration and Port Scanning)
Sorumlu: (arda - talha)

Açıklama: 
Subprocess kütüphanesini kullanarak sistemdeki 'nmap' aracını hedefe yönelik çalıştırır. 
Tarama sonuçlarını yakalar ve işlenmesi için döndürür.
"""
import subprocess

def run_nmap(target):
    print(f"\n[+] {target} için Nmap servis taraması (-sV) başlatılıyor...")
    print("[!] Bu işlem hedefin hızına göre biraz zaman alabilir...\n")
    
    command = ["nmap", "-sV", target]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("[+] Nmap Taraması Tamamlandı! Sonuçlar:\n")
        print(result.stdout)
        return result.stdout
        
    except FileNotFoundError:
        print("[-] Hata: Sisteminizde 'nmap' kurulu bulunamadı.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Hata: Nmap çalıştırılırken bir sorun oluştu:\n{e.stderr}")