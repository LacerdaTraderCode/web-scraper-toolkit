"""
Rate limiter simples para evitar sobrecarga de servidores.
"""
import time
from fake_useragent import UserAgent


class RateLimiter:
    """Controla o intervalo mínimo entre requisições."""

    def __init__(self, min_interval: float = 1.0):
        self.min_interval = min_interval
        self._last_request = 0.0

    def wait(self):
        """Aguarda se necessário para respeitar o intervalo."""
        elapsed = time.time() - self._last_request
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last_request = time.time()


def get_random_user_agent() -> str:
    """Retorna um User-Agent aleatório para rotação."""
    try:
        return UserAgent().random
    except Exception:
        # Fallback para UA padrão
        return (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
