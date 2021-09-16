# `utils`の中身について

## `data_create/`

### `shapping.py`
市町村名と町域が実在するかのチックを行う際に用いる`:dict`(辞書型 (`map<string, vector<string>>`))を作成する際に呼ばれる

## `extract/`

### `detail/`

#### `building_detail.py`

#### `caution.py`

#### `check.py`

#### `data_check.py`

#### `detail_check.py`

#### `detail_data_check.py`

#### `house_number.py`

#### `munipulate.py`

#### `shaping_building_info.py`

#### `shaping.py`

### `prefecture.py`

都道府県を抽出する。この際、存在しない架空の都道府県を抽出してしまうことはない。
都道府県名とそれ以外とに分割し、これを`tuple`の配列で返す

### `city.py`

市、区、群、町、村の順で文字列を探索し、分割する。
市町村名とそれ以外とに分割し、これを`tuple`の配列で返す

### `town.py`

`city.py`で`それ以外`とされたものから、区、群、町、村の順で文字列を探索し、分割する。
市町村名とそれ以外とに分割し、これを`tuple`の配列で返す

### `district.py`

`town.py`で`それ以外`とされたものから、算用数字が出現するまで探索を行う。
算用数字が見つかるまでの部分を`district`として、算用数字が見つかった部分に関しては`others`とする。
この２つを`tuple`の配列にして返す。

## `shape/`

### `output_data_shaping.py`

出力するcsvファイルとして望ましい形式に変換することが主目的



## `shapping.py`

前処理を目的に呼ばれる

以下に行う処理を列挙する

- `丁目, 番地, 番, の` といった文字を`-`に変換
- 入力された文字列の最後にある`-`を削除
- 全角の空白、半角の空白、タブを削除
- `/` を `-`に変換
- 漢数字を算用数字（半角）に変換
- 全角の算用数字を半角の算用数字に変換
- 全角のハイフンを半角のハイフンに変換