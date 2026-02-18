import configparser
import os

config = configparser.RawConfigParser()

# Get project root directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create full path to config file
config_path = os.path.join(base_dir, "Configuration", "config_SIT.ini")

config.read(config_path)


class ReadConfigClass:

    @staticmethod
    def get_data_for_email():
        return config.get("login_data", "email")

    @staticmethod
    def get_data_for_password():
        return config.get("login_data", "password")

    @staticmethod
    def get_data_for_login_url():
        return config.get("application_url", "login_url")

    @staticmethod
    def get_data_for_registration_url():
        return config.get("application_url", "registration_url")

    config.read(config_path)
print("CONFIG PATH:", config_path)
print("FILE EXISTS:", os.path.exists(config_path))
print("SECTIONS:", config.sections())

