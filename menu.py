import os
import platform
from alay.generator import Generator

alay = Generator()

def original():
  while True:
    if platform.system() == 'Darwin' or platform.system() == 'Linux':
      os.system('clear')
    else:
      os.system('cls')
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
    if platform.system() == 'Darwin' or platform.system() == 'Linux':
      os.system('clear')
    else:
      os.system('cls')
    print("Alay Generator: Vokal")
    print("----------------------------")
    alay.teks = input('Input teks: ')
    print("Output teks:",alay.vokal())
    tanya = input("Lagi? (y/t): ")
    if tanya == 'y':
      continue
    elif tanya == 't':
      break

def autis():
  while True:
    if platform.system() == 'Darwin' or platform.system() == 'Linux':
      os.system('clear')
    else:
      os.system('cls')
    print("Alay Generator: Autis")
    print("----------------------------")
    alay.teks = input('Input teks: ')
    print("Output teks:",alay.autis())
    tanya = input("Lagi? (y/t): ")
    if tanya == 'y':
      continue
    elif tanya == 't':
      break