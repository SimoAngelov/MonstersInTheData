# MonstersInTheData
Studying the patterns behind the sightings, not the monsters themselves.

Course project for Data Science 2026, SoftUni.

## Getting the data
Raw data are tracked with [DVC](https://dvc.org) and imported directly from their original public sources, so no account or token is needed:

```
pip install dvc
dvc update -R data/raw
```

| Dataset | Source |
|---------|--------|
| BFRO Bigfoot reports | [TidyTuesday 2022-09-13](https://github.com/rfordatascience/tidytuesday/tree/main/data/2022/2022-09-13) (T. Renner) |
| Loch Ness Monster reports | [Paxton, Shine & Popov (2025)](https://github.com/Tullimonstrum/NessiestatsforJSDSE), GPL-3 |