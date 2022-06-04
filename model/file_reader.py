from exceptions.incorrect_file_extension import IncorrectFileExtension
from model.competitor_info import CompetitorInfo


class FileReader:
    '''
    Read the file and return a list of CompetitorInfo objects
    '''
    def __init__(self, file_path: str) -> None:
        # Only accepts .txt files
        if not file_path.lower().endswith('.txt'):
            raise IncorrectFileExtension()
        self.file_path = file_path


    def read_file(self) -> list:
        competitors_info_list = list()
        with open(self.file_path, 'r') as f:
            for line in f:
                competitor_info = CompetitorInfo(line)
                competitors_info_list.append(competitor_info)

        return competitors_info_list
