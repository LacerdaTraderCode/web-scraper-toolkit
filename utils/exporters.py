"""
Exportadores de dados para múltiplos formatos usando Polars.
"""
from pathlib import Path
from typing import List, Dict
import polars as pl


def export_to_csv(data: List[Dict], filepath: str) -> None:
    """Exporta lista de dicts para CSV usando Polars (mais rápido que Pandas)."""
    df = pl.DataFrame(data)
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.write_csv(filepath)
    print(f"✅ CSV salvo: {filepath} ({len(df)} linhas)")


def export_to_json(data: List[Dict], filepath: str) -> None:
    """Exporta lista de dicts para JSON."""
    df = pl.DataFrame(data)
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.write_json(filepath)
    print(f"✅ JSON salvo: {filepath} ({len(df)} linhas)")


def export_to_parquet(data: List[Dict], filepath: str) -> None:
    """
    Exporta para Parquet - formato colunar eficiente.
    Ideal para grandes volumes de dados e análises posteriores.
    """
    df = pl.DataFrame(data)
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(filepath, compression="snappy")
    print(f"✅ Parquet salvo: {filepath} ({len(df)} linhas, compressão snappy)")


def export_all(data: List[Dict], base_path: str) -> None:
    """Exporta nos 3 formatos de uma vez."""
    export_to_csv(data, f"{base_path}.csv")
    export_to_json(data, f"{base_path}.json")
    export_to_parquet(data, f"{base_path}.parquet")
