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
            with open('C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/reliability/'
                      'rabit_population_system/data/records.json', 'r') as f:

                content = f.read().split(",")
                for i in range(len(content)):
                    content[i] = content[i].split(":")[1]  # split the data so that we get only the wanted numbers
                    content[i] = content[i].split("\\n")[0]

            if failure_probability < 1.0:  # Cap the failure probability at 100%
                failure_probability += 0.05  # Increase failure probability
                # print('failure_probability after: ', failure_probability)
    except Exception as e:
        failure_probability = 0  # Reset failure probability upon failure
        raise e
    return content
