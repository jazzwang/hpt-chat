all: init
	@python bacon.py "count of distinct cpt"
	@echo "Usage: ./bacon.py 'your question'"
init:
	@./gen-sqlite-from-mrf.sh
	@pip install -r requirements.txt
clean: sample.db
	@rm sample.db
test:
	@python bacon.py "count of primary precedures"
	@python bacon.py "price of IRON related precedures"
sample:
	@chainlit run chainlit_sample.py -w
run:
	@chainlit run hpt-chat.py -w
