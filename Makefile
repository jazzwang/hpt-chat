all: init
	@python bacon.py "count of distinct cpt"
	@echo "Usage: ./bacon.py 'your question'"
init:
	@./gen-sqlite-from-mrf.sh
	@pip install -r requirements.txt
clean:
	@rm sample.db
test:
	@python bacon.py "count of primary precedures"
	@python bacon.py "price of IRON related precedures"

