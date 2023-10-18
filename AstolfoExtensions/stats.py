import psutil

def get_system_stats():
  return psutil.cpu_percent(), psutil.virtual_memory().percent

