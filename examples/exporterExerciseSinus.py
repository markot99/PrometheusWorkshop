import prometheus_client
import time
import math

# suppresses the exporter's system metrics
prometheus_client.REGISTRY.unregister(prometheus_client.GC_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)

my_sinus = prometheus_client.Gauge("my_sinus", "my sinus")

if __name__ == '__main__':
    start_time = time.time()

    # starts the metrics server
    prometheus_client.start_http_server(8000)

    # empty loop to prevent the server from stopping
    while True:
        my_sinus.set((math.sin((time.time() - start_time) * math.pi / 10)))
        time.sleep(1)
