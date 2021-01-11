from database import (
    get_surface, df
)
import pandas as pd

def test_get_surface():
    df = pd.DataFrame(
        {"tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    assert get_surface('Wimbledon') == "Grass"
