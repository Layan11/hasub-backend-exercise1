import random
import json

failure_probability = 0  # Initial failure probability


def read_from_json():
    global failure_probability
    try:
        if random.random() < failure_probability:
            # Raise json_funcs random exception
            random_exception = random.choice([
                FileNotFoundError,
                PermissionError,
                IsADirectoryError,
                FileExistsError,
                NotADirectoryError,
                IOError
            ])
            raise random_exception("Random exception raised")
        else:
            with open('./data/journal.records.json') as f:
                print(f.read())

            if failure_probability < 1.0:  # Cap the failure probability at 100%
                failure_probability += 0.05  # Increase failure probability
                print('failure_probability after: ', failure_probability)
    except Exception as e:
        failure_probability = 0  # Reset failure probability upon failure
        raise e
