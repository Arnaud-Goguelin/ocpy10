from enum import Enum


class Environnement(str, Enum):
    local = "local"
    production = "production"
    test = "test"
