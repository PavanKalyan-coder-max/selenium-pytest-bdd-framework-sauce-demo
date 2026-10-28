import uuid


def generate_vehicle_name():
    return f"V_{uuid.uuid4().hex[:8]}"