import argparse

if __name__ == "__main__":
    print("Module invoked directly")
    parser = argparse.ArgumentParser(description=__doc__)
    # parser.add_argument()
    args = parser.parse_args()

# running module by creating a file called __main__.py in it

