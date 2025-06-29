"Nama: Ahmad Khoerudin"
"NIM: 122203003"
"Mata Kuliah: Pemrograman Asinkron"
"Tugas: Ujian Akhir Semester"
"Dosen Pengajar: Donny Maulana, S.Kom., MMSI"

# 2. Program FastAPI yang menangani permintaan POST async

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn
import asyncio

# Inisialisasi FastAPI app
app = FastAPI(title="Async POST Handler", description="FastAPI dengan async POST endpoints")

# Model untuk request body
class UserData(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    city: Optional[str] = None

class MessageData(BaseModel):
    title: str
    content: str
    priority: Optional[str] = "normal"

# Simulasi database (dalam memori)
users_db = []
messages_db = []

# Fungsi async untuk simulasi operasi database yang lambat
async def simulate_db_operation(delay: float = 1.0):
    """Simulasi operasi database yang membutuhkan waktu"""
    await asyncio.sleep(delay)
    return True

# Endpoint POST untuk menambah user
@app.post("/users", response_model=dict)
async def create_user(user: UserData):
    """
    Endpoint async untuk membuat user baru
    """
    print(f"📝 Memproses pembuatan user: {user.name}")
    
    # Simulasi operasi async (misalnya menyimpan ke database)
    await simulate_db_operation(0.5)
    
    # Validasi email unik
    for existing_user in users_db:
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email sudah terdaftar")
    
    # Buat user baru
    new_user = {
        "id": len(users_db) + 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "city": user.city
    }
    
    users_db.append(new_user)
    
    print(f"✅ User berhasil dibuat: {new_user}")
    
    return {
        "message": "User berhasil dibuat",
        "user": new_user,
        "total_users": len(users_db)
    }

# Endpoint POST untuk menambah pesan
@app.post("/messages", response_model=dict)
async def create_message(message: MessageData):
    """
    Endpoint async untuk membuat pesan baru
    """
    print(f"📨 Memproses pembuatan pesan: {message.title}")
    
    # Simulasi operasi async yang lebih lama untuk pesan prioritas tinggi
    delay = 1.5 if message.priority == "high" else 0.3
    await simulate_db_operation(delay)
    
    # Buat pesan baru
    new_message = {
        "id": len(messages_db) + 1,
        "title": message.title,
        "content": message.content,
        "priority": message.priority,
        "timestamp": "2024-01-01T10:00:00Z"  # Dalam implementasi nyata, gunakan datetime.now()
    }
    
    messages_db.append(new_message)
    
    print(f"✅ Pesan berhasil dibuat: {new_message}")
    
    return {
        "message": "Pesan berhasil dibuat",
        "data": new_message,
        "total_messages": len(messages_db)
    }

# Endpoint GET untuk melihat semua users
@app.get("/users")
async def get_users():
    """Mendapatkan semua users"""
    await simulate_db_operation(0.2)
    return {"users": users_db, "total": len(users_db)}

# Endpoint GET untuk melihat semua messages
@app.get("/messages")
async def get_messages():
    """Mendapatkan semua messages"""
    await simulate_db_operation(0.2)
    return {"messages": messages_db, "total": len(messages_db)}

# Endpoint POST untuk operasi batch
@app.post("/batch-operation")
async def batch_operation(data: Dict[str, Any]):
    """
    Endpoint untuk operasi batch async
    """
    print("🔄 Memulai operasi batch...")
    
    # Simulasi multiple operasi async secara parallel
    tasks = []
    for i in range(3):
        tasks.append(simulate_db_operation(0.5))
    
    # Jalankan semua operasi secara bersamaan
    await asyncio.gather(*tasks)
    
    print("✅ Operasi batch selesai")
    
    return {
        "message": "Operasi batch berhasil",
        "operations_completed": len(tasks),
        "data_received": data
    }

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "FastAPI Async POST Handler",
        "endpoints": [
            "POST /users - Buat user baru",
            "POST /messages - Buat pesan baru", 
            "POST /batch-operation - Operasi batch",
            "GET /users - Lihat semua users",
            "GET /messages - Lihat semua messages"
        ]
    }

# Cara menjalankan server
if __name__ == "__main__":
    print("🚀 Menjalankan FastAPI server...")
    print("📍 Server akan berjalan di: http://localhost:8000")
    print("📖 Dokumentasi API: http://localhost:8000/docs")
    print("🔧 Untuk menjalankan: pip install fastapi uvicorn")
    print("\nContoh POST request:")
    print("curl -X POST http://localhost:8000/users \\")
    print('  -H "Content-Type: application/json" \\')
    print('  -d \'{"name": "John Doe", "email": "john@example.com", "age": 25}\'')
    
    # Uncomment baris di bawah untuk menjalankan server
    # uvicorn.run(app, host="0.0.0.0", port=8000)
