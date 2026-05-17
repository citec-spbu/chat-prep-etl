from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from testing_system.internal.domain.entities import Experiment, Question
from testing_system.internal.domain.interfaces import IExperimentLoader


class YamlExperimentLoader(IExperimentLoader):
    """Loads an Experiment entity from a YAML config file."""

    def load(self, path: str) -> Experiment:
        config_path = Path(path)
        data = self._read_yaml(config_path)
        prompt = self._load_prompt(data.get("prompt", {}), config_path)
        raw_queries = self._load_queries(data, config_path)

        return Experiment(
            id=data["id"],
            name=data.get("name", data["id"]),
            questions=self._questions(
                raw_queries=raw_queries,
                system_prompt=prompt,
            ),
            ground_truth=self._ground_truth(raw_queries),
            answers=[],
            metrics={},
        )

    def _read_yaml(self, path: Path) -> Dict[str, Any]:
        with path.open("r", encoding="utf-8") as file:
            loaded = yaml.safe_load(file) or {}
        if not isinstance(loaded, dict):
            raise ValueError(f"YAML file must contain a mapping: {path}")
        return loaded

    def _load_prompt(
        self,
        prompt_config: Dict[str, Any],
        config_path: Path,
    ) -> Optional[str]:
        if not prompt_config:
            return None

        text = prompt_config.get("text")
        if text:
            return text

        path = prompt_config.get("path")
        if not path:
            return None

        prompt_path = Path(path)
        if not prompt_path.exists():
            prompt_path = config_path.parent / prompt_path

        return self._render_prompt(self._read_yaml(prompt_path))

    def _render_prompt(self, prompt_data: Dict[str, Any]) -> str:
        parts = []
        for key in ("role", "instruction", "constraints", "output_format"):
            value = prompt_data.get(key)
            if value:
                parts.append(f"{key}: {value}")

        examples = prompt_data.get("examples") or []
        if examples:
            parts.append(f"examples: {examples}")

        return "\n\n".join(parts)

    def _load_queries(
        self,
        data: Dict[str, Any],
        config_path: Path,
    ) -> List[Dict[str, Any]]:
        if "queries" in data:
            return data.get("queries", [])

        task_config = data.get("control_task") or data.get("dataset") or {}
        path = task_config.get("path")
        if not path:
            return []

        task_path = Path(path)
        if not task_path.exists():
            task_path = config_path.parent / task_path

        task_data = self._read_yaml(task_path)
        if "queries" in task_data:
            return task_data.get("queries", [])
        if "questions" in task_data:
            return self._queries_from_topic(
                questions=task_data.get("questions", []),
                topic=task_data.get("topic", {}),
            )

        queries = []
        for topic in task_data.get("topics", []):
            queries.extend(
                self._queries_from_topic(
                    questions=topic.get("questions", []),
                    topic=topic,
                )
            )
        return queries

    def _queries_from_topic(
        self,
        questions: List[Dict[str, Any]],
        topic: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        topic_name = topic.get("name")
        queries = []
        for item in questions:
            query = dict(item)
            query.setdefault("metadata", {})
            if topic_name:
                query["metadata"]["topic"] = topic_name
            queries.append(query)
        return queries

    def _questions(
        self,
        raw_queries: List[Dict[str, Any]],
        system_prompt: Optional[str],
    ) -> List[Question]:
        questions = []
        for raw in raw_queries:
            metadata = dict(raw.get("metadata") or {})
            metadata["system_prompt"] = system_prompt

            questions.append(
                Question(
                    id=str(raw["id"]),
                    text=raw["text"],
                    metadata=metadata,
                )
            )
        return questions

    def _ground_truth(self, raw_queries: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            str(raw["id"]): raw.get("ground_truth")
            for raw in raw_queries
            if "ground_truth" in raw
        }
