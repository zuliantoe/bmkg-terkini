"""
aplikasi deteksi gempa terkini
"""
import gempa

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempa.ekstraksi_data()
    gempa.tampilkan_data(result)
