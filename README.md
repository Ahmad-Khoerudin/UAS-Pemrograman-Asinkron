**UAS No.1: Async URL Fetcher**

Deskripsi

Program ini mendemonstrasikan pengambilan data dari multiple URLs secara paralel menggunakan asyncio dan aiohttp. Program menunjukkan efisiensi pemrograman asinkron dibandingkan dengan pendekatan sekuensial.

Fitur Utama

- ✅ Pengambilan data dari 3 URL secara paralel
- ⏱️ Pengukuran waktu eksekusi total
- 🛡️ Error handling untuk setiap request
- 📊 Ringkasan hasil dengan status code dan panjang konten
- 🎯 Preview konten yang diambil (200 karakter pertama)

URLs yang Digunakan

- https://jsonplaceholder.typicode.com/posts/1
- https://jsonplaceholder.typicode.com/users/1
- https://jsonplaceholder.typicode.com/comments/1

Cara Menjalankan

    Install dependencies
    pip install aiohttp
    
    Jalankan program
    python "UAS No.1.py"

Output yang Diharapkan

- 🚀 Memulai pengambilan data secara parallel...
- ✅ Data berhasil diambil dari https://jsonplaceholder.typicode.com/posts/1
- Status Code: 200
- Content Length: xxx characters
--------------------------------------------------
- ⏱️ Total waktu eksekusi: x.xx detik

📊 RINGKASAN HASIL:
1. https://jsonplaceholder.typicode.com/posts/1 - Status: 200 ✅
2. https://jsonplaceholder.typicode.com/users/1 - Status: 200 ✅
3. https://jsonplaceholder.typicode.com/comments/1 - Status: 200 ✅

**UAS No.2: FastAPI Async Server**

Deskripsi

Program ini adalah implementasi FastAPI server dengan multiple endpoints yang menangani operasi POST secara asinkron. Server ini mendemonstrasikan penggunaan async/await dalam web development.

Fitur Utama

- 🌐 RESTful API dengan multiple endpoints
- 📝 Validasi data menggunakan Pydantic models
- 💾 Simulasi operasi database asinkron
- 🔄 Operasi batch dengan parallel processing
- 📋 Auto-generated API documentation
- ⚡ Non-blocking I/O operations

Cara Menjalankan

    bash# Install dependencies
    pip install fastapi uvicorn

    # Jalankan server (uncomment baris terakhir di file)
    python "UAS No.2.py"

    # Atau jalankan dengan uvicorn langsung
    uvicorn UAS_No_2:app --host 0.0.0.0 --port 8000

Akses API

- Server URL: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc


**Proyek ini dibuat sebagai tugas akademik dari mata kuliah pemrograman asinkron**
