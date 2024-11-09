import pyautogui
import time

def move_mouse():
    try:
        while True:
            # Move o mouse em um pequeno círculo
            pyautogui.moveRel(300, 0, duration=0.1)
            pyautogui.moveRel(0, 300, duration=0.1)
            pyautogui.moveRel(-300, 0, duration=0.1)
            pyautogui.moveRel(0, -300, duration=0.1)
            
            # Espera 5 minutos antes de mover o mouse novamente
            time.sleep(5)  # 300 segundos = 5 minutos

    # Interrompe execução do programa com o comando CTRL + C
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário")

if __name__ == "__main__":
    move_mouse()
