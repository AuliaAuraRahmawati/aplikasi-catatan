# Aplikasi Catatan Belajar Sederhana

# List untuk menyimpan semua catatan
catatan = []

# Fitur pengembangan mandiri: Target harian
target_harian = 0  # Dalam menit

def tambah_catatan():
    """
    Fungsi untuk menambah catatan belajar baru.
    Meminta input: mapel, topik, dan durasi belajar (menit)
    """
    print("\n--- Tambah Catatan Baru ---")
    
    # Meminta input dari pengguna
    mapel = input("Nama mata pelajaran: ")
    topik = input("Topik belajar: ")
    durasi = input("Durasi belajar (menit): ")
    
    # Membuat catatan baru dalam bentuk dictionary
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    
    # Menambahkan catatan ke dalam list
    catatan.append(catatan_baru)
    
    print("✓ Catatan berhasil ditambahkan!")

def lihat_catatan():
    """Fungsi untuk melihat semua catatan"""
    print("\n" + "="*50)
    print("             📚 DAFTAR CATATAN BELAJAR")
    print("="*50)
    
    # Cek apakah ada catatan atau tidak
    if len(catatan) == 0:
        print("\n⚠️  Belum ada catatan belajar.")
        print("Mulai tambahkan catatan untuk melacak aktivitas belajar Anda!\n")
        return
    
    # Menampilkan semua catatan
    total_menit = 0
    for i, item in enumerate(catatan, 1):
        print(f"\n{i}. 📖 Mapel: {item['mapel']}")
        print(f"   📝 Topik: {item['topik']}")
        print(f"   ⏱️  Durasi: {item['durasi']} menit")
        print("   " + "-"*46)
        
        # Hitung total durasi (jika input berupa angka)
        try:
            total_menit += int(item['durasi'])
        except ValueError:
            pass
    
    # Menampilkan ringkasan
    print(f"\n📊 RINGKASAN:")
    print(f"   Total catatan: {len(catatan)}")
    print(f"   Total waktu belajar: {total_menit} menit")
    print("="*50 + "\n")

def total_waktu():
    """Fungsi untuk menghitung total durasi belajar dari semua catatan"""
    print("\n" + "="*50)
    print("          ⏱️  TOTAL WAKTU BELAJAR")
    print("="*50)
    
    # Cek apakah ada catatan
    if len(catatan) == 0:
        print("\n❌ Belum ada catatan untuk dihitung.")
        print("="*50 + "\n")
        return 0
    
    # Hitung total durasi
    total_menit = 0
    durasi_valid = 0
    
    for item in catatan:
        try:
            durasi = int(item['durasi'])
            total_menit += durasi
            durasi_valid += 1
        except ValueError:
            print(f"⚠️  Catatan '{item['mapel']}' memiliki durasi yang tidak valid")
    
    # Konversi ke jam dan menit untuk tampilan yang lebih informatif
    jam = total_menit // 60
    menit = total_menit % 60
    
    # Menampilkan hasil
    print(f"\n📈 HASIL PERHITUNGAN:")
    print(f"   Total catatan: {len(catatan)}")
    print(f"   Catatan dengan durasi valid: {durasi_valid}")
    print(f"   Total waktu belajar: {total_menit} menit")
    
    if jam > 0:
        print(f"   Atau: {jam} jam {menit} menit")
    
    print(f"\n💡 Rata-rata per catatan: {total_menit // len(catatan)} menit")
    print("="*50 + "\n")
    
    return total_menit

def atur_target_harian():
    """Fungsi untuk mengatur target waktu belajar harian"""
    global target_harian
    
    print("\n" + "="*50)
    print("         🎯 ATUR TARGET BELAJAR HARIAN")
    print("="*50)
    
    if target_harian > 0:
        jam_current = target_harian // 60
        menit_current = target_harian % 60
        print(f"\n📍 Target harian saat ini: {target_harian} menit")
        if jam_current > 0:
            print(f"   ({jam_current} jam {menit_current} menit)")
    else:
        print("\n❌ Belum ada target harian yang ditetapkan")
    
    try:
        target_baru = int(input("\nMasukkan target waktu belajar harian (menit): "))
        
        if target_baru < 0:
            print("❌ Target harus berupa angka positif!")
            return
        
        target_harian = target_baru
        jam = target_baru // 60
        menit = target_baru % 60
        
        print(f"\n✅ Target berhasil diatur!")
        print(f"   Target: {target_baru} menit", end="")
        if jam > 0:
            print(f" ({jam} jam {menit} menit)")
        else:
            print()
        print("="*50 + "\n")
        
    except ValueError:
        print("❌ Input harus berupa angka!")
        print("="*50 + "\n")

def lihat_progress_harian():
    """Fungsi untuk melihat progress pembelajaran vs target harian"""
    print("\n" + "="*50)
    print("      📊 PROGRESS BELAJAR vs TARGET HARIAN")
    print("="*50)
    
    if target_harian == 0:
        print("\n⚠️  Belum ada target harian yang ditetapkan.")
        print("Silakan atur target terlebih dahulu di menu 'Atur Target'.\n")
        return
    
    # Hitung total waktu belajar hari ini
    total_menit = 0
    for item in catatan:
        try:
            total_menit += int(item['durasi'])
        except ValueError:
            pass
    
    # Konversi target ke jam dan menit
    target_jam = target_harian // 60
    target_menit = target_harian % 60
    
    # Konversi actual ke jam dan menit
    actual_jam = total_menit // 60
    actual_menit = total_menit % 60
    
    # Hitung progress
    if target_harian > 0:
        persentase = (total_menit / target_harian) * 100
    else:
        persentase = 0
    
    # Tampilkan informasi
    print(f"\n🎯 TARGET HARIAN: {target_harian} menit ({target_jam}j {target_menit}m)")
    print(f"✅ WAKTU BELAJAR HARI INI: {total_menit} menit ({actual_jam}j {actual_menit}m)")
    print(f"\n📈 PROGRESS: {persentase:.1f}%")
    
    # Visualisasi progress bar
    bar_length = 30
    filled = int(bar_length * total_menit / target_harian) if target_harian > 0 else 0
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n   [{bar}]")
    
    # Status
    print("\n💬 STATUS:")
    if total_menit >= target_harian:
        sisa = total_menit - target_harian
        print(f"   ✨ Excellent! Anda sudah melampaui target sebesar {sisa} menit!")
    else:
        sisa = target_harian - total_menit
        jam_sisa = sisa // 60
        menit_sisa = sisa % 60
        print(f"   ⏳ Perlu tambahan {sisa} menit ({jam_sisa}j {menit_sisa}m) untuk mencapai target")
    
    print("="*50 + "\n")

def main():
    """Fungsi utama untuk menjalankan aplikasi"""
    while True:
        print("\n=== Aplikasi Catatan Belajar ===")
        print("1. Tambah Catatan")
        print("2. Lihat Catatan")
        print("3. Total Waktu Belajar")
        print("4. Atur Target Harian")
        print("5. Lihat Progress Harian")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            tambah_catatan()
        elif pilihan == "2":
            lihat_catatan()
        elif pilihan == "3":
            total_waktu()
        elif pilihan == "4":
            atur_target_harian()
        elif pilihan == "5":
            lihat_progress_harian()
        elif pilihan == "6":
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid!")

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
