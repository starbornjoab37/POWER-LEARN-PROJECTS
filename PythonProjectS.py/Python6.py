# Ubuntu-Inspired Image Fetcher Assignment
# The Wisdom of Ubuntu: "I am because we are"
# In the spirit of Ubuntu, which emphasizes community and 
# sharing, your task is to create a program that connects to the global community of the internet, 
# respectfully fetches shared resources, and organizes them for later appreciation.
# Your Task
# Create a Python script that:
# Prompts the user for a URL containing an image
# Creates a directory called "Fetched_Images" if it doesn't exist
# Downloads the image from the provided URL
# Saves it to the Fetched_Images directory with an appropriate filename
# Handles errors gracefully, respecting that not all connections succeed
# Requirements
# Use the requests library to fetch the image
# Check for HTTP errors and handle them appropriately
# Create the directory if it doesn't exist using os.makedirs() with exist_ok=True
# Extract the filename from the URL or generate one if not available
# Save the image in binary mode
# Ubuntu Principles to Implement
# Community: Your program should connect to the wider web community
# Respect: Handle errors gracefully without crashing
# Sharing: Organize the fetched images for later sharing
# Practicality: Create a tool that serves a real need
# Save Your Work in a GitHub Repo Called "Ubuntu_Requests" 
# and Submit the URL for this Repository to Complete the Assignment. 

# Terminal Output Text
# Welcome to the Ubuntu Image Fetcher
# A tool for mindfully collecting images from the web

# Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
# ✓ Successfully fetched: ubuntu-wallpaper.jpg
# ✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

# Connection strengthened. Community enriched.
# Starter Code Structure
# python

# Clean, readable code with clear comments
# Faithfulness to Ubuntu principles of community and respect


# Ubuntu-Inspired Image Fetcher
# The Wisdom of Ubuntu: "I am because we are"
# This program connects to the wider web community,
# respectfully fetches shared images, and organizes them for later appreciation.import requests
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
