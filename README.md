# A print tool that wraps text to a specified width.

Usage:

```python
from wrap_print import WrapPrint

wp = WrapPrint(20)
wp.print('12345678901234567890')
wp.print('This module provides access to', end='')
wp.print(' the Unicode Character Database (UCD)', end='')
wp.print(' which defines character properties', end='')
wp.print(' for all Unicode characters. The data contained', end='')
wp.print(' in this database is compiled from the UCD version 15.1.0.')
wp.print('這個模組提供了對 Unicode 字元資料庫（UCD）的存取，', end='')
wp.print('該資料庫定義了所有 Unicode 字元的字元屬性。', end='')
wp.print('這個資料庫中的資料是從 UCD 15.1.0 版本編譯而來的。')
```

Result:

```
12345678901234567890

This module provides
 access to the Unico
de Character Databas
e (UCD) which define
s character properti
es for all Unicode c
haracters. The data 
contained in this da
tabase is compiled f
rom the UCD version 
15.1.0.
這個模組提供了對 Uni
code 字元資料庫（UCD
）的存取，該資料庫定
義了所有 Unicode 字元
的字元屬性。這個資料
庫中的資料是從 UCD 1
5.1.0 版本編譯而來的
。
```

It counts the CJK wide characters the fullwidth characters as 2 characters.