class Buku(object):
  judul = None
  genre = None
  author = None
  penerbit = None

  def setBukuJudul(self, judul):
    self.judul = judul
    return self

  def setBukuGenre(self, genre):
    self.genre = genre
    return self

  def setBukuAuthor(self, author):
    self.author = author
    return self

  def setBukuPenerbit(self, penerbit):
    self.penerbit = penerbit
    return self

  def getBuku(self):
    msg = "Buku telah diterbitkan\n"
    msg += f"Judul: {self.judul}\n"
    msg += f"Genre: {self.genre}\n"
    msg += f"Author: {self.author}\n"
    msg += f"Penerbit: {self.penerbit}\n"

    return msg

  def copyBuku(self):
    return Buku() \
    .setBukuJudul(self.judul) \
    .setBukuGenre(self.genre) \
    .setBukuAuthor(self.author) \
    .setBukuPenerbit(self.penerbit) \

buku1 = Buku()
buku1.setBukuJudul("Bumi")
buku1.setBukuGenre("Fiksi")
buku1.setBukuAuthor("Tere Liye")
buku1.setBukuPenerbit("Gramedia Pustaka Utama")
print(buku1.getBuku())

buku2 = buku1.copyBuku()
buku2.setBukuJudul("Matahari")
print(buku2.getBuku())