"""
(TR) Aracımızın amaç ve çalışma şekli(:
-Hedef url ve wordlistimiz alır
-Gobuster aracını arka planda çalıştırır
-Sonuçları bölümlendirip döndürür.

Our tool's purpose and how it works:
-It retrieves our target URL and wordlist.
-It runs the Gobuster tool in the background.
-It segments and returns the results.
---------------------------------------------------
(TR) Dikkat:
Fuzzing tekniği hedef makineye çok yüksek boyutlu log dosyaları oluşturur ve DoS benzeri etki yaratabilir
İzinsiz yapılamaz ve yasadışıdır.
Sadece etik hackleme ve sızma testlerinde kullanınız.

Caution:
Fuzzing thecnique is creating very high log files to target machine
Avoid from mapping without permission.
Use only in  ethical hacking and penetration testing
----------------------------------------------------
(TR) Gobuster:
Bir hedef siteye karşı wordlist kullanarak gizli dosya, dizinler ve subdomainleri brute-force ile
bulan araçtır. Örnek olarak h.com/admin , h.com/backup.zip
(daha fazla bilgi için gobuster.org/what-is-gobuster-and-how-does-it-work/ ziyaret edebilirsiniz)

Gobuster: 
Gobuster is a powerful open-source tool designed for directory and DNS brute-forcing 
Widely used in ethical hacking and penetration testing.Written in the Go programming language
(for more information you can visit gobuster.org/what-is-gobuster-and-how-does-it-work/)

"""


import subprocess
""" 
İşletim sistemi düzeyindeki işlemleri ve komut satırı yürütmesini yönetmek için subprocess modülü
Importing the subprocess library to handle OS-level operations and command-line execution
"""

import os
"""
Sistem , klasör ve dosya yolu işlemleri için os modülü
Importing the os library to execute system commands and manage file paths
"""

def run_gobuster(target_url,wordlist_path,threads=50):
    """
    Gobusterı komut satırında kullanmamızı sağlayan foknsiyon.
    threads=50 varsayılan değerdir. Çağırırken bu paramatre yazılmazsa otomatik 50 kullanılır.
    The threads parameter defaults to 50 if not explicitly provided.
    """


    """
    Verilen dosya yolunun sistemde gerçekten var olup olmadığını kontrol ediyor
    Verifying if the provided file path exists on the system
    """
    if not os.path.exists(wordlist_path):

        print(f"Wordlist not found at {wordlist_path}")
        return None    
    
    """
    Komut satırında subprocess modülü için kullanılacak stringi bir liste halinde hazırlıyoruz.
    subprocess modülü yalnızca string gönderebildiğinden str() ile sayıyı(50) metne çeviriyoruz.
    Gobustera bağlı hataları ekrana yazdırmamak için no error flagi ekliyoruz.
    Komut satırında örnek olarak şöyle görünecek : gobuster dir -u h.com -w /home/words.txt -t 50 --no error 
    
    We assemble a list of strings where integers are explicitly cast to str()
    Effectively building a command like: gobuster dir -u h.com -w /home/words.txt -t 50 --no-error.
    """
    command=[
    "gobuster","dir",
    "-u" ,target_url,
    "-w" ,wordlist_path,
    "-t" ,str(threads),
    "--no-error"
    ]

    try:
        print(f"Starting enumeration on: {target_url}")
        """
        subprocess.run(): Terminalde komut çalıştır.
        command: Komut satırı için listemiz.
        capture_output=True: Çıktıyı terminale yazdırmak  yerine Python'a vermek için.
        text= Çıktının string olarak gelmesi için
        check=True Eğer komut başarısız olur  veya sisten hata kodu döndürürse CalledProcessError fırlatılır
        result.stdout: Ekrana yazdırılan sonuçlar stdout dosyası içindedir
        """
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as err:
        """
        Standart hata ise gobusterın asıl hata mesajı yazdırılır
        """
        print(f"An error occurred: {err.stderr}")
        return None
    except FileNotFoundError:
        """
        Sistemde gobuster yüklü değilse bu hata fırlatılır
        """
        print("Error: Gobuster is not installed.")
        return None

if __name__== "__main__":
    target=input("Please type your targe url (Ensure that you have permisson). : ")
    wordlist_path=input("Wordlist path: ")
    scan_results = run_gobuster(target,wordlist_path)
    print(scan_results)
