[![version](https://img.shields.io/badge/version-1.2-blue)](https://pypi.org/project/alay/)

# Alay Generator
* Original: mengubah teks menjadi huruf besar dan kecil
* Vokal: mengubah huruf vokal menjadi huruf ```i```
* Autis: mencampurkan dengan angka/karakter simbol

# Install
* Install python 3.7.x
* Clone/download [repo ini](https://github.com/HilmiZul/alay-generator)
```
git clone https://github.com/HilmiZul/alay-generator
```
* Jalankan
```
python main.py
```

# Install as package via pip
```
pip install alay
```
```python
from alay.generator import Generator

alay = Generator()

# input teks
alay.teks = "aku suka sama kamu"

alay.original()
# aKu sUkA SaMa kAmU

alay.vokal()
# iki siki simi kimi

alay.autis()
# 4ku 5uk4 54m4 k4mu
```