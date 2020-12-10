# Python DI Example
Python DI + Module 단위 실행 Example

## 디렉토리 구성 규칙

* 모듈 추가시 module 하위에 폴더 생성 후 추가 

```
├─ README.md
├─ docker
├─ rsc
├─ di
│ ├─ module
│ │ ├─ __init__.py
│ │ ├─ *folder*
│ │ │ ├─ __init__.py
│ │ │ └─ ...
│ │ ├─ *folder*
│ │ │ ├─ __init__.py
│ │ │ └─ ...
│ │ ├─ util
│ │ │ ├─ __init__.py
│ │ │ └─ ...
│ │ └─ ...
│ └─ ....
├─ tests
│ ├─ refinery
│ │ ├─ *folder*
│ │ │ └─ ...
│ │ ├─ *folder*
│ │ │ └─ ...
│ │ ├─ util
│ │ └─ ...
│ │ └─ ...
│ └─ test_main.py

```