import multiprocessing

workers = multiprocessing.cpu_count() * 2
threads = multiprocessing.cpu_count() * 2
worker_connections = 2048
max_requests = 2048
max_requests_jitter = 100