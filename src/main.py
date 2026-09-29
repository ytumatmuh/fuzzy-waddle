from core.cli import parse_arguments
from modules.nmap_runner import run_nmap  # <-- Nmap modülünü içeri aktarıyoruz

def main():
    args = parse_arguments()
    
    print("-" * 40)
    print("[*] Fuzzy-Waddle Keşif Aracı Başlatılıyor...")
    print(f"[*] Hedef: {args.target}")
    
    if args.wordlist:
        print(f"[*] Wordlist: {args.wordlist}")
    print("-" * 40)

    # <-- Nmap fonksiyonunu BURADA çağırıyoruz -->
    run_nmap(args.target)

if __name__ == "__main__":
    main()