import csv
import os
from typing import Tuple, List
import requests
from models import Response
from analysis.ca import get_ca_metrics
from analysis.org import get_org_metrics
from analysis.voc import get_voc_metrics
import pandas as pd

RESP_CSV_FILENAME = "./data/responses.csv"
RESP_NUM_CSV_FILENAME = "./data/responses_as_num.csv"
TEXTS_DIRECTORY = "./data/texts"
XLSX_FILE = "./data/letters.xlsx"

FROM_XLSX = True

def _get_texts() -> tuple[list[str], list[list[str]]]:
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

def _get_from_xlsx()-> tuple[list[str], list[list[str]]]:
    data = pd.read_excel(XLSX_FILE, sheet_name=0)
    return data["Почта"].values, data["Текст эссе"].values
    


def _write_to_csv(filename: str, resp: Response) -> None:
    """
    :param filename: name of file
    :param resp: response from program
    """
    with open(RESP_CSV_FILENAME, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        if os.stat(RESP_CSV_FILENAME).st_size == 0:
            writer.writerow(["filename",
                             "CA1", "CA1.1", "CA1.2", "CA1.3", "CA1.4", "CA1.5", "CA1.6", "CA1.7", "CA2",
                             "ORG1", "ORG2", "ORG2.2", "ORG2.3", "ORG2.4", "ORG2.5", "ORG3",
                             "VOC1", "VOC2", "VOC3",
                             "GR1", "GR2", "GR3"])
        writer.writerow([filename] + resp.values("CA") + resp.values("ORG") + resp.values("VOC") + resp.values("GR"))

    with open(RESP_NUM_CSV_FILENAME, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        if os.stat(RESP_NUM_CSV_FILENAME).st_size == 0:
            writer.writerow(["filename",
                             "CA1", "CA1.1", "CA1.2", "CA1.3", "CA1.4", "CA1.5", "CA1.6", "CA1.7", "CA2",
                             "ORG1", "ORG2", "ORG2.2", "ORG2.3", "ORG2.4", "ORG2.5", "ORG3",
                             "VOC1", "VOC2", "VOC3",
                             "GR1", "GR2", "GR3", "UNIQ_WORDS", "OR_ERR", "CLQ_WORDS", "CLC_ERRORS", 
                             "prop_a1", "prop_a2", "prop_b1", "prop_b2", "prop_c1", "prop_c2",])
        writer.writerow([filename] + resp.values("CA", True) + resp.values("ORG", True) + resp.values("VOC", True) + resp.values("GR", True) + resp.values("metrics"))


def main():
    if not FROM_XLSX:
        files, texts = _get_texts()
    else:
        files, texts = _get_from_xlsx()

    errors = 0
    for filename, text in zip(files, texts):
        # Getting results
        try:
            response = get_ca_metrics(Response(), text)
            response = get_org_metrics(response, text)
            response = get_voc_metrics(response, text)

            _write_to_csv(filename, response)
        except requests.exceptions.JSONDecodeError:
            errors+=1
            continue
        except Exception:
            _write_to_csv(filename, Response())
            
    
    print(f"ERRORS: {errors}")


if __name__ == '__main__':
    main()

