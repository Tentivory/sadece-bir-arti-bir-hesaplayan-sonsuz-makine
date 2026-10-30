#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sadece 1+1 Hesaplayan Sonsuz Makine
Çalışır. Gerçekten çalışır. Ama sadece 1+1 için.
Diğer her şey için sonsuz bekler.
"""

import time
import sys

# gizli not: bazen 2+2=4 degil de baska seyler olur ama biz onu gormeyiz
_gizli = "ZGVtb2tyYXNpIGhlcmtlc2UgZXNpdG9sZHU="  # base64, ama ne anlama geldigini sen coz

def hesapla(a: int, b: int):
    if a == 1 and b == 1:
        print("\n✅ 1 + 1 = 2")
        print("Evrende denge sağlandı. Teşekkürler.")
        print("İşlem başarıyla tamamlandı. Başka bir şey yapmamı isteme.")
        return 2
    else:
        print(f"\n❌ HATA: {a} + {b} hesaplanamaz!")
        print("Bu makine sadece 1+1 hesaplar. Çünkü öyle yazıldı.")
        print("Sonsuz döngüye giriyorum... Ctrl+C ile kurtulabilirsin belki.")
        sayac = 0
        while True:
            sayac += 1
            print(f"Hala bekliyorum... ({sayac} saniyedir)", end="\r")
            time.sleep(1)
            if sayac % 100 == 0:
                print("\n(Hala burada. Vazgeçmedin mi?)")

if __name__ == "__main__":
    print("=" * 50)
    print("   SADECE 1+1 HESAPLAYAN SONSUZ MAKİNE")
    print("   v1.0 - Çalışır, ama çalışmaz gibi")
    print("=" * 50)
    print()
    
    try:
        a = int(input("İlk sayıyı gir (umarım 1): "))
        b = int(input("İkinci sayıyı gir (yine 1 olsun): "))
        sonuc = hesapla(a, b)
        print(f"\nSonuç: {sonuc}")
    except ValueError:
        print("\nSadece sayı gir! Bu makine harfleri sevmez.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nKaçtın. İyi yaptın.")
        sys.exit(0)
