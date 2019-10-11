def hitung_kecepatan(massa,percepatan):
    gaya = massa*percepatan
    print('jarak= {jarak / 1000} km ditempuh dalam waktu ={waktu / 60} menit')
    print(f'sehingga kecepatan ={kecepatan} m/s')
    return kecepatan
# jarak = 1000
# waktu = 5*60
kecepatan =hitung_kecepatan(1000, 5*60)
kecepatan =hitung_kecepatan(5000, 15*60)