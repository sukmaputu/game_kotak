import pygame
import random

# 1. Inisialisasi Pygame
pygame.init()

# 2. Pengaturan Layar
lebar_layar = 800
tinggi_layar = 600
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Game Kumpulkan Makanan")

# 3. Warna (RGB)
putih = (255, 255, 255)
hitam = (0, 0, 0)
merah = (255, 0, 0)
hijau = (0, 255, 0)
biru = (0, 0, 255)

# 4. Pengaturan Pemain
pemain_lebar = 50
pemain_tinggi = 50
pemain_x = (lebar_layar - pemain_lebar) // 2
pemain_y = tinggi_layar - pemain_tinggi - 10 # Sedikit di atas bagian bawah
pemain_kecepatan = 7 # Piksel per frame

# 5. Pengaturan Makanan
makanan_lebar = 30
makanan_tinggi = 30
makanan_x = random.randint(0, lebar_layar - makanan_lebar)
makanan_y = random.randint(0, tinggi_layar - makanan_tinggi - 100) # Biar tidak terlalu dekat bawah

# 6. Skor
skor = 0
font = pygame.font.Font(None, 36) # Font default, ukuran 36

# 7. Game Loop
berjalan = True
clock = pygame.time.Clock() # Untuk mengatur FPS

while berjalan:
    # 7.1. Event Handling (Input dari pengguna)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Jika tombol close (X) diklik
            berjalan = False

    # 7.2. Kontrol Pemain
    keys = pygame.key.get_pressed() # Mendapatkan status semua tombol keyboard
    if keys[pygame.K_LEFT] and pemain_x > 0:
        pemain_x -= pemain_kecepatan
    if keys[pygame.K_RIGHT] and pemain_x < lebar_layar - pemain_lebar:
        pemain_x += pemain_kecepatan
    if keys[pygame.K_UP] and pemain_y > 0:
        pemain_y -= pemain_kecepatan
    if keys[pygame.K_DOWN] and pemain_y < tinggi_layar - pemain_tinggi:
        pemain_y += pemain_kecepatan

    # 7.3. Logika Game
    # Buat Rect untuk pemain dan makanan untuk deteksi tabrakan
    rect_pemain = pygame.Rect(pemain_x, pemain_y, pemain_lebar, pemain_tinggi)
    rect_makanan = pygame.Rect(makanan_x, makanan_y, makanan_lebar, makanan_tinggi)

    # Deteksi tabrakan
    if rect_pemain.colliderect(rect_makanan):
        skor += 1
        # Pindahkan makanan ke posisi acak baru
        makanan_x = random.randint(0, lebar_layar - makanan_lebar)
        makanan_y = random.randint(0, tinggi_layar - makanan_tinggi - 100)
        print(f"Skor: {skor}") # Cetak skor ke konsol juga (opsional)

    # 7.4. Menggambar ke Layar
    layar.fill(hitam) # Isi layar dengan warna hitam (background)

    # Gambar pemain
    pygame.draw.rect(layar, biru, (pemain_x, pemain_y, pemain_lebar, pemain_tinggi))

    # Gambar makanan
    pygame.draw.rect(layar, hijau, (makanan_x, makanan_y, makanan_lebar, makanan_tinggi))

    # Tampilkan skor
    teks_skor = font.render(f"Skor: {skor}", True, putih) # True untuk anti-aliasing
    layar.blit(teks_skor, (10, 10)) # Posisi teks skor di kiri atas

    # 7.5. Update Tampilan
    pygame.display.flip() # Atau pygame.display.update()

    # 7.6. Atur FPS (Frames Per Second)
    clock.tick(60) # Batasi game agar berjalan pada 60 FPS

# 8. Keluar dari Pygame
pygame.quit()