import yaml

def load_config(file_path: str) -> dict:
    """Load YAML config files."""
    with open(file_path, "r") as f:
        return yaml.safe_load(f)