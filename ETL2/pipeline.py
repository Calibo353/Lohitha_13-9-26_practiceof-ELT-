from extract import extract
from transform import transform
from Validate import validate
from load import load
def run_pipeline():

    raw = extract()

    clean = transform(raw)

    validate(clean)

    load(clean)
if __name__ == "__main__":
    run_pipeline()