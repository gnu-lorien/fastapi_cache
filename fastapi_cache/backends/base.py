from typing import TypeVar, Generic, Tuple

DEFAULT_TIMEOUT = 600

KT = TypeVar('KT')
VT = TypeVar('VT')


class BaseCacheBackend(Generic[KT, VT]):
    async def add(
        self,
        key: KT,
        value: VT,
        timeout: int = DEFAULT_TIMEOUT
    ) -> bool:
        raise NotImplementedError

    async def get(
        self,
        key: KT,
        default: VT = None,
        **kwargs
    ) -> VT:
        raise NotImplementedError

    async def set(
        self,
        key: KT,
        value: VT,
        timeout: int = DEFAULT_TIMEOUT
    ) -> bool:
        raise NotImplementedError

    async def exists(self, *keys: Tuple[KT]) -> bool:
        raise NotImplementedError

    async def delete(self, key: KT) -> bool:
        raise NotImplementedError

    async def flush(self) -> None:
        raise NotImplementedError

    async def close(self) -> None:
        raise NotImplementedError
