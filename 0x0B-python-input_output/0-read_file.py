
#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """reads texte from filename

    Args:
        filename (file): the name of the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
    f.close()
