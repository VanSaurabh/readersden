import yaml


def read_config(file):
    try:
        with open(file) as f:
            try:
                return yaml.safe_load(f)
            except ValueError:
                raise ValueError('config.yml is invalid !')
    except IOError:
        raise IOError('got error while opening config.yml file !')