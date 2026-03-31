import socket

# Ayarlar
hedef_ip = "8.8.8.8"
port_listesi = [53, 80, 443]

print(f"--- Tarama Başlatıldı: {hedef_ip} ---")

for port in port_listesi:
    # Yeni bir bağlantı soketi oluştur
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 1 saniye bekledikten sonra cevap gelmezse vazgeç
    s.settimeout(1)
    
    # Bağlantıyı dene (0 dönerse başarılıdır)
    sonuc = s.connect_ex((hedef_ip, port))
    
    if sonuc == 0:
        print(f"Port {port}: [AÇIK]")
    else:
        print(f"Port {port}: [KAPALI]")
    
    # Soketi her seferinde kapat
    s.close()

print("--- Tarama Tamamlandı ---")