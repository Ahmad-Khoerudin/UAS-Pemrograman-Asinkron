"Nama: Ahmad Khoerudin"
"NIM: 122203003"
"Mata Kuliah: Pemrograman Asinkron"
"Tugas: Ujian Akhir Semester"
"Dosen Pengajar: Donny Maulana, S.Kom., MMSI"

# 1. Program Async untuk mengambil data dari 3 URL secara parallel

import asyncio
import aiohttp
import time

async def fetch_data(session, url):
    """Fungsi untuk mengambil data dari satu URL"""
    try:
        async with session.get(url) as response:
            data = await response.text()
            print(f"✅ Data berhasil diambil dari {url}")
            print(f"Status Code: {response.status}")
            print(f"Content Length: {len(data)} characters")
            print("-" * 50)
            return {"url": url, "status": response.status, "data": data[:200] + "..." if len(data) > 200 else data}
    except Exception as e:
        print(f"❌ Error mengambil data dari {url}: {str(e)}")
        return {"url": url, "status": "error", "error": str(e)}

async def fetch_multiple_urls(urls):
    """Fungsi untuk mengambil data dari multiple URLs secara parallel"""
    print("🚀 Memulai pengambilan data secara parallel...")
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        # Membuat tasks untuk semua URL secara bersamaan
        tasks = [fetch_data(session, url) for url in urls]
        
        # Menjalankan semua tasks secara parallel
        results = await asyncio.gather(*tasks, return_exceptions=True)
    
    end_time = time.time()
    print(f"⏱️ Total waktu eksekusi: {end_time - start_time:.2f} detik")
    
    return results

# Contoh penggunaan
async def main():
    # Daftar URL untuk diambil datanya
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/users/1", 
        "https://jsonplaceholder.typicode.com/comments/1"
    ]
    
    results = await fetch_multiple_urls(urls)
    
    print("\n📊 RINGKASAN HASIL:")
    for i, result in enumerate(results, 1):
        if isinstance(result, dict) and "error" not in result:
            print(f"{i}. {result['url']} - Status: {result['status']} ✅")
        else:
            print(f"{i}. Error occurred ❌")

# Jalankan program
if __name__ == "__main__":
    # Untuk menjalankan: pip install aiohttp
    asyncio.run(main())

print("\n" + "="*80 + "\n")
