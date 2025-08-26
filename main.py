import asyncio

from upload_shorts import upload_video
from download_reels import download_instagram_reel
from pathlib import Path

# Path to the folder containing files


async def main(code: str):
    if not code:
        raise RuntimeError("Reels Code is required")

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

    print(len(content))
    print(content)
    breakpoint()
    await upload_video(
        video_file,
        content,
        "Rick and Morty #shorts #rickandmorty #funny #viral #rickandmortyclips #clips",
        [
            "rickandmorty",
            "rickandmortyshorts",
            "adultswim",
            "ricksanchez",
            "mortysmith",
            "rickandmortyclips",
            "rickandmortyfunny",
            "funnycartoonclips",
            "scificartoons",
            "rickandmortybestsenes",
            "rickandmortyhumor",
            "wubbalubbadubdub",
            "picklerick",
            "portalgun",
            "rickandmortyseason",
            "rickandmortyepisodes",
            "trendingshorts",
            "youtubeshorts",
            "comedyanimation",
            "adultcartoons",
            "cartoonshorts",
            "rickandmortyfans",
            "rickandmortyfan",
            "rickandmortyquotes",
            "adultcartoonclips",
            "cartoonfunny",
            "animationfunny",
            "funnyanimation",
            "animatedcomedy",
            "cartooncomedy",
            "sciencefiction",
            "animatedshorts",
        ],
    )


if __name__ == "__main__":
    REELS_CODE = "C7W46AVxwuL"
    asyncio.run(main(REELS_CODE))
