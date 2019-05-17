"""Document containing JsonFile class description."""
import json


class JsonFile:
    """ A class is intended to interact with a JSON file.
        Class contains methods for translating the csv file into json,
        reading and writing to json file, data structure of JSON file.
    """
    def __init__(self, _json_file_path, _csv_file_path):
        """Initializing the class variables containing the paths
         to the required files and generating a JSON file.

        :param _json_file_path: Variable that contains
         the path to the JSON file.
        :param _csv_file_path:  Variable that contains
         the path to the CSV file.
        """
        self.json_file_path = _json_file_path
        self.csv_file_path = _csv_file_path
        try:
            file = open(self.json_file_path, 'r')
            file.close()
        except IOError:
            self.generate_json(self.json_file_path, self.csv_file_path)

    def json_structure(self, line):
        """The function receives a string of data about the book
           and creates a dictionary that has the JSON structure
           used in this program for storing information.

        :param line: String line that contain row of csv file with
                information about book.
        :return: Dictionary with information about book.
        """
        book = {
            'Title': line[0],
            'Author': line[1],
            'Country': line[2],
            'Language': line[3],
            'Genre': line[4],
            'Pages': int(line[5]),
            'Take_status': bool(line[6]),
        }

        return book

    def extract_from_csv(self, file_path):
        """A function that converts a received csv file
         into a list of dictionaries that contain information about books.

        :param file_path: Variable that contains the path to the CSV file.
        :return: List of dictionaries that contain information
                 about books in corresponding JSON structure.
        """
        books = []
        with open(file_path) as csv_file:
            file_data = csv_file.readlines()

        for line in file_data:
            line = line[:-1].split(';')
            books.append(self.json_structure(line))

        return books

    def generate_json(self, json_file_path, csv_file_path):
        """The function generates a JSON file
        by extracting data from a CSV file
        and writing it in a JSON format to a JSON file.

        :param json_file_path: Variable that contains the path
         to the JSON file.
        :param csv_file_path: Variable that contains the path
         to the CSV file.
        :return: Nothing.
        """
        formatted_json = json.dumps(self.extract_from_csv(csv_file_path),
                                    indent=2, separators=(',', ': '))

        with open(json_file_path, "w") as json_file:
            json_file.write(formatted_json)

    def update_json(self, json_file_path, books):
        """The function receiving an updated array
         of dictionaries with books and rewriting the JSON file.

        :param json_file_path: Variable that contains the path
         to the JSON file.
        :param books: List of dictionaries that contain information
                      about books in corresponding JSON structure
        :return: Nothing.
        """
        with open(json_file_path, "w") as json_file:
            json_file.write(json.dumps(books,
                                       indent=2, separators=(',', ': ')))

    def read_from_json(self, json_file_path):
        """The function that returns the data read from the
         received JSON file.

        :param json_file_path: Variable that contains the path
        to the JSON file.
        :return: Data that was read from the file.
        """
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        return data
