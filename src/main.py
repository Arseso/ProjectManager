import csv
import os
from typing import Tuple, List

from models import Response

RESP_CSV_FILENAME = "./data/responses.csv"
TEXTS_DIRECTORY = "./data/texts"


def get_texts() -> tuple[list[str], list[list[str]]]:
    """
    :return: Tuple of filenames and texts lists
    """
    filenames = []
    texts = []
    for filename in os.listdir(TEXTS_DIRECTORY):
        with open(os.path.join(TEXTS_DIRECTORY, filename), "r") as file:
            text = file.readlines()
            filenames.append(filename)
            texts.append(text)
    return filenames, texts


def write_to_csv(filename: str, resp: Response) -> None:
    """
    :param filename: name of file
    :param resp: response from program
    """
    with open(RESP_CSV_FILENAME, mode="w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow([filename] + resp.values("CA") + resp.values("ORG") + resp.values("VOC") + resp.values("GR"))


def main():
    files, texts = get_texts()
    for filename, text in zip(files, texts):
        response = Response()
        raise NotImplementedError # Getting results from application
        write_to_csv(filename, response)


if __name__ == '__main__':
    main()
