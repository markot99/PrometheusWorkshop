import prometheus_client
import time

# suppresses the exporter's system metrics
prometheus_client.REGISTRY.unregister(prometheus_client.GC_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)

if __name__ == '__main__':
    # starts the metrics server
    prometheus_client.start_http_server(8000)
    
    # empty loop to prevent the server from stopping
    while True:
        time.sleep(1)
        pass
