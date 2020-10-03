import os
import menu
import platform

while True:
  if platform.system() == 'Darwin' or platform.system() == 'Linux':
    os.system('clear')
  else:
    os.system('cls')
  print("== Alay Generator ==")
  print("1. Original")
  print("2. Vokal")
  print("3. Autis")
  print("4. Selesai")
  pilih = input("Pilih (1/2/3): ")

  if pilih == '1':
    menu.original()
  elif pilih == '2':
    menu.vokal()
  elif pilih == '3':
    menu.autis()
  elif pilih == '0':
    menu.ubahkata()
  elif pilih == '4':
    print("selesai.")
    break