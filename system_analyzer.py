import platform
import psutil
import os
import csv
from datetime import datetime


# ============================================================
#                    SYSTEM ANALYZER
# ============================================================


def get_system_info():
    """Get basic information about the computer."""

    return {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Physical CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPU Cores": psutil.cpu_count(logical=True),
        "Computer Name": platform.node()
    }


def get_cpu_info():
    """Analyze CPU usage and frequency."""

    usage = psutil.cpu_percent(interval=1)
    frequency = psutil.cpu_freq()

    if frequency:
        current_frequency = round(frequency.current, 2)
    else:
        current_frequency = "N/A"

    if usage >= 80:
        status = "HIGH"
    elif usage >= 50:
        status = "MODERATE"
    else:
        status = "NORMAL"

    return {
        "usage": usage,
        "frequency": current_frequency,
        "status": status
    }


def get_memory_info():
    """Analyze RAM usage."""

    memory = psutil.virtual_memory()

    total = memory.total / (1024 ** 3)
    used = memory.used / (1024 ** 3)
    available = memory.available / (1024 ** 3)

    if memory.percent >= 80:
        status = "HIGH"
    elif memory.percent >= 50:
        status = "MODERATE"
    else:
        status = "NORMAL"

    return {
        "total": round(total, 2),
        "used": round(used, 2),
        "available": round(available, 2),
        "usage": memory.percent,
        "status": status
    }


def get_disk_info():
    """Analyze disk usage."""

    disk = psutil.disk_usage(os.getcwd())

    total = disk.total / (1024 ** 3)
    used = disk.used / (1024 ** 3)
    free = disk.free / (1024 ** 3)

    if disk.percent >= 90:
        status = "CRITICAL"
    elif disk.percent >= 75:
        status = "HIGH"
    else:
        status = "NORMAL"

    return {
        "total": round(total, 2),
        "used": round(used, 2),
        "free": round(free, 2),
        "usage": disk.percent,
        "status": status
    }


def get_battery_info():
    """Analyze battery status."""

    battery = psutil.sensors_battery()

    if battery is None:
        return {
            "available": False,
            "percentage": "N/A",
            "power": "N/A",
            "status": "NOT DETECTED"
        }

    percentage = battery.percent

    if battery.power_plugged:
        power = "PLUGGED IN"
    else:
        power = "ON BATTERY"

    if percentage <= 20:
        status = "LOW"
    elif percentage <= 50:
        status = "MODERATE"
    else:
        status = "GOOD"

    return {
        "available": True,
        "percentage": percentage,
        "power": power,
        "status": status
    }


def get_top_processes(limit=10):
    """Get processes using the most CPU."""

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"] or "Unknown",
                "cpu": info["cpu_percent"] or 0,
                "memory": info["memory_percent"] or 0
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    processes.sort(
        key=lambda process: process["cpu"],
        reverse=True
    )

    return processes[:limit]


def calculate_health_score(cpu, memory, disk, battery):
    """Calculate overall system health score."""

    score = 100

    # CPU
    if cpu["usage"] >= 90:
        score -= 30
    elif cpu["usage"] >= 75:
        score -= 20
    elif cpu["usage"] >= 50:
        score -= 10

    # RAM
    if memory["usage"] >= 90:
        score -= 30
    elif memory["usage"] >= 80:
        score -= 20
    elif memory["usage"] >= 60:
        score -= 10

    # Disk
    if disk["usage"] >= 95:
        score -= 25
    elif disk["usage"] >= 90:
        score -= 20
    elif disk["usage"] >= 75:
        score -= 10

    # Battery
    if battery["available"]:
        if battery["percentage"] <= 10:
            score -= 10
        elif battery["percentage"] <= 20:
            score -= 5

    score = max(0, score)

    if score >= 80:
        status = "EXCELLENT"
    elif score >= 60:
        status = "GOOD"
    elif score >= 40:
        status = "WARNING"
    else:
        status = "CRITICAL"

    return score, status


def display_system_info(system):
    """Display system information."""

    print("\n" + "=" * 65)
    print("                    SYSTEM INFORMATION")
    print("=" * 65)

    for key, value in system.items():
        print(f"{key:<28}: {value}")


def display_performance(cpu, memory, disk, battery):
    """Display CPU, RAM, disk and battery information."""

    print("\n" + "=" * 65)
    print("                       PERFORMANCE")
    print("=" * 65)

    print("\nCPU")
    print("-" * 40)
    print(f"Usage              : {cpu['usage']}%")
    print(f"Frequency          : {cpu['frequency']} MHz")
    print(f"Status             : {cpu['status']}")

    print("\nRAM")
    print("-" * 40)
    print(f"Total              : {memory['total']} GB")
    print(f"Used               : {memory['used']} GB")
    print(f"Available          : {memory['available']} GB")
    print(f"Usage              : {memory['usage']}%")
    print(f"Status             : {memory['status']}")

    print("\nDISK")
    print("-" * 40)
    print(f"Total              : {disk['total']} GB")
    print(f"Used               : {disk['used']} GB")
    print(f"Free               : {disk['free']} GB")
    print(f"Usage              : {disk['usage']}%")
    print(f"Status             : {disk['status']}")

    print("\nBATTERY")
    print("-" * 40)

    if battery["available"]:
        print(f"Percentage         : {battery['percentage']}%")
        print(f"Power              : {battery['power']}")
        print(f"Status             : {battery['status']}")
    else:
        print("Battery            : Not detected")


def display_processes(processes):
    """Display top CPU-consuming processes."""

    print("\n" + "=" * 65)
    print("                       TOP PROCESSES")
    print("=" * 65)

    print(
        f"{'PID':<10}"
        f"{'PROCESS':<30}"
        f"{'CPU %':<12}"
        f"{'MEMORY %':<12}"
    )

    print("-" * 65)

    for process in processes:

        name = process["name"]

        if len(name) > 27:
            name = name[:27] + "..."

        print(
            f"{process['pid']:<10}"
            f"{name:<30}"
            f"{process['cpu']:<12.2f}"
            f"{process['memory']:<12.2f}"
        )


def display_health(score, status):
    """Display system health."""

    print("\n" + "=" * 65)
    print("                       SYSTEM HEALTH")
    print("=" * 65)

    print(f"\nHealth Score       : {score}/100")
    print(f"System Status      : {status}")

    if status == "EXCELLENT":
        print("Message            : Your system is running very well.")

    elif status == "GOOD":
        print("Message            : Your system is performing normally.")

    elif status == "WARNING":
        print("Message            : Some resources are under pressure.")

    else:
        print("Message            : Your system requires attention.")


def generate_report(
    system,
    cpu,
    memory,
    disk,
    battery,
    processes,
    score,
    status
):
    """Generate a text report."""

    filename = "system_report.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 65 + "\n")
        file.write("                 SYSTEM ANALYZER REPORT\n")
        file.write("=" * 65 + "\n")

        file.write(
            f"Generated: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        file.write("SYSTEM INFORMATION\n")
        file.write("-" * 40 + "\n")

        for key, value in system.items():
            file.write(f"{key}: {value}\n")

        file.write("\nCPU INFORMATION\n")
        file.write("-" * 40 + "\n")
        file.write(f"Usage: {cpu['usage']}%\n")
        file.write(f"Frequency: {cpu['frequency']} MHz\n")
        file.write(f"Status: {cpu['status']}\n")

        file.write("\nRAM INFORMATION\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total: {memory['total']} GB\n")
        file.write(f"Used: {memory['used']} GB\n")
        file.write(f"Available: {memory['available']} GB\n")
        file.write(f"Usage: {memory['usage']}%\n")
        file.write(f"Status: {memory['status']}\n")

        file.write("\nDISK INFORMATION\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total: {disk['total']} GB\n")
        file.write(f"Used: {disk['used']} GB\n")
        file.write(f"Free: {disk['free']} GB\n")
        file.write(f"Usage: {disk['usage']}%\n")
        file.write(f"Status: {disk['status']}\n")

        file.write("\nBATTERY INFORMATION\n")
        file.write("-" * 40 + "\n")

        if battery["available"]:
            file.write(f"Percentage: {battery['percentage']}%\n")
            file.write(f"Power: {battery['power']}\n")
            file.write(f"Status: {battery['status']}\n")
        else:
            file.write("Battery: Not detected\n")

        file.write("\nTOP PROCESSES\n")
        file.write("-" * 40 + "\n")

        for process in processes:
            file.write(
                f"PID: {process['pid']} | "
                f"Name: {process['name']} | "
                f"CPU: {process['cpu']:.2f}% | "
                f"Memory: {process['memory']:.2f}%\n"
            )

        file.write("\nSYSTEM HEALTH\n")
        file.write("-" * 40 + "\n")
        file.write(f"Health Score: {score}/100\n")
        file.write(f"Status: {status}\n")

    print(f"\nReport saved as: {filename}")


def generate_csv_report(cpu, memory, disk, battery, score, status):
    """Generate a CSV report."""

    filename = "system_report.csv"

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(["SYSTEM ANALYZER REPORT"])
        writer.writerow([])
        writer.writerow(["Metric", "Value"])

        writer.writerow([
            "CPU Usage",
            f"{cpu['usage']}%"
        ])

        writer.writerow([
            "RAM Usage",
            f"{memory['usage']}%"
        ])

        writer.writerow([
            "Disk Usage",
            f"{disk['usage']}%"
        ])

        writer.writerow([
            "Battery",
            (
                f"{battery['percentage']}%"
                if battery["available"]
                else "N/A"
            )
        ])

        writer.writerow([
            "Health Score",
            f"{score}/100"
        ])

        writer.writerow([
            "Health Status",
            status
        ])

    print(f"CSV report saved as: {filename}")


def main():
    """Main program."""

    print("\n")
    print("=" * 65)
    print("                 PYTHON SYSTEM ANALYZER")
    print("=" * 65)

    print("\nAnalyzing system... Please wait.")

    # Collect information
    system = get_system_info()
    cpu = get_cpu_info()
    memory = get_memory_info()
    disk = get_disk_info()
    battery = get_battery_info()
    processes = get_top_processes()

    # Calculate health
    score, status = calculate_health_score(
        cpu,
        memory,
        disk,
        battery
    )

    # Display results
    display_system_info(system)

    display_performance(
        cpu,
        memory,
        disk,
        battery
    )

    display_processes(processes)

    display_health(
        score,
        status
    )

    # Generate reports
    generate_report(
        system,
        cpu,
        memory,
        disk,
        battery,
        processes,
        score,
        status
    )

    generate_csv_report(
        cpu,
        memory,
        disk,
        battery,
        score,
        status
    )

    print("\n" + "=" * 65)
    print("                  ANALYSIS COMPLETED")
    print("=" * 65)
    print("\nThank you for using System Analyzer!")


# ============================================================
#                    PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()

# run this first in your terminal
# pip install psutil 
# After that run code 

