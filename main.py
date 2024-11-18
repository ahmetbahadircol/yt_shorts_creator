import asyncio

from upload_shorts import upload_video
from download_reels import download_instagram_reel
from pathlib import Path

# Path to the folder containing files


async def main(code: str):
    await download_instagram_reel(code)

    folder_path = Path(f"reels/{code}")
    video_file = None
    txt_file = None
    image_file = None
    for file in folder_path.iterdir():
        if file.suffix == ".mp4":
            video_file = str(file)
        elif file.suffix == ".txt":
            txt_file = str(file)
        elif file.suffix in [
            ".jpg",
            ".jpeg",
            ".png",
        ]:  # You can add more image extensions here
            image_file = str(file)
    if not all([video_file, txt_file, image_file]):
        raise RuntimeError(f"Data is missing. Check downloaded folder {code}")

    with open(txt_file, "r", encoding="utf-8") as txt:
        content = txt.read()

    content = content.replace("\n", " ").strip()

    if len(content) > 99:
        breakpoint()

    await upload_video(
        video_file,
        content,
        "Rick and Morty #shorts #rickandmorty #funny #viral #rickandmortyclips #clips",
        ["shorts", "rickandmorty", "viral", "youtube", "funny"],
    )


if __name__ == "__main__":
    REELS_CODE = ""
    asyncio.run(main(REELS_CODE))
