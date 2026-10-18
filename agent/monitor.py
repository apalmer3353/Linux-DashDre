import psutil
import json
import time

#  server info for my dash
def get_stats():
    net = psutil.net_io_counters()

    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "network_sent": net.bytes_sent,
        "network_received": net.bytes_recv
    }

#  every few seconds
while True:
    stats = get_stats()
      # send the stats through the pipe 
    with open("/run/dashboard/metrics.pipe", "w") as pipe:
        pipe.write(json.dumps(stats) + "\n")

    time.sleep(4)
