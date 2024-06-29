import os
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip


def fetch_streams():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Uyarı", "Lütfen bir YouTube video URL'si girin.")
        return

    try:
        yt = YouTube(url)
        video_streams = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc()
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()

        # Stream bilgilerini ve çözünürlüklerini sakla
        stream_options = []
        for stream in video_streams:
            stream_options.append((stream.resolution, stream))

        # Açılır menüyü güncelle
        quality_var.set("")
        quality_menu['menu'].delete(0, 'end')
        for res, stream in stream_options:
            quality_menu['menu'].add_command(label=res, command=tk._setit(quality_var, res))

        # İndir butonunu aktif hale getir
        download_button.config(state=tk.NORMAL)

        # Streamleri ve ses akışını global olarak sakla
        global video_streams_global, audio_stream_global
        video_streams_global = dict(stream_options)
        audio_stream_global = audio_stream

    except Exception as e:
        messagebox.showerror("Hata", f"Video akışları alınamadı: {str(e)}")


def download_video():
    url = url_entry.get()
    selected_quality = quality_var.get()
    if not url or not selected_quality:
        messagebox.showwarning("Uyarı", "Lütfen bir YouTube video URL'si girin ve bir kalite seçin.")
        return

    try:
        yt = YouTube(url)
        desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        download_path = os.path.join(desktop_path, 'İndirilenler')
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Seçilen kalitedeki video akışını indir
        video_stream = video_streams_global[selected_quality]
        video_path = video_stream.download(output_path=download_path, filename='video.mp4')

        # Ses akışını indir
        audio_path = audio_stream_global.download(output_path=download_path, filename='audio.mp4')

        # Video ve ses akışlarını birleştir
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        final_clip = video_clip.set_audio(audio_clip)
        final_clip_path = os.path.join(download_path, 'final_video.mp4')
        final_clip.write_videofile(final_clip_path)

        # Geçici dosyaları sil
        os.remove(video_path)
        os.remove(audio_path)

        messagebox.showinfo("Başarılı", f"Video başarıyla {final_clip_path} klasörüne indirildi.")

        # Giriş alanlarını sıfırla
        url_entry.delete(0, tk.END)
        quality_var.set("")
        quality_menu['menu'].delete(0, 'end')
        download_button.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Hata", f"Video indirilemedi: {str(e)}")


# Tkinter arayüzünü oluşturma
root = tk.Tk()
root.title("YouTube Video İndirici")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg='#f2f2f2')

# Başlık
header = tk.Label(root, text="YouTube Video İndirici", font=("Helvetica", 16, "bold"), bg='#ff6666', fg='white')
header.pack(pady=10, fill=tk.X)

# URL Girişi
tk.Label(root, text="YouTube Video URL", bg='#f2f2f2').pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Akışları Al Butonu
fetch_button = tk.Button(root, text="Akışları Al", command=fetch_streams, fg='black',
                         font=("Helvetica", 10, "bold"))
fetch_button.pack(pady=5)

# Kalite Seçimi
tk.Label(root, text="Kalite Seçin", bg='#f2f2f2').pack(pady=5)
quality_var = StringVar()
quality_menu = OptionMenu(root, quality_var, "")
quality_menu.pack(pady=5)

# İndir Butonu
download_button = tk.Button(root, text="İndir", command=download_video, state=tk.DISABLED, fg='black',
                            font=("Helvetica", 10, "bold"))
download_button.pack(pady=20)

# Animasyon Etiketi
animation_label = tk.Label(root, text="✨💫🌟🎉", font=("Helvetica", 20), fg='#ff6666')
animation_label.pack(pady=5)

root.mainloop()
