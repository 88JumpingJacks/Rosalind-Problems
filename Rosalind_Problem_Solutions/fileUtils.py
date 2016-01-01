class FileUtils():

    DATA_FILES_DIR = "../Data_Files/"

    @staticmethod
    def readFile(file_path):
        file = open(file_path, "r")
        contents = ""

        with file as f:
            for line in f:
                contents += line

        return contents.strip()
