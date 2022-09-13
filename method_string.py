belajar = 'langkah pertama adalah awal yang baik'
print(len(belajar))
# menghitung karakter string
print(belajar.upper())
print(belajar.lower())
print(belajar.find('h'))
print(belajar.find('z'))
# -1 artinya karakter itu tidak ada
print(belajar.find('pertama'))
# kata 'pertama' ada di urutan ke-8
print(belajar.replace('baik' , 'bagus'))
print(belajar.replace('Baik' , 'bagus'))
# karena kata 'Baik' bukan value, maka outputnya sama seperti aslinya.
print(belajar.replace('l' , 'r'))
# mengganti karakter dengan karakter lain
print('baik' in belajar)
# ini adalah bentuk true atau false dengan 'in'
print('laik' in belajar)
