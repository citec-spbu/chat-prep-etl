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
        temperature = self._temperature(data.get("assistant", {}))

        return Experiment(
            id=data["id"],
            name=data["name"],
            config=self._experiment_config(data),
            questions=self._questions(
                raw_queries=data.get("queries", []),
                system_prompt=prompt,
                temperature=temperature,
            ),
            answers=[],
            metrics=[],
        )

    def _read_yaml(self, path: Path) -> Dict[str, Any]:
        with path.open("r", encoding="utf-8") as file:
            loaded = yaml.safe_load(file) or {}
        if not isinstance(loaded, dict):
            raise ValueError(f"YAML file must contain a mapping: {path}")
        return loaded

    def _experiment_config(self, data: Dict[str, Any]) -> Dict[str, Any]:
        config = dict(data)
        config.pop("queries", None)
        return config

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

    def _questions(
        self,
        raw_queries: List[Dict[str, Any]],
        system_prompt: Optional[str],
        temperature: Optional[float],
    ) -> List[Question]:
        questions = []
        for raw in raw_queries:
            metadata = dict(raw.get("metadata") or {})
            metadata["system_prompt"] = system_prompt
            metadata["temperature"] = temperature

            questions.append(
                Question(
                    id=str(raw["id"]),
                    text=raw["text"],
                    retrieved_context_id=[
                        str(item) for item in raw.get("expected_context_ids", [])
                    ],
                    metadata=metadata,
                )
            )
        return questions

    def _temperature(self, assistant_config: Dict[str, Any]) -> Optional[float]:
        params = assistant_config.get("params") or {}
        if "temperature" in params:
            return params["temperature"]

        generation = params.get("generation") or {}
        return generation.get("temperature")
