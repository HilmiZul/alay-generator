class Generator:
  def __init__(self):
    self.teks = ""

  def original(self):
    text_awal = self.teks
    text_akhir = ""
    for i in range(len(text_awal)):
      if i % 2 == 0:
        text_akhir = text_akhir + text_awal[i].lower()
      else:
        text_akhir = text_akhir + text_awal[i].upper()
    return text_akhir

  def vokal(self):
    teks_origin = self.teks
    huruf_vokal = ['a', 'i', 'u', 'e', 'o']
    for e in teks_origin:
      if e in huruf_vokal:
        teks_origin = teks_origin.replace(e, 'i')
    return teks_origin

  def autis(self):
    teks_origin = self.teks
    teks_change = ""
    change = ['4', '3', '6', '!', '7', '0', '12', '5']
    for i in range(len(teks_origin)):
      if teks_origin[i] == 'a':
        teks_change = teks_change + change[0]
      elif teks_origin[i] == 'e':
        teks_change = teks_change + change[1]
      elif teks_origin[i] == 'g':
        teks_change = teks_change + change[2]
      elif teks_origin[i] == 'i':
        teks_change = teks_change + change[3]
      elif teks_origin[i] == 'j':
        teks_change = teks_change + change[4]
      elif teks_origin[i] == 'o':
        teks_change = teks_change + change[5]
      elif teks_origin[i] == 'r':
        teks_change = teks_change + change[6]
      elif teks_origin[i] == 's':
        teks_change = teks_change + change[7]
      else:
        teks_change = teks_change + teks_origin[i]
    return teks_change
