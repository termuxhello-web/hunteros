import time

def monitor_app(app_pid):
    while True:
        # Check process syscall / file / network activity
        # Placeholder logic
        print(f"Monitoring app PID {app_pid}")
        time.sleep(2)

if __name__ == "__main__":
    import sys
    pid = int(sys.argv[1])
    monitor_app(pid)
