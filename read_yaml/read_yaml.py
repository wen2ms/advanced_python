from pathlib import Path

import yaml

with Path("read_yaml/config.yaml").open("r", encoding="utf-8") as infile:
    config_str = infile.read()

# config = yaml.load(config_str, Loader=yaml.FullLoader)
config = yaml.safe_load(config_str)
print(config)
print(config["Strategy"])
