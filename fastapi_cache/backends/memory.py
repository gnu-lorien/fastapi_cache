from typing import Union

from .base import BaseCacheBackend

DEFAULT_TIMEOUT = 0


class InMemoryCacheBackend(BaseCacheBackend):
    _cache: dict = {}

    async def add(
        self,
        key: Union[str, int],
        value: Union[str, int],
        timeout: int = DEFAULT_TIMEOUT
    ) -> bool:
        if key in self._cache:
            return False
        self._cache[key] = value

        return True

    async def get(
        self,
        key: Union[str, int],
        default: Union[str, int] = None
    ) -> bool:
        return self._cache.get(key, default)

    async def set(
        self,
        key: Union[str, int],
        value: Union[str, int],
        timeout: int = DEFAULT_TIMEOUT
    ) -> bool:
        self._cache[key] = value

        return True

    async def delete(self, key: Union[str, int]) -> bool:
        if key not in self._cache:
            return False

        del self._cache[key]

        return True