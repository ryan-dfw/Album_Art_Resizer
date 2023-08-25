from mutagen.id3 import ID3, APIC
import os

def resize_artwork(file_path):
    try:
        audio = ID3(file_path)
        for tag in audio.getall("APIC"):
            if tag.type == 3:
                if tag.width >= 1000 and tag.height >= 1000:
                    tag.width = 999
                    tag.height = 999
                    audio.save()
                    print(f"resized {os.path.basename(file_path)}")
    except Exception as e:
        print(f"it broke")

def process_mp3_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".mp3"):
                file_path = os.path.join(root, file)
                resize_artwork(file_path)

drive_X_path = "X:\\"
process_mp3_files(drive_X_path)