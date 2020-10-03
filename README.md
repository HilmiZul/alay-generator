[![version](https://img.shields.io/badge/version-1.2.1-blue)](https://pypi.org/project/alay/)

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
from bahasa.alay import Alay

alay = Alay()

# input teks
alay.teks = "aku kangen kamu"

alay.original()
# aKu kAnGeN KaMu

alay.vokal()
# iki kingin kimi

alay.autis()
# 4ku k4n63n k4mu
```
