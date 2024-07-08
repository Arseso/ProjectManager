import csv
import os

from models import Response

RESP_CSV_FILENAME = "./data/responses.csv"
TEXTS_DIRECTORY = "./data/texts"


def texts() -> tuple[str, list[str]]:
    """
    :return: text from ./data/texts/ directory. Format: Filename, Text
    """
    for filename in os.listdir(TEXTS_DIRECTORY):
        with open(os.path.join(TEXTS_DIRECTORY, filename), "r") as file:
            text = file.readlines()
            yield filename, text


def write_to_csv(filename: str, resp: Response) -> None:
    """
    :param filename: name of file
    :param resp: response from program
    """
    with open(RESP_CSV_FILENAME, mode="w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow([filename] + resp.values("CA") + resp.values("ORG") + resp.values("VOC") + resp.values("GR"))


def main():
    resp = Response()
    # Writing results to Answer model
    raise NotImplementedError

if __name__ == '__main__':
    main()
