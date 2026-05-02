# =====================================================
# Network Port Scanner
# Geliştirici: Gasimoff-M
# Açıklama: Hedef sistemdeki açık portları tespit eder
# =====================================================

import socket
import threading
from datetime import datetime

# Tarama sonuçlarını tutacak liste
acik_portlar = []

# Ekrana yazdırırken karışmaması için kilit
print_lock = threading.Lock()


def port_tara(hedef_ip, port):
    """
    Belirtilen IP ve porta TCP bağlantısı kurmaya çalışır.
    Bağlantı başarılıysa port açıktır.
    """
    try:
        # Yeni bir soket oluştur (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # 1 saniye zaman aşımı

        # Bağlantı deneme: 0 = başarılı, diğer = başarısız
        sonuc = s.connect_ex((hedef_ip, port))

        if sonuc == 0:
            # Servis adını almaya çalış
            try:
                servis = socket.getservbyport(port, "tcp")
            except:
                servis = "bilinmiyor"

            with print_lock:
                print(f"  [+] Port {port:5d} AÇIK  -->  Servis: {servis}")
                acik_portlar.append(port)

        s.close()

    except socket.error:
        pass  # Bağlantı hatası, port kapalı


def tarama_baslat(hedef, baslangic=1, bitis=1024):
    """
    Verilen aralıktaki portları çoklu iş parçacığıyla tarar.
    """
    print("\n" + "=" * 55)
    print(f"  Hedef    : {hedef}")
    print(f"  Port Aralığı: {baslangic} - {bitis}")
    print(f"  Başlangıç: {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 55 + "\n")

    threadler = []

    for port in range(baslangic, bitis + 1):
        # Her port için ayrı bir thread başlat
        t = threading.Thread(target=port_tara, args=(hedef, port))
        threadler.append(t)
        t.start()

        # Aynı anda maksimum 100 thread çalışsın
        if len(threadler) >= 100:
            for t in threadler:
                t.join()
            threadler = []

    # Kalan threadleri bekle
    for t in threadler:
        t.join()

    print("\n" + "=" * 55)
    print(f"  Tarama Tamamlandı: {datetime.now().strftime('%H:%M:%S')}")
    print(f"  Toplam Açık Port : {len(acik_portlar)}")
    if acik_portlar:
        print(f"  Açık Portlar     : {sorted(acik_portlar)}")
    print("=" * 55 + "\n")


# ─── Ana Program ───────────────────────────────────────
if __name__ == "__main__":
    print("\n╔══════════════════════════════════════╗")
    print("║       Network Port Scanner v1.0      ║")
    print("║       github.com/Gasimoff-M          ║")
    print("╚══════════════════════════════════════╝")

    # Kullanıcıdan hedef al
    hedef = input("\n  Hedef IP veya domain girin: ").strip()

    # IP adresine çevir (domain girdiyse)
    try:
        hedef_ip = socket.gethostbyname(hedef)
    except socket.gaierror:
        print("  [!] Geçersiz adres. Lütfen tekrar deneyin.")
        exit()

    # Port aralığını al
    print("  Port aralığı (varsayılan: 1-1024)")
    baslangic = input("  Başlangıç portu [1]: ").strip()
    bitis = input("  Bitiş portu [1024]: ").strip()

    baslangic = int(baslangic) if baslangic.isdigit() else 1
    bitis = int(bitis) if bitis.isdigit() else 1024

    # Taramayı başlat
    tarama_baslat(hedef_ip, baslangic, bitis)
