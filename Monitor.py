import os
import requests

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
    
    # Memeriksa setiap URL
    for url in urls:
        result = check_website_status(url)
        print(result)
    
    print("=" * 50)
