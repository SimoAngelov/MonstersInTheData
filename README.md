# MonstersInTheData
Studying the patterns behind the sightings, not the monsters themselves.

Course project for Data Science 2026, SoftUni.
See the [project proposal](docs/Project_Proposal.ipynb).

## Getting the data
Raw data are tracked with [DVC](https://dvc.org). The DVC cache is stored in a public repository ([MonstersInTheData-storage](https://github.com/SimoAngelov/MonstersInTheData-storage)), so no account or token is needed:

```
pip install dvc
dvc pull
```

If the storage repository is unavailable, the raw data can be downloaded directly from their original sources:

```
dvc update -R data/raw
```

The MD5 hashes in the `.dvc` files identify the exact versions used. If `git status` shows a changed `.dvc` file after `dvc update`, the source has changed since this analysis.

| Dataset | Source |
|---------|--------|
| BFRO Bigfoot reports | [TidyTuesday 2022-09-13](https://github.com/rfordatascience/tidytuesday/tree/main/data/2022/2022-09-13) (T. Renner) |
| Loch Ness Monster reports | [Paxton, Shine & Popov (2025)](https://github.com/Tullimonstrum/NessiestatsforJSDSE), GPL-3 |