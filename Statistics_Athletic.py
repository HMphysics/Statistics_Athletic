def stat(results):
    if not results:
        return ""
    
    times = []
    for r in results.split(", "):
        h, m, s = map(int, r.split("|"))
        total_seconds = h * 3600 + m * 60 + s
        times.append(total_seconds)
    
    range_seconds = max(times) - min(times)
    avg_seconds = sum(times) // len(times)
    median_seconds = 0
    
    times_sorted = sorted(times)
    n = len(times_sorted)
    if n % 2 == 0:
        median_seconds = (times_sorted[n // 2 - 1] + times_sorted[n // 2]) // 2
    else:
        median_seconds = times_sorted[n // 2]
    
    range_str = f"{range_seconds // 3600:02d}|{(range_seconds // 60) % 60:02d}|{range_seconds % 60:02d}"
    avg_str = f"{avg_seconds // 3600:02d}|{(avg_seconds // 60) % 60:02d}|{avg_seconds % 60:02d}"
    median_str = f"{median_seconds // 3600:02d}|{(median_seconds // 60) % 60:02d}|{median_seconds % 60:02d}"
    
    return f"Range: {range_str} Average: {avg_str} Median: {median_str}"
