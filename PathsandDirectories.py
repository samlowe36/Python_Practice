from pathlib import Path

#absolute path - the main location starting from the top
# example: c:\Pram Files\Microsoft\etc.
#relative path - the path relative to where you are currently

path = Path("ecommerce")
print(path.exists())
path = Path("ecommerce1")
print(path.exists())            #boolean returning whether something of that name exists

path = Path("emails")
print(path.mkdir())         #makes a directory/folder
path = Path("emails")
print(path.rmdir())         #removes a directory/folder


path = Path()
for file in path.glob("*.py"):  #all python files in current location
    print(file)

path = Path()
for file in path.glob("*"):  # all files and directories in current location
    print(file)