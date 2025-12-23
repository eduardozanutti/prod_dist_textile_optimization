import yaml

def get_config():
    # Carregue config
    with open('src/config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config
