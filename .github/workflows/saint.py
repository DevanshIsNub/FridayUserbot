# ./.github/workflows/rename.yaml
name: Rename Directory

on:
  push:

jobs:
  rename:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: git mv userbot fridaybot
      - uses: EndBug/add-and-commit@v5.1.0
