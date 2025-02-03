# 📊 Tugas Praktikum Pengenalan Pola

Repositori ini berisi kode Python untuk tugas praktikum **Pengenalan Pola**, yang mencakup operasi dasar dengan **vektor**, **matriks**, **list**, **DataFrame**, **pengolahan file**, serta **pengolahan gambar menggunakan OpenCV**.

---

## 🚀 Demo 
🔗 **[Klik di sini untuk mencoba di Google Colab](https://colab.research.google.com/drive/1pMM9H0snQxzrJZcCN41Uis_mOXczo0vZ?usp=sharing)**

---

## ✨ Fitur Utama
✅ **Vektor & Matriks**: Operasi dasar menggunakan NumPy.  
✅ **List & DataFrame**: Manipulasi data dengan Pandas.  
✅ **Membaca Data dari Berbagai Sumber**:
   - File CSV  
   - File teks dengan delimiter  
   - URL  
✅ **Visualisasi Data**: Menampilkan data web traffic dengan Matplotlib.  
✅ **Pengolahan Gambar**:
   - Membaca gambar dengan OpenCV  
   - Konversi ke grayscale  
   - Menampilkan nilai piksel gambar  

---

## 📦 Instalasi & Persiapan
Pastikan Anda memiliki **Python** dan pustaka berikut sudah terinstal:

```bash
Struktur Direktori :
📂 tugas-prak-pola-1
│── 📄 README.md
│── 📜 main.py
│── 📂 datasets
│   ├── Data.csv
│   ├── Data.txt
│   ├── web_traffic.tsv
│   ├── ipb.png
│   ├── 5.png

Requirements : 
pip install -r requirements.txt

Cara Menjalankan : 
python main.py

-- main.py → File utama yang berisi kode program.
-- datasets/ → Folder yang berisi dataset dalam berbagai format.
-- README.md → File Markdown (Penjelasan Program)

📌 Penjelasan Program
Vektor & Matriks:
- Membuat vektor menggunakan np.arange()
- Membentuk matriks 2D dari vektor 1D menggunakan .reshape()

List & DataFrame:
- Membuat list dengan berbagai tipe data.
- Membuat DataFrame dengan Pandas.
- Membaca Data dari Berbagai Sumber:
- Membaca CSV dengan pd.read_csv()
- Membaca file teks menggunakan open()
- Membaca data dari URL dengan pd.read_csv()

Visualisasi Web Traffic:
- Menggunakan plt.scatter() untuk memvisualisasikan jumlah pengunjung web.

Pengolahan Gambar dengan OpenCV:
- Membaca gambar menggunakan OpenCV cv2.imread()
- Menampilkan gambar dengan Matplotlib
- Mengonversi gambar menjadi grayscale
- Mengakses nilai piksel gambar tertentu.
```
---

### 🤝 Kontribusi & Dukungan
- Jika proyek ini bermanfaat, **jangan lupa beri ⭐ di repository ini!**
- Saran dan kontribusi selalu diterima! Silakan buat **Pull Request** atau diskusi di **Issues**.

---

