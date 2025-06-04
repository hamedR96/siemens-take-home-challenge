from datasets import load_dataset
import os
import math


ds = load_dataset("hamedrahimi/Defect_Spectrum_cleaned")

columns_to_check = ["object_description", "defect_description"]

def is_valid(example):
    for col in columns_to_check:
        val = example[col]
        if val is None or (isinstance(val, float) and math.isnan(val)):
            return False
    return True

filtered_ds = ds.filter(is_valid)

# Output directory
output_dir = "./data"
os.makedirs(output_dir, exist_ok=True)


# Iterate and save
for idx, item in enumerate(filtered_ds["train"]):
    # Save image
    image = item["image"]
    image_rgb = image.convert("RGB")
    image_rgb.save(os.path.join(output_dir, f"{idx:03d}.jpg"), format="JPEG")
    # Save text
    with open(os.path.join(output_dir, f"{idx:03d}.txt"), "w", encoding="utf-8") as f:
        f.write(item["object_description"]+" "+item["defect_description"])

    if idx % 100 == 0:
        print(f"Saved {idx} items...")

print("Done!")
