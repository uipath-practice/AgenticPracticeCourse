"""Write metadata JSON files atomically."""

import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from .config import AZURE_API_VERSION, AZURE_DEPLOYMENT, METADATA_SUFFIX


def build_metadata(
    image_task,
    extraction: dict,
    usage: dict,
) -> dict:
    """Build the full metadata dictionary.

    Args:
        image_task: The ImageTask being processed.
        extraction: Dict with keys: ocr_text, description, step_instructions.
        usage: Dict with keys: prompt_tokens, completion_tokens, total_tokens.

    Returns:
        Complete metadata dictionary ready to write.
    """
    return {
        "version": "1.0",
        "image_file": image_task.image_name,
        "image_path": image_task.relative_image_path,
        "lesson": image_task.lesson_slug,
        "exercise": image_task.exercise_slug,
        "extraction": {
            "ocr_text": extraction.get("ocr_text", ""),
            "description": extraction.get("description", ""),
            "step_instructions": extraction.get("step_instructions", ""),
        },
        "model": {
            "name": "gpt-5.4",
            "deployment": AZURE_DEPLOYMENT,
            "api_version": AZURE_API_VERSION,
        },
        "usage": {
            "prompt_tokens": usage.get("prompt_tokens", 0),
            "completion_tokens": usage.get("completion_tokens", 0),
            "total_tokens": usage.get("total_tokens", 0),
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def write_metadata(metadata_path: Path, metadata: dict) -> None:
    """Write metadata to a JSON file atomically.

    Writes to a temporary file first, then renames to avoid partial writes.
    """
    content = json.dumps(metadata, indent=2, ensure_ascii=False) + "\n"

    # Write to temp file in the same directory, then rename
    fd, tmp_path = tempfile.mkstemp(
        dir=metadata_path.parent,
        suffix=".tmp",
        prefix=metadata_path.stem,
    )
    try:
        with open(fd, "w", encoding="utf-8") as f:
            f.write(content)
        Path(tmp_path).replace(metadata_path)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise
