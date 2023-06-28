all: gen
	@python bacon.py "count of distinct cpt"
	@echo "Usage: ./bacon.py 'your question'"
gen:
	@./gen-sqlite-from-mrf.sh
clean:
	@rm sample.db
