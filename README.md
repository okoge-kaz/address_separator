# 株式会社センキョ smart-senkyo v2.5 extensions address-separator

## 仮想環境の整備

- poetry [推奨]  
  [公式 Document](https://python-poetry.org/docs/)  
  [日本語 Document](https://cocoatomo.github.io/poetry-ja/cli/)

  - はじめて使用する際
    1. poetry install:  
       for osx:  
       `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
    2. type following:  
       `$ poetry --version`
    3. Updating Poetry to the latest stable version is as simple as calling the `self update` command.
       `$ poetry self update`
    4. poetry config:  
       `$ poetry config virtualenvs.in-project true`
    5. Installing dependencies:
       To install the defined dependencies for your project, just run the install command.  
       `$ cd <project>`  
       `$ poetry install`
  - 自分でプロジェクトを作成する際

    - Initialising a pre-existing project

      1. poetry init  
         `$ cd <pre-existing-project>`  
         `$ poetry init`  
         Instead of creating a new project, Poetry can be used to ‘initialise’ a pre-populated directory. To interactively create a `pyproject.toml` file in directory `pre-existing-project`:
      2. add specifying dependencies:  
         instead of modifying the pyproject.toml file by hand, you can use the add command.  
         `$ poetry add <package>`

    - Project setup
      1. First, let’s create our new project, let’s call it poetry-demo:  
         `poetry new poetry-demo`
      2. add specifying dependencies:  
         instead of modifying the pyproject.toml file by hand, you can use the add command.  
         `$ poetry add <package>`

  - 仮想環境を利用する

    1. Installing dependencies:  
       To install the defined dependencies for your project, just run the install command.  
       `$ cd <project>`  
       `$ poetry install`
    2. 仮想環境に入る  
       `$ poetry shell`
    3. Run python-code in virtualenv:  
       `$ python <python-code>`  
       or  
       `$ python3 <python-code>`

       補足:  
        2. 3. を同時に行うには、  
        `poetry run python <python-file>`  
        を行う。

    4. 仮想環境から抜ける  
       `$ deactivate`

- python3 標準 [非推奨]

  1. 仮想環境作成 : `python3 -m venv .venv`
  2. 仮想環境に入る : `source .venv/bin/activate`
  3. 依存環境の整備 : `python3 -m pip install -r requirements.txt`
  4. 仮想環境から抜ける : `deactivate`

  - `requirements.txt`を作成する
    `python3 -m pip freeze > requirements.txt`

  - 仮想環境内にパッケージをインストール
    `python3 -m pip install requests`
    `python3 -m ppip install selenium`

    参考記事 : [URL](https://maku77.github.io/python/env/venv.html)  
    パッケージ関連 : [URL](https://rinoguchi.net/2020/08/python-scraping-library.html)

## To Do

1. `senkyo/senkyo/utils/modify/handleMiscellaneousBug.py` のコードがあまりにも多くの処理をまとめてしまっているので分割処理を行う
2. `senkyo/senkyo/utils/extract/detail/check/*` チェックコードは、それだけで分離するべき
3. `senkyo/senkyo/utils/shape/output_data_shaping.py`があまりにも多くの処理をまとめてしまっているので分割処理を行う
4. test コードをロジック周りをちゃんと書く
5. `re.search`の結果を使って、`.start(), .end()`のように安易に int 型に代入しているが、`None`となる可能性があるので修正する(`senkyo/senkyo/utils/modify/reSplitByEveryFieldAfterSplit.py`など)
6. Excel 対応

## Git-flow

[参考記事](http://keijinsonyaban.blogspot.com/2010/10/a-successful-git-branching-model.html)
