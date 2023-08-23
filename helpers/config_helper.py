import json

class ConfigHelper:
    def __init__(self, config_file_path="config.json"):
        self.config_file_path = config_file_path
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_file_path) as config_file:
            return json.load(config_file)

    def get_explicit_wait(self):
        return self.config_data.get("explicit_wait", 10)

    def get_implicit_wait(self):
        return self.config_data.get("implicit_wait", 10)