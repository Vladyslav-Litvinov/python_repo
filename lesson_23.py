from datetime import datetime

def analyze_heartbeat(log_file, key, output_file):
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()

        filtered_lines = [line for line in lines if key in line]

        if not filtered_lines:
            print(f"No lines found with key: {key}")
            return

        results = []

        for i in range(len(filtered_lines) - 1):
            current_line = filtered_lines[i]
            next_line = filtered_lines[i + 1]

            current_time_str = current_line[current_line.find("Timestamp ") + 10:current_line.find("Timestamp ") + 18]
            next_time_str = next_line[next_line.find("Timestamp ") + 10:next_line.find("Timestamp ") + 18]

            current_time = datetime.strptime(current_time_str, "%H:%M:%S")
            next_time = datetime.strptime(next_time_str, "%H:%M:%S")

            heartbeat_diff = (current_time - next_time).total_seconds()
            if heartbeat_diff < 0:
                heartbeat_diff += 24 * 3600

            if 31 < heartbeat_diff < 33:
                results.append(f"WARNING: Heartbeat delay {heartbeat_diff} seconds at {current_time_str}")
            elif heartbeat_diff >= 33:
                results.append(f"ERROR: Heartbeat delay {heartbeat_diff} seconds at {current_time_str}")

        with open(output_file, 'w') as outfile:
            outfile.write('\n'.join(results))

        print(f"Analysis complete. Results written to {output_file}")

    except Exception as e:
        print(f"Error occurred: {e}")

log_file = "hblog.txt"
key = "Key TSTFEED0300|7E3E|0400"
output_file = "hb_test.log"

analyze_heartbeat(log_file, key, output_file)
