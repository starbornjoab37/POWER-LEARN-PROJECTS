import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Accept multiple URLs separated by spaces
    urls = input("Please enter image URLs (separate by spaces): ").split()

    os.makedirs("Fetched_Images", exist_ok=True)
    downloaded_hashes = set()

    for url in urls:
        try:
            # Fetch the image
            response = requests.get(url, timeout=10, headers={"User-Agent": "UbuntuFetcher/1.0"})
            response.raise_for_status()

            # Check Content-Type before saving
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipping non-image URL: {url}")
                continue

            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = "downloaded_image.jpg"

            filepath = os.path.join("Fetched_Images", filename)

            # Prevent duplicate downloads using file hash
            file_hash = hashlib.md5(response.content).hexdigest()
            if file_hash in downloaded_hashes:
                print(f"⚠ Duplicate image skipped: {filename}")
                continue

            downloaded_hashes.add(file_hash)

            # Save the image in binary mode
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.HTTPError as e:
            print(f"✗ HTTP error: {e}")
        except requests.exceptions.ConnectionError:
            print(f"✗ Connection error for {url}")
        except Exception as e:
            print(f"✗ An unexpected error occurred: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
