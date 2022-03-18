## About 

株式会社センキョ 住所名簿自動整形プログラム Repository

## Tech

- Formater: [autopep8](https://github.com/hhatto/autopep8)
- Code Check Tool: [flake8](https://pypi.org/project/flake8/)

- Language: Python 3.9.7 64-bit

- 開発環境: Mac OS Big Sur 11

- Editor: Visual Studio Code 
  - スペース: 4 (.py), 2 (.md)
  - 改行: LF
  - 文字コード: UTF-8

## Reference

使用したライブラリや機能についてのリンク

- Python 3.9 regular expression [link](https://docs.python.org/ja/3.9/library/re.html)

- Pandas [link](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)

## GitHub

[GitHub conflict](https://docs.github.com/ja/github/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github)

[circleci](https://circleci.com/integrations/github/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--japac-en-dsa-maxConv-auth-brand&utm_term=g_b-_c__dsa_&utm_content=&gclid=CjwKCAjwh5qLBhALEiwAioods02imTziHAq63Gv_RABFHrXFECtFvah_aCs3W8LA51SCDUTMN7w6NRoCXScQAvD_BwE)

## 仮想環境の整備

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
4. testコードをロジック周りをちゃんと書く