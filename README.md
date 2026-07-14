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

A Reidemeister-I crossing contains a locally repeated arc pattern. The algorithm builds the opposite-slot strand graph, identifies labels trapped in the one-crossing loop, removes exactly one crossing, reconnects its surviving strand endpoints, and restarts the scan. Restarting is required for links containing a closed one-crossing component because deletion changes the active crossing indices. Labels are renumbered along every remaining component cycle, and removal repeats because one reduction can expose another R1 crossing.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required.

## Development

Python 3.10 or newer is required. Run tests with `pd_code_sanity` available:

```bash
python -m unittest discover -s tests -v
```

No PyPI publication is performed as part of repository maintenance.

## License

MIT. See `LICENSE`.

## Citation

If you use this repository in academic work, please cite it as:

```bibtex
@software{topologicalknotindexer_pd_code_de_r1,
  author = {{TopologicalKnotIndexer contributors}},
  title = {{pd\_code\_de\_r1}},
  year = {2026},
  url = {https://github.com/TopologicalKnotIndexer/pd_code_de_r1}
}
```
