import json
import os
import time

pipe_path = "/run/dashboard/metrics.pipe"
output_path = "/run/dashboard/latest.json"
history_path = "/home/dre997005/linux-dashboard/data/history.jsonl"

# keep reading the stats from my monitoring agent
while True:
    with open(pipe_path, "r") as pipe:
        for line in pipe:
            try:
                stats = json.loads(line)
                stats["timestamp"] = int(time.time())

                # save the newest stats for my live dashboard
                with open(output_path + ".tmp", "w") as file:
                    json.dump(stats, file)

                os.replace(output_path + ".tmp", output_path)

                # also save each reading so i can make charts
                with open(history_path, "a") as file:
                    file.write(json.dumps(stats) + "\n")

            except json.JSONDecodeError:
                print("Could not read the stats", flush=True)
