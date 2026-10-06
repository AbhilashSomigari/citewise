"""Export the suite as EvalForge YAML (evals/suite.yaml + evals/suite_builtin.yaml).

`suite.yaml` uses Citewise graders (run it with `citewise eval`, which registers them).
`suite_builtin.yaml` uses only EvalForge's built-in graders, so plain EvalForge can drive the
command adapter:  evalforge run --suite evals/suite_builtin.yaml \
    --agent "python -m citewise.evals.agent --prompt-file src/citewise/prompts/writer_v1.md"
"""

from citewise.config import REPO_ROOT
from citewise.evals.suite import build_suite, write_suite_yaml

suite = build_suite(trials=2)
write_suite_yaml(REPO_ROOT / "evals" / "suite.yaml", suite)
write_suite_yaml(REPO_ROOT / "evals" / "suite_builtin.yaml", suite, builtin_only=True)
print(f"exported {len(suite.tasks)} tasks")
