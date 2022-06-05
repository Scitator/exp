# Experiment Template

- `.github/workflow` - codestyle and CI
- `assets` - datasets, logs, etc
- `bin` - bash files to start pipelines
- `docker` - docker files
- `examples` - notebooks and full-featured examples
- `requirements` - python requirements
- `src` - code
- `tests` - tests

## How to reproduce?

```bash
bash bin/...  # download data
pip install -r ./requirements/...  # install dependencies, or use docker
bash bin/...  # run experiments
# use examples/... to analize results
```
