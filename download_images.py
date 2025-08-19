
import os
import re
import urllib.request
from urllib.parse import urlparse

# --- Configuration ---
MARKDOWN_FILE_PATH = 'content/blog/my-experience-crafting-an-interpreter-with-rust.md'
# Note: This script is intended to be run from the root of the blog project.
# If you run it from another directory, you will need to adjust the paths.
IMAGE_OUTPUT_DIR = 'static/images/my-experience-crafting-an-interpreter-with-rust'
# --- End Configuration ---

def find_image_urls(markdown_content):
    """
    Finds all markdown image URLs in the given string.
    Example: ![alt text](http://example.com/image.png)
    """
    # Regex to find markdown image syntax and capture the URL
    return re.findall(r'https://ceronman.com/wp-content/uploads/2021/07/[a-z0-9-]*\.png', markdown_content)

def clean_url(url):
    """
    Removes query parameters from a URL.
    Example: http://foo.com/bar.jpg?w=937 -> http://foo.com/bar.jpg
    """
    parsed_url = urlparse(url)
    return parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path

def download_image(url, destination_folder):
    """
    Downloads an image from a URL and saves it to a destination folder.
    """
    if not url.startswith(('http://', 'https://')):
        print(f"Skipping non-http URL: {url}")
        return

    try:
        clean_image_url = clean_url(url)
        image_name = os.path.basename(urlparse(clean_image_url).path)

        if not image_name:
            print(f"Could not determine a valid filename for URL: {clean_image_url}")
            return

        output_path = os.path.join(destination_folder, image_name)

        print(f"Downloading {clean_image_url} -> {output_path}")

        # Create a request with a user-agent to avoid potential 403 Forbidden errors
        req = urllib.request.Request(
            clean_image_url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )

        with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        print("...Success")

    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")


def main():
    """
    Main function to run the image download process.
    """
    print("Starting image download script...")

    # 1. Ensure the output directory exists
    if not os.path.exists(IMAGE_OUTPUT_DIR):
        print(f"Creating directory: {IMAGE_OUTPUT_DIR}")
        os.makedirs(IMAGE_OUTPUT_DIR)

    # 2. Read the markdown file
    try:
        with open(MARKDOWN_FILE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: Markdown file not found at '{MARKDOWN_FILE_PATH}'")
        print("Please ensure you are running this script from the root of your project.")
        return

    # 3. Find all image URLs
    urls = find_image_urls(content)
    if not urls:
        print("No image URLs found in the markdown file.")
        return

    print(f"Found {len(urls)} image(s) to process.")

    # 4. Download each image
    for url in urls:
        download_image(url, IMAGE_OUTPUT_DIR)

    print("\nDownload process finished.")

if __name__ == "__main__":
    main()
