import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()
pygame.mixer.init()

# Konstanta
WIDTH, HEIGHT = 665, 700  # Lebar dan tinggi window
LINE_WIDTH = 14
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15
SPACE = SQUARE_SIZE // 4
BOARD_OFFSET = 60  # Offset untuk memindahkan papan ke bawah agar tombol tidak menutupi

# Warna dengan efek 3D (highlight dan shadow)
BG_COLOR = (28, 170, 156)  # Hijau biru
LINE_COLOR = (23, 145, 135)
LINE_SHADOW = (10, 100, 100)  # Bayangan garis
CIRCLE_COLOR = (239, 231, 200)
CIRCLE_SHADOW = (200, 190, 150)  # Bayangan lingkaran
CROSS_COLOR = (66, 66, 66)
CROSS_SHADOW = (30, 30, 30)  # Bayangan silang
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (50, 150, 200)
BUTTON_HOVER_COLOR = (70, 170, 220)
BUTTON_SHADOW = (20, 100, 150)  # Bayangan tombol

# Font
FONT = pygame.font.SysFont("comicsansms", 40)
SMALL_FONT = pygame.font.SysFont("comicsansms", 20)

# Sound effects
try:
    win_sound = pygame.mixer.Sound("win.wav.mp3")
except pygame.error:
    win_sound = None
    print("File suara 'win.wav.mp3' tidak ditemukan atau tidak valid. Suara kemenangan tidak akan dimainkan.")

try:
    click_sound = pygame.mixer.Sound("click.wav.mp3")
except pygame.error:
    click_sound = None
    print("File suara 'click.wav.mp3' tidak ditemukan atau tidak valid. Suara klik tidak akan dimainkan.")

# Load background music untuk menu (pastikan file 'menu_music.mp3' ada di direktori yang sama)
try:
    pygame.mixer.music.load("menu_music.mp3")
    music_loaded = True
except pygame.error:
    music_loaded = False
    print("File musik 'menu_music.mp3' tidak ditemukan. Musik tidak akan dimainkan.")

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe 3D Menarik - Pygame")

try:
    menu_bg = pygame.image.load("menu_background.png")
    menu_bg = pygame.transform.scale(menu_bg, (WIDTH, HEIGHT))
    print("Gambar background berhasil dimuat!")  # Tambahkan ini
except pygame.error as e:
    menu_bg = None
    print(f"Gambar background gagal dimuat: {e}")  # Tambahkan ini untuk detail error

# Board
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Player
player = 1  # 1 untuk X, 2 untuk O
game_over = False
winner = 0
sound_played = False

# Skor
score = {"X": 0, "O": 0}

# Nama pemain
player1_name = "X"
player2_name = "O"

# Mode input nama
input_mode = False
current_input = ""
input_for = 1  # 1 untuk player1, 2 untuk player2

# State permainan
current_state = "menu"  # "menu" atau "game"

# Fungsi untuk menggambar gradien background (efek 3D)
def draw_gradient_background():
    for y in range(HEIGHT):
        # Gradien dari atas ke bawah
        r = int(28 + (y / HEIGHT) * 50)  # Dari hijau ke biru lebih gelap
        g = int(170 + (y / HEIGHT) * 50)
        b = int(156 + (y / HEIGHT) * 50)
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

# Fungsi untuk menggambar garis dengan bayangan (efek 3D)
def draw_lines():
    # Bayangan garis (offset sedikit)
    pygame.draw.line(screen, LINE_SHADOW, (2, SQUARE_SIZE + BOARD_OFFSET + 2), (WIDTH + 2, SQUARE_SIZE + BOARD_OFFSET + 2), LINE_WIDTH)
    pygame.draw.line(screen, LINE_SHADOW, (2, 2 * SQUARE_SIZE + BOARD_OFFSET + 2), (WIDTH + 2, 2 * SQUARE_SIZE + BOARD_OFFSET + 2), LINE_WIDTH)
    pygame.draw.line(screen, LINE_SHADOW, (SQUARE_SIZE + 2, BOARD_OFFSET + 2), (SQUARE_SIZE + 2, 3 * SQUARE_SIZE + BOARD_OFFSET + 2), LINE_WIDTH)
    pygame.draw.line(screen, LINE_SHADOW, (2 * SQUARE_SIZE + 2, BOARD_OFFSET + 2), (2 * SQUARE_SIZE + 2, 3 * SQUARE_SIZE + BOARD_OFFSET + 2), LINE_WIDTH)
    
    # Garis utama
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE + BOARD_OFFSET), (WIDTH, SQUARE_SIZE + BOARD_OFFSET), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE + BOARD_OFFSET), (WIDTH, 2 * SQUARE_SIZE + BOARD_OFFSET), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, BOARD_OFFSET), (SQUARE_SIZE, 3 * SQUARE_SIZE + BOARD_OFFSET), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, BOARD_OFFSET), (2 * SQUARE_SIZE, 3 * SQUARE_SIZE + BOARD_OFFSET), LINE_WIDTH)

# Fungsi untuk menggambar figures (X dan O) dengan efek 3D
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                # Bayangan X (offset)
                pygame.draw.line(screen, CROSS_SHADOW, (col * SQUARE_SIZE + SPACE + 3, row * SQUARE_SIZE + SPACE + BOARD_OFFSET + 3), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE + 3, row * SQUARE_SIZE + SQUARE_SIZE - SPACE + BOARD_OFFSET + 3), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_SHADOW, (col * SQUARE_SIZE + SPACE + 3, row * SQUARE_SIZE + SQUARE_SIZE - SPACE + BOARD_OFFSET + 3), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE + 3, row * SQUARE_SIZE + SPACE + BOARD_OFFSET + 3), CROSS_WIDTH)
                # X utama
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE + BOARD_OFFSET), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE + BOARD_OFFSET), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE + BOARD_OFFSET), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE + BOARD_OFFSET), CROSS_WIDTH)
            elif board[row][col] == 2:
                # Bayangan O (lingkaran lebih besar dan gelap)
                pygame.draw.circle(screen, CIRCLE_SHADOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2 + 3, row * SQUARE_SIZE + SQUARE_SIZE // 2 + BOARD_OFFSET + 3), CIRCLE_RADIUS + 2, CIRCLE_WIDTH)
                # O utama
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2 + BOARD_OFFSET), CIRCLE_RADIUS, CIRCLE_WIDTH)

# Fungsi untuk menandai kotak pemenang dengan efek 3D
def mark_win(row, col, player):
    color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
    shadow_color = CROSS_SHADOW if player == 1 else CIRCLE_SHADOW
    # Bayangan
    pygame.draw.rect(screen, shadow_color, (col * SQUARE_SIZE + 3, row * SQUARE_SIZE + BOARD_OFFSET + 3, SQUARE_SIZE, SQUARE_SIZE), 5)
    # Border utama
    pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE + BOARD_OFFSET, SQUARE_SIZE, SQUARE_SIZE), 5)

# Fungsi untuk cek pemenang
def check_win(player):
    # Cek baris
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            mark_win(row, 0, player)
            mark_win(row, 1, player)
            mark_win(row, 2, player)
            return True
    # Cek kolom
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            mark_win(0, col, player)
            mark_win(1, col, player)
            mark_win(2, col, player)
            return True
    # Cek diagonal
    if board[0][0] == board[1][1] == board[2][2] == player:
        mark_win(0, 0, player)
        mark_win(1, 1, player)
        mark_win(2, 2, player)
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        mark_win(0, 2, player)
        mark_win(1, 1, player)
        mark_win(2, 0, player)
        return True
    return False

# Fungsi untuk cek seri
def check_draw():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

# Fungsi untuk reset board
def reset_board():
    global board, player, game_over, winner, sound_played
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 1
    game_over = False
    winner = 0
    sound_played = False

# Fungsi untuk reset skor
def reset_score():
    global score
    score = {"X": 0, "O": 0}

# Fungsi untuk menggambar tombol dengan efek 3D (bayangan dan highlight)
def draw_button(text, x, y, width, height, color, hover_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    # Bayangan tombol
    pygame.draw.rect(screen, BUTTON_SHADOW, (x + 3, y + 3, width, height))
    
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1:
            if click_sound:
                click_sound.play()
            return True
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))
    
    text_surf = SMALL_FONT.render(text, True, TEXT_COLOR)
    screen.blit(text_surf, (x + (width - text_surf.get_width()) // 2, y + (height - text_surf.get_height()) // 2))
    return False

# Fungsi untuk menggambar menu utama
def draw_menu():
    # Gambar background gambar jika ada, atau gradien sebagai fallback
    if menu_bg:
        screen.blit(menu_bg, (0, 0))
    else:
        draw_gradient_background()  # Fallback ke gradien jika gambar tidak ada
    
    # Judul
    title_text = FONT.render("Tic Tac Toe WIN", True, TEXT_COLOR)
    title_shadow = FONT.render("Tic Tac Toe WIN", True, (0, 0, 0))
    screen.blit(title_shadow, (WIDTH // 2 - title_shadow.get_width() // 2 + 2, HEIGHT // 2 - 150 + 2))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 150))
    
    # Tombol Start Game
    if draw_button("Start Game", WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR):
        global current_state
        current_state = "game"
        reset_board()  # Reset board saat mulai game baru
    
    # Tombol Set Names
    if draw_button("Set Names", WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR):
        global input_mode, input_for, current_input
        input_mode = True
        input_for = 1
        current_input = ""
    
    # Tombol Quit
    if draw_button("Quit", WIDTH // 2 - 100, HEIGHT // 2 + 90, 200, 50, BUTTON_COLOR, BUTTON_HOVER_COLOR):
        pygame.quit()
        sys.exit()

# Loop utama
running = True
while running:
    # Background gradien hanya untuk game, menu menggunakan gambar atau gradien
    if current_state == "game":
        draw_gradient_background()  # Background gradien untuk efek 3D di game
    
    # Handle musik latar belakang
    if current_state == "menu" and music_loaded and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)  # Mainkan musik menu dalam loop
    elif current_state == "game" and music_loaded:
        pygame.mixer.music.stop()  # Stop musik saat masuk game
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle input nama secara global
        if event.type == pygame.KEYDOWN and input_mode:
            if event.key == pygame.K_RETURN:
                if input_for == 1:
                    player1_name = current_input if current_input else "X"
                    input_for = 2
                    current_input = ""
                else:
                    player2_name = current_input if current_input else "O"
                    input_mode = False
                    current_input = ""
            elif event.key == pygame.K_BACKSPACE:
                current_input = current_input[:-1]
            else:
                current_input += event.unicode
        if current_state == "menu":
            # Handle events untuk menu (tombol diklik di draw_button)
            pass
        elif current_state == "game":
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not input_mode:
                mouseX = event.pos[0] // SQUARE_SIZE
                mouseY = (event.pos[1] - BOARD_OFFSET) // SQUARE_SIZE
                if 0 <= mouseX < BOARD_COLS and 0 <= mouseY < BOARD_ROWS and board[mouseY][mouseX] == 0:
                    if click_sound:
                        click_sound.play()
                    board[mouseY][mouseX] = player
                    if check_win(player):
                        game_over = True
                        winner = player
                        if player == 1:
                            score["X"] += 1
                        else:
                            score["O"] += 1
                        if not sound_played and win_sound:
                            win_sound.play()
                            sound_played = True
                    elif check_draw():
                        game_over = True
                        winner = 0
                    player = 2 if player == 1 else 1
    
    # Jika dalam mode input, gambar prompt (global)
    if input_mode:
        prompt_text = f"Masukkan nama Player {input_for} (X):" if input_for == 1 else f"Masukkan nama Player {input_for} (O):"
        prompt_surf = FONT.render(prompt_text, True, TEXT_COLOR)
        screen.blit(prompt_surf, (WIDTH // 2 - prompt_surf.get_width() // 2, HEIGHT // 2 - 50))
        input_surf = FONT.render(current_input, True, TEXT_COLOR)
        screen.blit(input_surf, (WIDTH // 2 - input_surf.get_width() // 2, HEIGHT // 2))
    else:
        if current_state == "menu":
            draw_menu()
        elif current_state == "game":
            # Gambar garis dan figures
            draw_lines()
            draw_figures()
            
            # Gambar skor dengan bayangan
            score_shadow = FONT.render(f"{player1_name}: {score['X']}   {player2_name}: {score['O']}", True, (0, 0, 0))
            screen.blit(score_shadow, (WIDTH // 2 - score_shadow.get_width() // 2 + 2, HEIGHT - 80 + 2))
            score_text = FONT.render(f"{player1_name}: {score['X']}   {player2_name}: {score['O']}", True, TEXT_COLOR)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT - 80))
            
            # Gambar tombol di atas papan
            if draw_button("Reset Game", 50, 10, 120, 40, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                reset_board()
            if draw_button("Reset Score", 200, 10, 120, 40, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                reset_score()
            if draw_button("Set Names", 350, 10, 120, 40, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                input_mode = True
                input_for = 1
                current_input = ""
            if draw_button("Back Menu", 500, 10, 100, 40, BUTTON_COLOR, BUTTON_HOVER_COLOR):
                current_state = "menu"
            
            # Gambar status dengan bayangan
            if game_over:
                if check_win(1):
                    status_text = FONT.render(f"{player1_name} Menang!", True, CROSS_COLOR)
                elif check_win(2):
                    status_text = FONT.render(f"{player2_name} Menang!", True, CIRCLE_COLOR)
                else:
                    status_text = FONT.render("Seri!", True, TEXT_COLOR)
                status_shadow = FONT.render(f"{player1_name} Menang!" if check_win(1) else f"{player2_name} Menang!" if check_win(2) else "Seri!", True, (0, 0, 0))
                screen.blit(status_shadow, (WIDTH // 2 - status_shadow.get_width() // 2 + 2, HEIGHT - 120 + 2))
                screen.blit(status_text, (WIDTH // 2 - status_text.get_width() // 2, HEIGHT - 120))

    # Update layar setiap frame (dipindahkan ke sini)
    pygame.display.update()

   