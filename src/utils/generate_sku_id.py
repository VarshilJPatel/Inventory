from datetime import datetime, timezone

def generate_sku_id() -> str:
    now = datetime.now(timezone.utc)

    return f"PRD-{now.strftime('%Y%m%d%H%M%S%f')}"