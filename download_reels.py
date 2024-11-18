import instaloader
import os
from pathlib import Path

# Initialize the Instaloader object
loader = instaloader.Instaloader()


async def download_instagram_reel(shortcode):
    try:
        reels_folder = Path("reels")
        os.makedirs(reels_folder, exist_ok=True)

        # Load the Reel post
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        target_file = reels_folder / f"{shortcode}"

        loader.download_post(post, target=target_file)

        print(f"Downloaded Reel: {shortcode}")
    except Exception as e:
        print(f"An error occurred: {e}")
