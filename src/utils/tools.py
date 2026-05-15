import argparse 
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Aracim - A simple cyber security tool')
    parser.add_argument('ip_address', help='hedef ip adresi')
    parser.add_argument('--port', '-p', help='hedef port numarası')
    parser.add_argument('-v', '--verbose', action='store_true', help='detaylı çıktı')
    args = parser.parse_args()  

    print(f'ip_address: {args.ip_address}')
    print(f'port: {args.port}')

    if args.verbose:
        print('Detaylı çıktı etkinleştirildi.')

    print(f"\n--- {args.ip_address} nmap taraması başlıyor ---")
    if args.port:
        nmap_emri = f"nmap {args.ip_address} -p {args.port} -sV "
    else:
        nmap_emri = f"nmap {args.ip_address} -sV"

    sonuc = subprocess.run(nmap_emri.split(), capture_output=True, text=True)
    print(sonuc.stdout)

    port_80_acik = "80/tcp open" in sonuc.stdout
    port_443_acik = "443/tcp open" in sonuc.stdout
    port_8080_acik = "8080/tcp open" in sonuc.stdout

    protocol = "https" if port_443_acik else "http"
    
    if port_80_acik or port_443_acik or port_8080_acik:
        if port_8080_acik:
            target_url = f"http://{args.ip_address}:8080"
        else:
            target_url = f"{protocol}://{args.ip_address}"
        
        print(f"[+] Web hizmeti bulundu: {target_url}")
        print(f"[+] {args.ip_address} üzerinde uygun web portu bulundu.")
        print(f"[*] {target_url} üzerinde otomatik olarak Gobuster çalıştırılıyor...")

        gobuster_emri = f"gobuster dir -u {target_url} -w common.txt -o gobuster_output.txt"
            
        try:
                sonuc = subprocess.run(gobuster_emri.split(), check=True, capture_output=True, text=True)
                print("Gobuster taraması tamamlandı. gobuster_output.txt dosyası nuclei ile taranıyor.")
                        
                nuclei_emri = f"nuclei -list gobuster_output.txt -severity info,low,medium,high,critical"
                subprocess.run(nuclei_emri.split(), check=True)

        except FileNotFoundError as e:
                        print(f"Bir araç bulunamadı: {e}")
        except subprocess.CalledProcessError as e:
                        print(f"Komut çalıştırılırken hata oluştu: {e}")
                        print("[-] Tarama sırasında bir hata oluştu.")
    else:
                print(f"{args.ip_address} üzerinde 80, 443 veya 8080 numaralı portlar kapalı.")

if __name__ == '__main__':
    main()