# pydantic-tomlkit-bool

Reproduce Pydantic bool validation error from TOML document parsed using `tomlkit.load()`

## Virtual Environment

Set up the virtual environment

```bash
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
.venv/bin/pip freeze
```

Package versions

```python-requiements
annotated-types==0.7.0
pydantic==2.10.5
pydantic_core==2.27.2
tomlkit==0.13.2
typing_extensions==4.12.2
```

## Reproduction

Run the example

```bash
.venv/bin/python3 example.py
```

Output

```console
± .venv/bin/python3 example.py
doc: {'name': 'example-doc', 'subdoc': {'first': {'value': True}, 'second': {'value': False}}}
type(doc): <class 'tomlkit.toml_document.TOMLDocument'>
type(doc.subdoc.first.value): <class 'bool'>
type(doc.subdoc.second.value): <class 'bool'>
Traceback (most recent call last):
  File "/home/bschwedler/repos/bschwedler/pydantic-tomlkit-bool/example.py", line 35, in <module>
    main()
  File "/home/bschwedler/repos/bschwedler/pydantic-tomlkit-bool/example.py", line 29, in main
    ExampleDoc(**doc)
  File "/home/bschwedler/repos/bschwedler/pydantic-tomlkit-bool/.venv/lib64/python3.12/site-packages/pydantic/main.py", line 214, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for ExampleDoc
subdoc.first.value
  Input should be a valid boolean [type=bool_type, input_value=True, input_type=Bool]
    For further information visit https://errors.pydantic.dev/2.10/v/bool_type
```
