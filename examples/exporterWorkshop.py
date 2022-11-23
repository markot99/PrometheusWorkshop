import prometheus_client
import time
import random

# suppresses the exporter's system metrics
prometheus_client.REGISTRY.unregister(prometheus_client.GC_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)

time_passed = prometheus_client.Counter("time_passed", "time elapsed since program start")
current_seconds = prometheus_client.Gauge("current_seconds", "current seconds")
random_numbers = prometheus_client.Histogram("random_numbers", "random numbers")
random_numbers2 = prometheus_client.Summary("random_numbers2", "random numbers", ["node", "service"])

if __name__ == '__main__':

    start_time = time.time()

    # starts the metrics server
    prometheus_client.start_http_server(8000)
    
    # empty loop to prevent the server from stopping
    while True:
        current_time = time.time()
        time_passed.inc(current_time - start_time)
        start_time = current_time

        current_seconds.set(time.localtime().tm_sec)

        x = random.random()
        random_numbers.observe(x)

        random_numbers2.labels("node 1", "service 1").observe(x)
        random_numbers2.labels("node 1", "service 2").observe(x)
        random_numbers2.labels("node 2", "service 1").observe(x)

        time.sleep(1)
        pass
