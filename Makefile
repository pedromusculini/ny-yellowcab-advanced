.PHONY: clean curate enrich validate test visualize all

clean:
	@echo "Cleaning data..."

curate:
	python scripts/clean_curate.py

enrich: curate
	@echo "Feature engineering completed."

validate:
	python scripts/validate_curated.py

visualize:
	python scripts/visualize_data.py

test:
	pytest tests/

all: enrich validate test visualize