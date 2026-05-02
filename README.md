# 🔍 Network Port Scanner

Hedef sistemlerdeki açık portları hızlı ve verimli şekilde tespit eden Python tabanlı bir ağ tarama aracı.

## 🚀 Özellikler

- Multithreaded yapı ile hızlı tarama (100 eş zamanlı thread)
- TCP port tarama
- Otomatik servis adı tespiti (HTTP, FTP, SSH vb.)
- Domain ve IP adresi desteği
- Özelleştirilebilir port aralığı

## 📦 Kurulum

```bash
git clone https://github.com/Gasimoff-M/network-port-scanner
cd network-port-scanner
python port_scanner.py
```

> Python 3.x gereklidir. Harici kütüphane gerekmez.

## 💻 Kullanım

```
╔══════════════════════════════════════╗
║       Network Port Scanner v1.0      ║
║       github.com/Gasimoff-M          ║
╚══════════════════════════════════════╝

  Hedef IP veya domain girin: scanme.nmap.org
  Başlangıç portu [1]: 1
  Bitiş portu [1024]: 1024
```

## 📊 Örnek Çıktı

```
=======================================================
  Hedef    : 45.33.32.156
  Port Aralığı: 1 - 1024
  Başlangıç: 14:23:01
=======================================================

  [+] Port    22 AÇIK  -->  Servis: ssh
  [+] Port    80 AÇIK  -->  Servis: http

=======================================================
  Tarama Tamamlandı: 14:23:09
  Toplam Açık Port : 2
  Açık Portlar     : [22, 80]
=======================================================
```

## ⚠️ Yasal Uyarı

Bu araç yalnızca **eğitim amaçlı** ve **izin verilen sistemlerde** kullanım içindir.
İzinsiz sistemleri taramak yasadışıdır.

## 👤 Geliştirici

**Gasimoff-M** — [github.com/Gasimoff-M](https://github.com/Gasimoff-M)
