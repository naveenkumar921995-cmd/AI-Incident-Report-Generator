import pandas as pd

def monitoring_metrics(data):

    metrics = {}

    metrics["total_incidents"] = len(data)

    metrics["near_miss"] = len(data[data["root_cause"]=="Near Miss"])

    metrics["high_risk"] = len(data[data["root_cause"]=="Equipment failure"])

    return metrics
