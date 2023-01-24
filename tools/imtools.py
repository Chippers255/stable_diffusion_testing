import glob
import os

import fire
from PIL import Image

SIZE = (64, 64)


def create_output_folder(raw_folder: str) -> str:
    """
    Creates a duplicate of the raw image folder with the suffix `_fixed` at the end. Only creates new folder
    if it doesn't already exist

    Args:
        raw_folder: The name and path to the raw image folder. Can be exact or relative.

    Returns:
        The name and path of the new fixed image folder, regardless of if it was created or not.

    Raises:
        None
    """
    output_folder = raw_folder.rstrip("/")
    output_folder = output_folder + "_fixed"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder


def resize(raw_folder: str) -> None:
    output_folder = create_output_folder(raw_folder)

    files = glob.glob(raw_folder)
    print(raw_folder)
    for file in os.listdir(raw_folder):
        if ".png" not in file and ".jpg" not in file and ".jpeg" not in file:
            continue  # skip if not the correct file type

        print(f"found file {file}, resizing to {SIZE[0]}x{SIZE[1]}...")
        basename = os.path.splitext(os.path.basename(file))[0]

        with Image.open(f"{raw_folder}/{file}") as img:
            img = img.resize(SIZE)
            img.save(
                f"{output_folder}/{basename}.png",
                format="PNG",
                resample=Image.Resampling.NEAREST,
            )
    print(f"resizing complete")


if __name__ == "__main__":
    fire.Fire(resize)
