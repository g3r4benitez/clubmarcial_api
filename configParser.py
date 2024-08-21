import configparser

class ConfigParser2:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_database_config(self):
        return {
            'host': self.config.get('database', 'host'),
            'port': self.config.getint('database', 'port'),
            'username': self.config.get('database', 'username'),
            'password': self.config.get('database', 'password')
        }

    def get_server_config(self):
        return {
            'host': self.config.get('server', 'host'),
            'port': self.config.getint('server', 'port')
        }


if __name__ == '__main__':
    configuration = ConfigParser2('configuration.ini')
    db_config = configuration.get_database_config()
    print(f"database configuration: {db_config}")

    server_config = configuration.get_server_config()
    print(f"server configuration: {server_config}")