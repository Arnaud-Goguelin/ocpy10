from enum import Enum


class Environment(str, Enum):
    local = "local"
    production = "production"
    test = "test"
