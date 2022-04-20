# Common libraries
import matplotlib.pyplot as plt
from datetime import datetime
import requests
import json 
import pandas as pd
import datetime

def setup():
    # API setup
    from messari.messari import Messari                   # Messari
    #m = Messari('cb0d3a33-c4c5-4b50-9fff-5dce65d44b97')   # Messari
    m = Messari('f8783744-faf2-475e-8675-b3769cd55c81')   # Messari
    from pycoingecko import CoinGeckoAPI                  # Coingecko
    cg = CoinGeckoAPI()                                   # Coingecko
    API_KEY = '27mKdxqslM3aORzuco6LoqzKjFc'               # Glassnode
    return (cg, m)