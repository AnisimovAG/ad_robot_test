import statistics
from datetime import datetime, timedelta
from timeit import timeit

from requests import get

DEFAULT_URL = 'http://127.0.0.1:8080'


class DownloadPictureTestService:
    """Тест скорости. Скачиваем файл."""
    DEFAULT_URL = 'https://speedtest.selectel.ru/10MB'
    DEFAULT_ITERATIONS = 10

    def __init__(self,
                 url: str | None = None,
                 chunk: int | None = None,
                 iterations: int | None = None):
        self.url = url or self.DEFAULT_URL
        self.chunk = chunk
        self.iterations = iterations or self.DEFAULT_ITERATIONS

    def _download(self) -> tuple[int, timedelta]:
        start = datetime.now()
        resp = get(self.url, **(self.chunk and  {'stream': True} or {}))
        return (
            self.chunk and sum(len(c) for c in resp.iter_content(chunk_size=self.chunk)) or len(resp.content),
            datetime.now() - start
        )

    @property
    def speed(self) -> int:
        """Скорость байт в секунду"""
        res = []
        for i in range(self.iterations):
            size, t = self._download()
            res.append(size / t.seconds)
        return round(statistics.fmean(res))
