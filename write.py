"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json

from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    # TODO: Write the results to a CSV file, following the specification in the instructions.]
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fieldnames)
        if len(results) == 0:
            pass
        else:
             for approach in results:
                row = [approach.time, approach.distance, approach.velocity,
                       approach.neo.designation, approach.neo.name,
                       approach.neo.diameter, approach.neo.hazardous]
                csv_writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    with open(filename, 'w') as json_file:
        if len(results) == 0:
            return []
        else:
            output = []
            for approach in results:
                approach_dict = dict()
                approach_dict['datetime_utc'] = datetime_to_str(approach.time)
                approach_dict['distance_au'] = float(approach.distance)
                approach_dict['velocity_km_s'] = float(approach.velocity)
                approach_dict['neo'] = dict()
                approach_dict['neo']['designation'] = approach.neo.designation
                if approach.neo.name is None:
                    approach_dict['neo']['name'] = ''
                else:
                    approach_dict['neo']['name'] = approach.neo.name
                if approach.neo.diameter is None:
                    approach_dict['neo']['diameter_km'] = float('nan')
                else:
                    approach_dict['neo']['diameter_km'] = float(approach.neo.diameter)
                if approach.neo.hazardous:
                    approach_dict['neo']['potentially_hazardous'] = True
                else:
                    approach_dict['neo']['potentially_hazardous'] = False

                output.append(approach_dict)

            json.dump(output, json_file)
