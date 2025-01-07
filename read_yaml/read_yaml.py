import yaml

with open('read_yaml/config.yaml', 'r') as infile:
    config_str = infile.read()

config = yaml.load(config_str, Loader=yaml.FullLoader)
print(config)
print(config['Strategy'])