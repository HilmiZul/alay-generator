from .kamus import kamus

class Alay:
  def __init__(self):
    self.teks = ""
    self.huruf_vokal = ['a', 'i', 'u', 'e', 'o']
    self.kamus_karakter = ['4', '3', '6', '!', '7', '0', '12', '5']

  def original(self):
    teks = self.teks
    hasil = ""
    for i in range(len(teks)):
      if i % 2 == 0:
        hasil = hasil + teks[i].lower()
      else:
        hasil = hasil + teks[i].upper()
    return hasil

  def vokal(self):
    teks = self.teks
    for e in teks:
      if e in self.huruf_vokal:
        teks = teks.replace(e, 'i')
    return teks

  def autis(self):
    teks = self.teks
    hasil = ""
    for i in range(len(teks)):
      if teks[i] == 'a':
        hasil = hasil + self.kamus_karakter[0]
      elif teks[i] == 'e':
        hasil = hasil + self.kamus_karakter[1]
      elif teks[i] == 'g':
        hasil = hasil + self.kamus_karakter[2]
      elif teks[i] == 'i':
        hasil = hasil + self.kamus_karakter[3]
      elif teks[i] == 'j':
        hasil = hasil + self.kamus_karakter[4]
      elif teks[i] == 'o':
        hasil = hasil + self.kamus_karakter[5]
      elif teks[i] == 'r':
        hasil = hasil + self.kamus_karakter[6]
      elif teks[i] == 's':
        hasil = hasil + self.kamus_karakter[7]
      else:
        hasil = hasil + teks[i]
    return hasil

  def ubahkata(self):
    teks = self.teks
    k = kamus.keys()
    return list(k)


