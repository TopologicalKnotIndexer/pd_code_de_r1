# pd-code-de-r1

Remove Reidemeister-I crossings from PD codes.

## Installation

```bash
pip install pd-code-de-r1
```

## Quick start

`from pd_code_de_r1 import de_r1`.

PD codes are lists of four-entry crossings. Each arc label must occur exactly twice. Functions validate their inputs and do not mutate caller-owned PD-code lists unless explicitly documented.

## Development

Use Python 3.10 or newer for Python packages. Build distributions with `poetry build`. Run the package's tests or examples before publishing. C++ projects require a modern standards-compliant compiler.

## License

MIT. See `LICENSE`.
