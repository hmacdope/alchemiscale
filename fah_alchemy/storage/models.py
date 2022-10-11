from pydantic import BaseModel, Field
from gufe.tokenization import GufeKey, GufeTokenizable


class ScopedKey(BaseModel):
    """Unique identifier for GufeTokenizables in state store."""

    gufe_key: GufeKey
    org: str
    campaign: str
    project: str

    def __repr__(self):   # pragma: no cover
        return f"<ScopedKey('{str(self)}')>"

    def __str__(self):
        return "-".join([self.gufe_key, self.org, self.campaign, self.project])


class ComputeKey(BaseModel):
    """Unique identifier for FahAlchemyComputeService instances."""

    identifier: str

    def __repr__(self):   # pragma: no cover
        return f"<ComputeKey('{str(self)}')>"

    def __str__(self):
        return "-".join([self.identifier])


class Task(GufeTokenizable):
    ...

    def _to_dict(self):
        ...

    def _from_dict(self):
        ...

    @property
    def _defaults(self):
        ...


class TaskQueue(GufeTokenizable):
    ...

    def _to_dict(self):
        ...

    def _from_dict(self):
        ...

    @property
    def _defaults(self):
        ...


class TaskArchive(GufeTokenizable):
    ...

    def _to_dict(self):
        ...

    def _from_dict(self):
        ...

    @property
    def _defaults(self):
        ...


