import os
import menu

while True:
  os.system('clear')
  print("== Alay Generator ==")
  print("1. Original")
  print("2. Vokal")
  print("3. Selesai")
  pilih = input("Pilih (1/2/3): ")

  if pilih == '1':
    menu.original()
  elif pilih == '2':
    menu.vokal()
  elif pilih == '3':
    print("selesai.")
    break