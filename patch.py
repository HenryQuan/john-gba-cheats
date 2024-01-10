# %%
# read all cheats file
import os

# get a list of all cheats files
cheats_path = "others/GBA-CHEATS"
cheats_files = os.listdir(cheats_path)
# patch the encoding issues on modern computers
# by using encode("utf-8").decode("gbk") to support Chinese/Japanese characters
patched_path = "others/GBA-CHEATS-patched"

def read_all_cheats_title():
    titles = []
    for cheats in cheats_files:
        with open(os.path.join(cheats_path, cheats), "r", encoding="latin-1") as cht:
            lines = cht.readlines()
            for line in lines:
                if line.startswith("["):
                    line = line.replace("[", "").replace("]", "").strip()
                    titles.append(line)
    return titles

def patch_all_cheats_title_encodings():
    for cheats in cheats_files:
        with open(os.path.join(cheats_path, cheats), "r", encoding="latin-1") as cht:
            lines = cht.readlines()
            with open(os.path.join(patched_path, cheats), "w", encoding="utf-8") as patched:
                for line in lines:
                    if line.startswith("["):
                        line = line.replace("[", "").replace("]", "").strip()
                        try:
                            line = line.encode("latin-1").decode("gbk")
                        except:
                            try:
                                line = line.encode("latin-1").decode("big5")
                            except:
                                line = line.encode("utf-8").decode("utf-8")
                            
                        patched.write(f"[{line}]\n")
                    else:
                        patched.write(line)

    print("Done!")

# %%
patch_all_cheats_title_encodings()

# %%
