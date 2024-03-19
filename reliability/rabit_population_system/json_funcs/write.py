import random
import json
import reliability.rabit_population_system.data

failure_probability = 0  # Initial failure probability


def write_to_json(msg):
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
            with open('../rabit_population_system/data/records.json', 'r+') as f:
                f.seek(0)
                content = f.read()
                content = json.loads(content)
                content.append(msg)
                f.seek(0)
                json.dump(content, f)
                f.truncate()
            if failure_probability < 1.0:  # Cap the failure probability at 100%
                failure_probability += 0.05  # Increase failure probability
                # print('failure_probability after: ', failure_probability)
    except Exception as e:
        failure_probability = 0  # Reset failure probability upon failure
        raise e


