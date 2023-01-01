from deta import Deta
from settings import PROJECT_KEY, DATABASE_NAME

deta = Deta(PROJECT_KEY)
drive = deta.Drive("simple_drive")

photos = deta.Drive("photos")

image_name = "fish.png"

# with open(image_name, "rb") as f:
#     photos.put(image_name, f)


print(photos.list())

# large_file = drive.get(image_name)
# print(large_file)

# with open("cat.png", "wb+") as f:
#   for chunk in large_file.iter_chunks(4096):
#       f.write(chunk)
#   large_file.close()

