nama ='Rifai'
program ='Gerak Lurus'

print(f'program {program} oleh {nama}')
def hitung_kecepatan(jarak,waktu):
    kecepatan = jarak/waktu
    print('jarak= {jarak / 1000} km ditempuh dalam waktu ={waktu / 60} menit')
    print(f'sehingga kecepatan ={kecepatan} m/s')
    return kecepatan
# jarak = 1000
# waktu = 5*60
kecepatan =hitung_kecepatan(1000, 5*60)
kecepatan =hitung_kecepatan(5000, 15*60)