all: init
	@python bacon.py "count of distinct cpt"
	@echo "Usage: ./bacon.py 'your question'"
init:
	@./gen-sqlite-from-mrf.sh
	@pip install -r < requirements.txt
clean:
	@rm sample.db
