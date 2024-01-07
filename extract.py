"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    neos = []
    with open(neo_csv_path, 'r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            pdes = row['pdes']
            name = row['name']
            diameter = row['diameter']
            pha = row['pha']

            neos.append(NearEarthObject(pdes, name, diameter, pha))

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    approaches = []
    with open(cad_json_path, 'r', encoding='utf8') as json_file:
        json_reader = json.load(json_file)
        for row in json_reader['data']:
            des = row[0]
            cd = row[3]
            dist = row[4]
            v_rel = row[7]

            approaches.append(CloseApproach(des, cd, dist, v_rel))

    return approaches
