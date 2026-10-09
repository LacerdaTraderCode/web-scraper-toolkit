import logging
from pathlib import Path

import polars as pl

logger = logging.getLogger(__name__)


def _to_frame(data: list[dict], filepath: str) -> pl.DataFrame:
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    return pl.DataFrame(data)


def export_to_csv(data: list[dict], filepath: str) -> None:
    frame = _to_frame(data, filepath)
    frame.write_csv(filepath)
    logger.info("CSV saved: %s (%d rows)", filepath, len(frame))


def export_to_json(data: list[dict], filepath: str) -> None:
    frame = _to_frame(data, filepath)
    frame.write_json(filepath)
    logger.info("JSON saved: %s (%d rows)", filepath, len(frame))


def export_to_parquet(data: list[dict], filepath: str) -> None:
    frame = _to_frame(data, filepath)
    frame.write_parquet(filepath, compression="snappy")
    logger.info("Parquet saved: %s (%d rows)", filepath, len(frame))


def export_all(data: list[dict], base_path: str) -> None:
    export_to_csv(data, f"{base_path}.csv")
    export_to_json(data, f"{base_path}.json")
    export_to_parquet(data, f"{base_path}.parquet")
