

def estimate_cement(pothole_data):
    DENSITY_CONCRETE = 2400  # kg/m³
    total_volume = 0.0

    for pothole in pothole_data["potholes"]:
        volume = pothole['area_m2'] * pothole['depth_m']
        total_volume += volume

    return total_volume * DENSITY_CONCRETE
