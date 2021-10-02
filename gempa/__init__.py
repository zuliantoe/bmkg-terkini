def ekstraksi_data():
    """
    Tanggal: 01 Oktober 2021,
    Waktu: 21:02:53 WIB
    Magnitudo: 4.1
    Kedalaman: 47 km
    Lokasi: LS=9.29 BT=116.91
    Pusat Gempa: Pusat gempa berada di laut 59 km Tenggara Sumbawa Barat
    Dirasakan: Dirasakan (Skala MMI): III Lombok Timur, II Lombok Tengah
        :return:
    """

    hasil = dict()
    hasil['tanggal'] = '01 Oktober 2021'
    hasil['waktu'] = '21:02:53 WIB'
    hasil['magnitudo'] = 4.1
    hasil['lokasi'] = {'ls': 9.29, 'bt': 116.91}
    hasil['pusat'] =  'Pusat Gempa: Pusat gempa berada di laut 59 km Tenggara Sumbawa Barat'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Lombok Timur, II Lombok Tengah'

    return hasil


def tampilkan_data(result):
    print('Gempa terbaru')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Lokasi : LS {result['lokasi']['ls']} - BT {result['lokasi']['bt']}")
    print(f"Pusat : {result['pusat']}")
    print(f"Dirasakan : {result['dirasakan']}")
