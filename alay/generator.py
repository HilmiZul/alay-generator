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
    huruf_vokal = ['a', 'i', 'u', 'e', 'o']
    for e in self.teks:
      if e in huruf_vokal:
        self.teks = self.teks.replace(e, 'i')
    return self.teks
