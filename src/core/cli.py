"""
İlgili Task: (Command Line Interface Design)
Sorumlu: (arda - talha)

Açıklama: 
argparse kütüphanesi kullanılarak programın dışarıdan alacağı parametreleri 
(-t hedef, -w wordlist vb.) tanımlar ve işler.
"""
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Fuzzy-Waddle: Otomatik Siber Güvenlik Keşif Aracı"
    )
    parser.add_argument("-t", "--target", required=True, help="Hedef IP veya URL (Örn: 192.168.1.1)")
    parser.add_argument("-w", "--wordlist", help="Gobuster/Ffuf için wordlist dosya yolu")
    
    return parser.parse_args()