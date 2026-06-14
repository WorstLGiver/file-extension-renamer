import os

folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
print("Put the full file extension with the dot or leave empty.")
target_ext = input("What file extension do you want to replace? ")
replace_ext = input("What do you want to replace it with? ")

if target_ext == "":
    if "." not in replace_ext:
        print("Aborted as no file extension was set to be added onto the extensionless files.")
        os._exit(1)
    for files in os.listdir(folder):
        if "." not in files:
            os.rename(folder + files, folder + files + replace_ext)
else:
    for files in os.listdir(folder):
        if files.endswith(target_ext):
            os.rename(folder + files, folder + files[:-(len(target_ext))] + replace_ext)
