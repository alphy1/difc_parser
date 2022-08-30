venv: requirements.txt
	python3 -m venv env
	. env/bin/activate
	pip install -r requirements.txt

clean:
	rm -rf env
	find -iname "*.pyc" -delete

test: db
	pytest tests --verbosity=2 --showlocals --log-level=DEBUG

db:
	docker-compose -f docker-compose.yml up -d --remove-orphans

run: db
	scrapy crawl difc -a companies=1000

all:
	@echo "make venv		- Create virtual environment for the project"
	@echo "make test		- Test application with pytest"
	@echo "make run			- Run scrapy application"
	@echo "make db			- Run mongodb in docker container"
	@echo "make clean		- Clean venv files"
	@exit 0
