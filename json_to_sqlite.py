import os

from pathlib import Path

def sqlitebiter_import_json(src):
    input_file = Path(src)
    db_out = Path("tugs-pdf-gen.sqlite").resolve()
    db_out.parent.mkdir(parents=True, exist_ok=True)
    os.system(f"sqlitebiter -a -o {db_out} file {input_file}")

src = "metadata.json"
sqlitebiter_import_json(src)