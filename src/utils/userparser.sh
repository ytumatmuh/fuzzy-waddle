#!/bin/bash
LOG_FILE="/var/log/auth.log"

if [ ! -f "$LOG_FILE" ]; then
    echo "Hata: $LOG_FILE bulunamadı!"
    exit 1
fi

echo "--- 'user' Bazlı Giriş Denemeleri Analizi ---"
results=$(grep -oP 'user \K[^ ]+' "$LOG_FILE" | sort | uniq -c | sort -rn)

if [ -z "$results" ]; then
    echo "Eşleşen kullanıcı kaydı bulunamadı."
else
    echo "Sayı | Kullanıcı Adı"
    echo "--------------------"
    echo "$results"
    
    total_unique=$(echo "$results" | wc -l)
    echo "--------------------"
    echo "Toplam Benzersiz Kullanıcı Sayısı: $total_unique"