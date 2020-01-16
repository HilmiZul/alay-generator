import os
from alay.generator import Generator

alay = Generator()

def original():
  while True:
    os.system('clear')
    print("Alay Generator: Original")
    print("----------------------------")
    alay.teks = input('Input teks: ')
    print("Output teks:",alay.original())
    tanya = input("Lagi? (y/t): ")
    if tanya == 'y':
      continue
    elif tanya == 't':
      break

def vokal():
  while True:
    os.system('clear')
    print("Alay Generator: Vokal")
    print("----------------------------")
    alay.teks = input('Input teks: ')
    print("Output teks:",alay.vokal())
    tanya = input("Lagi? (y/t): ")
    if tanya == 'y':
      continue
    elif tanya == 't':
      break