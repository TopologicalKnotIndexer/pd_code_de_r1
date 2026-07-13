# pd-code-de-r1

Remove Reidemeister-I crossings from a planar-diagram code.

## Installation

```bash
pip install pd-code-de-r1
```

## Usage example

```python
from pd_code_de_r1 import de_r1

pd = [[1, 1, 2, 2]]
print(de_r1(pd))  # []
```

## Algorithm

A Reidemeister-I crossing contains a locally repeated arc pattern. The algorithm builds the opposite-slot strand graph, identifies labels trapped in the one-crossing loop, removes the crossing, reconnects its surviving strand endpoints, and renumbers labels along each remaining cycle. Removal is repeated because one reduction can expose another R1 crossing.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required.

## Development

Run examples and package checks before release. Python packages require Python 3.10 or newer. Build PyPI artifacts with:

```bash
poetry check
poetry build
```

## License

MIT. See `LICENSE`.
