import json
import logging
import os
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import asdict

from testing_system.internal.domain.entities import Experiment
from testing_system.internal.domain.interfaces import IRegistry


logger = logging.getLogger(__name__)


class LocalRegistry(IRegistry):
    def __init__(self, output_dir: str) -> None:
        self._output_dir = Path(output_dir)
        self._experiments: Dict[str, Experiment] = {}
        self._load()

    def _index(self, experiment: Experiment) -> str:
        assistant_config = experiment.config["assistant"]
        retriever_config = experiment.config["retriever"]
        registry_config = experiment.config["registry"]
        clean_config = experiment.config["clean"]
        assert isinstance(assistant_config, str)
        assert isinstance(retriever_config, str)
        assert isinstance(registry_config, str)
        assert isinstance(clean_config, str)
        return experiment.id+'.'+'.'.join([
            assistant_config.split('.')[-1][:-2],
            retriever_config.split('.')[-1][:-2],
            registry_config.split('.')[-1][:-2],
            clean_config
        ])

    def push(self, experiment: Experiment) -> None:
        self._save_one(experiment)
        index = self._index(experiment=experiment)
        self._experiments[index] = experiment
        logger.info("Experiment %s saved to local registry", index)

    def check(self, experiment: Experiment) -> Optional[Experiment]:
        index = self._index(experiment=experiment)
        return self._experiments.get(index, None)

    def select(self, latest: Optional[int] = None) -> List[Experiment]:
        exps = sorted(
            self._experiments.values(),
            key=lambda e: e.name,
            reverse=False,
        )
        if latest is not None:
            exps = exps[:latest]
        return exps

    def _load(self) -> None:
        if not self._output_dir.exists():
            logger.info("Registry directory %s does not exist, starting empty", self._output_dir)
            return
        for file_path in self._output_dir.glob("*.json"):
            try:
                data = json.loads(file_path.read_text(encoding="utf-8"))
                exp = Experiment(**data)
                index = self._index(experiment=exp)
                self._experiments[index] = exp
                logger.debug("Loaded experiment %s from %s", index, file_path)
            except Exception:
                logger.exception("Failed to load experiment from %s, skipping", file_path)

    def _save_one(self, experiment: Experiment) -> None:
        self._output_dir.mkdir(parents=True, exist_ok=True)
        if "/" in experiment.id or "\\" in experiment.id or ".." in experiment.id:
            raise ValueError(f"Invalid experiment id: {experiment.id}")
        index = self._index(experiment=experiment)
        target = self._output_dir / f"{index}.json"
        tmp = target.with_suffix(".tmp")
        try:
            tmp.write_text(
                json.dumps(asdict(experiment), indent=2, ensure_ascii=False, default=str),
                encoding="utf-8",
            )
            os.replace(tmp, target)
        except Exception:
            if tmp.exists():
                tmp.unlink(missing_ok=True)
            raise