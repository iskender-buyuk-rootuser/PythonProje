def start():
    ok = "[ OK ] "
    fail = "[ FAIL ] "

    
    boot_liste = [
        ok + "Kernel yüklendi",
        ok + "Bellek kontrolü tamamlandı",
        ok + "Dosya sistemi bağlandı",
        fail + "Bluetooth servisi başlatılamadı",
        ok + "Ağ yapılandırması aktif",
        ok + "Grafik arayüzü hazır",
        ok + "Kullanıcı izinleri kontrol edildi",
        fail + "Ses sürücüsü yüklenemedi",
        ok + "Güvenlik duvarı çalışıyor",
        ok + "Sistem saati senkronize edildi"
    ]

    
    for mesaj in boot_liste:
        print(mesaj)

