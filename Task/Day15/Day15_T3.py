import yaml

from yaml.loader import SafeLoader

with open('services.yaml') as s:
    data = yaml.load(s, Loader=SafeLoader)
    print(data)