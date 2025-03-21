import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    rows = len(players)
    columns = len(players.columns)
    return [rows, columns]