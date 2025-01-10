from typing import Dict

import tomlkit
from pydantic import BaseModel


class ExampleBool(BaseModel):
    value: bool


class ExampleDoc(BaseModel):
    name: str
    subdoc: Dict[str, ExampleBool]


def main():
    with open("example.toml") as f:
        doc = tomlkit.load(f)

    print(f"doc: {doc}")
    print(f"type(doc): {type(doc)}")
    print(f"type(doc.subdoc.first.value): {type(doc.get("subdoc").get("first").get("value"))}")
    print(f"type(doc.subdoc.second.value): {type(doc.get("subdoc").get("second").get("value"))}")

    # This succeeds
    ExampleDoc.model_validate(doc)

    # This fails
    ExampleDoc(**doc)

    # This also fails
    ExampleDoc(**dict(doc))

if __name__ == "__main__":
    main()
