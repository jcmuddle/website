import os
import shutil

LOCATION="./dist"
CONTENT="./content"

def main():
    if os.path.isdir(LOCATION):
        shutil.rmtree(LOCATION)
    os.makedirs(LOCATION)
    for root, dirs, filenames in os.walk(CONTENT):
        for f in filenames:
           print(f)
    


if __name__ == "__main__":
    main()
