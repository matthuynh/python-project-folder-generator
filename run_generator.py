import os

# Create new files
def create_file(file_name):    
    try:
        new_file = open(file_name, 'x')
        new_file.close()
    except OSError:
        # Usually occurs if the file already exists
        print("Could not create file: " + file_name)
    else:
        print("Successfully created file for: " + file_name)

# Create new directories
def create_directory(path):
    try:
        os.mkdir(path)
    except OSError:
        # Usually occurs if the directory already exists
        print("Could not create directory for: " + path)
    else:
        print("Successfully created directory for: " + path)

if __name__ == "__main__":
    # Create paths for folders
    test_directory = "tests"
    docs_directory = "documentation"
    project_directory = "sample"

    # Create directories
    create_directory(test_directory)
    create_directory(docs_directory)
    create_directory(project_directory)

    # Create other miscellaneous text files
    create_file("README.md")
    create_file("requirements.txt")

    input("Press enter to close")




