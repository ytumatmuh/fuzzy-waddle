import socket
import time

print("=== Python Port Tarayiciya Hos Geldin ===")
hedef_ip = input("Lutfen taramak istedigin IP adresini yaz (Orn: 8.8.8.8): ")

port_listesi = [21, 22, 53, 80, 443, 8080]


gecikme = 0.5        
zaman_asimi = 1.0    

print(f"\n--- {hedef_ip} uzerinde tarama baslatiliyor... ---")
print(f"Hiz: Saniyede yaklasik {1/gecikme} port.\n")


try:
    for port in port_listesi:
       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(zaman_asimi)
        
       
        sonuc = s.connect_ex((hedef_ip, port))
        
        if sonuc == 0:
            print(f"Port {port:<5}: [ACIK]")
        else:
            print(f"Port {port:<5}: [KAPALI]")
        
        s.close()

        time.sleep(gecikme)

except KeyboardInterrupt:
    print("\nTarama kullanıcı tarafından durduruldu.")
except socket.gaierror:
    print("\nHata: IP adresi veya Hostname cozulemedi.")
except Exception as e:
    print(f"\nBir hata olustu: {e}")

print("\n--- Tarama Tamamlandi ---")