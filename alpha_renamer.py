from pathlib import Path

folder = Path(".")

for file in folder.glob("alpha*.txt"):
    name = file.stem
    number = name[5:]  # remove "alpha"

    if number.isdigit():
        new_name = f"alpha{int(number):03d}.txt"
        new_file = folder / new_name

        if file != new_file:
            file.rename(new_file)
            print(f"{file.name} -> {new_file.name}")