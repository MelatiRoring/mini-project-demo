import os
import requests
import csv

def check_website_status(url):
    """
    Memeriksa status HTTP sebuah URL.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return f"[OK] {url} is reachable (Status: {response.status_code})"
        else:
            return f"[WARN] {url} returned status {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"[ERROR] {url} is not reachable. Error: {str(e)}"

if __name__ == "__main__":
    print("Website Monitoring Tool")
    print("=" * 50)
    
    # Atur path ke lokasi file skrip
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "urls.txt")
    
    # Membaca daftar URL dari file
    if not os.path.exists(file_path):
        print(f"Error: File 'urls.txt' tidak ditemukan di {file_path}.")
        print("Harap buat file tersebut dengan daftar URL.")
        exit(1)

    with open(file_path, "r") as file:
        urls = [line.strip() for line in file if line.strip()]
    
    # Siapkan file CSV untuk menyimpan hasil
    output_file = os.path.join(script_dir, "website_status.csv")
    
    # Menulis header ke file CSV
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Status"])  # Menulis header
        
        # Memeriksa setiap URL dan menulis hasilnya ke CSV
        for url in urls:
            result = check_website_status(url)
            status = result.split(" ", 1)[1]  # Menyimpan hanya status, bukan pesan lengkap
            writer.writerow([url, status])
            print(result)
    
    print("=" * 50)
    print(f"Hasil pengecekan telah disimpan ke {output_file}")
