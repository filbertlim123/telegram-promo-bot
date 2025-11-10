import time
import requests
import os

# ======== KONFIGURASI =========
TOKEN = "8377497750:AAF0adxWvEJC3CylgnqJpu9wE5kHf9NofK4"  # token bot kamu
CHAT_ID = "-1003292398196"  # ganti dengan chat_id grup kamu (pakai tanda minus)
INTERVAL = 300  # 300 detik = 5 menit
# ==========================================

# Daftar promosi (setiap item berisi teks dan gambar)
promosi_list = [
    {
        "text": (
            "POLA KODE JP GET OLYMPUS SUPER SCATTER : PRAGMATIC PLAY\n"
            "➡️ ✅❌✅ 10X SPIN OTOMATIS ==> DC OFF\n"
            "➡️ ✅❌❌ 30X SPIN MANUAL ==> DC OFF\n"
            "➡️ ❌✅✅ 50X SPIN OTOMATIS ==> DC ON\n"
            "➡️ ❌❌❌ 10X SPIN MANUAL ==> DC ON\n"
            "Bet: 800 - 2000\n"
            "DEPOSIT DENGAN KODE JP 100.544 DAN POTENSI JP Rp.10.000.000\n"
            "📱 𝙇𝙄𝙉𝙆 𝘿𝘼𝙁𝙏𝘼𝙍 : https://joyme.io/@pwktoto"
        ),
        "image": r"C:\Users\PC\Downloads\Untitled design (2).png"
    },
    {
        "text": (
            "🎯 Wajib Coba Hari Ini, Bang!\n"
            "Slot lagi gacor banget — bandar ngasih terus-terusan! 💸🔥\n"
            "Kesempatan langka jangan disia-siain~\n"
            "👇 Buruan join & ambil rezekimu sekarang juga!\n"
            "📱 𝙇𝙄𝙉𝙆 𝘿𝘼𝙁𝙏𝘼𝙍 : https://mez.ink/pwktoto"
        ),
        "image": r"C:\Users\PC\Documents\Promo PWK (7).png"
    },
    {
        "text": (
            "💡 PROMO 3 💡\n"
            "Beli 1 dapat 2 untuk produk elektronik pilihan!\n"
            "🔌 Lihat sekarang: https://tokoku.com/elektronik"
        ),
        "image": "https://example.com/elektronik.jpg"
    },
    {
        "text": (
            "🌈 PROMO 4 🌈\n"
            "Voucher Rp25.000 untuk pengguna baru!\n"
            "🎁 Klaim di: https://tokoku.com/voucher"
        ),
        "image": "https://example.com/voucher.jpg"
    },
    {
        "text": (
            "🎉 PROMO 5 🎉\n"
            "Diskon besar-besaran akhir pekan ini!\n"
            "🔥 Buruan: https://tokoku.com/superdeal"
        ),
        "image": "https://example.com/superdeal.jpg"
    }
]

# ==========================================

def kirim_pesan(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    r = requests.post(url, data=data)
    print("📝 Kirim pesan:", r.status_code, r.text)

def kirim_gambar_dari_file(path, caption=None):
    if not os.path.exists(path):
        print("❌ File gambar tidak ditemukan:", path)
        return
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(path, "rb") as img:
        files = {"photo": img}
        data = {"chat_id": CHAT_ID, "caption": caption or ""}
        r = requests.post(url, data=data, files=files)
    print("🖼️ Kirim gambar (lokal):", r.status_code, r.text)

def kirim_gambar_dari_url(photo_url, caption=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    data = {"chat_id": CHAT_ID, "photo": photo_url, "caption": caption or ""}
    r = requests.post(url, data=data)
    print("🌐 Kirim gambar (URL):", r.status_code, r.text)

# ==========================================

if __name__ == "__main__":
    print("🤖 Bot promosi otomatis aktif! Tekan Ctrl+C untuk berhenti.\n")
    index = 0

    while True:
        try:
            promo = promosi_list[index]
            kirim_pesan(promo["text"])

            if os.path.exists(promo["image"]):
                kirim_gambar_dari_file(promo["image"], promo["text"])
            else:
                kirim_gambar_dari_url(promo["image"], promo["text"])

            index = (index + 1) % len(promosi_list)  # loop ke promo berikutnya
        except Exception as e:
            print("⚠️ Terjadi error:", e)

        print(f"Menunggu {INTERVAL/60} menit untuk kirim promo berikutnya...\n")
        time.sleep(INTERVAL)
