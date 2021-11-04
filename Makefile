run_prod:
	@gunicorn main:app \
		--bind 0.0.0.0:8888 \
		-w 2 --worker-class uvicorn.workers.UvicornWorker

run_tests:
	@python -m pytest