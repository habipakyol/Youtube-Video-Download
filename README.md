# 🎥 YouTube Video Downloader

## Proje Tanıtımı
YouTube Video Downloader, YouTube'dan video indirmenize olanak tanıyan bir Python uygulamasıdır. Bu projeyi kullanarak, YouTube videolarını istediğiniz kalitede indirebilirsiniz.

## Özellikler

- **Basit ve Kullanıcı Dostu Arayüz:** Uygulama, kolayca gezinebilen bir grafik kullanıcı arayüzü ile birlikte gelir.
- **Yüksek Kaliteli Video İndirmeleri:** Videoları çeşitli çözünürlük ve formatlarda indirin.
- **Hata Yönetimi:** Sorunsuz bir işlem sağlamak için güçlü hata yönetimi.
- **Çapraz Platform:** Uygulama, Windows, MacOS ve Linux dahil olmak üzere çeşitli işletim sistemlerinde çalıştırılabilir.

## Başlarken 🚀

### Gereksinimler 📋
Bu projeyi çalıştırabilmek için aşağıdaki yazılımlara ve kütüphanelere ihtiyacınız olacaktır:

- Python 3.6 veya daha üstü
- `pytube` kütüphanesi
- `requests` kütüphanesi
- `PyInstaller` kütüphanesi

### Kurulum 🛠️
Proje dosyalarını bilgisayarınıza indirdikten sonra, gerekli Python kütüphanelerini aşağıdaki komutlarla kurabilirsiniz:

    
    pip install pytube
    pip install requests
    pip install pyinstaller
### Kullanım 📹
Uygulamayı çalıştırmak için aşağıdaki adımları izleyin:

youtube_video_downloader.py dosyasını çalıştırın.
İndirmek istediğiniz YouTube videosunun URL'sini girin.
İndirme işlemi tamamlandığında video belirtilen dizine kaydedilecektir.
Örnek kullanım:

    
    python youtube_video_downloader.py
Uygulama, sizden bir YouTube video URL'si girmenizi isteyecek ve ardından videoyu indirecektir.

### Exe Dosyası Oluşturma 🖥️
Bu uygulamayı bir exe dosyasına dönüştürmek için aşağıdaki adımları izleyin:

pyinstaller kullanarak Python betiğinizi paketleyin:

    
    pyinstaller --onefile --windowed --debug=all youtube_video_downloader.py
Bu komut, proje klasörünüzde youtube_video_downloader.spec dosyasını oluşturacaktır.

Exe dosyasını oluşturmak için aşağıdaki komutu çalıştırın:

    
    pyinstaller youtube_video_downloader.spec
Bu işlem tamamlandığında, dist klasöründe çalıştırılabilir bir exe dosyası oluşturulacaktır.

### Katkı Yapma 🤝
Bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

• Bu repoyu fork edin.

• Yeni bir branş oluşturun: git checkout -b feature/AmazingFeature.

• Değişikliklerinizi commit edin: git commit -m 'Add some AmazingFeature'.

• Branşınıza push edin: git push origin feature/AmazingFeature.

• Bir Pull Request oluşturun.

### Lisans 📄

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylı bilgi için [LICENSE](./License) dosyasına bakabilirsiniz.


