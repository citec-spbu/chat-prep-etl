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

    def push(self, experiment: Experiment) -> None:
        self._experiments[experiment.id] = experiment
        self._save_one(experiment)
        logger.info("Experiment %s saved to local registry", experiment.id)

    def check(self, experiment: Experiment) -> Optional[Experiment]:
        return self._experiments.get(experiment.id, None)

    def select(self, latest: Optional[int] = None) -> List[Experiment]:
        exps = sorted(
            self._experiments.values(),
            key=lambda e: e.finished_at or e.started_at or "",
            reverse=True,
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
                self._experiments[exp.id] = exp
                logger.debug("Loaded experiment %s from %s", exp.id, file_path)
            except Exception:
                logger.exception("Failed to load experiment from %s, skipping", file_path)

    def _save_one(self, experiment: Experiment) -> None:
        self._output_dir.mkdir(parents=True, exist_ok=True)
        target = self._output_dir / f"{experiment.id}.json"
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