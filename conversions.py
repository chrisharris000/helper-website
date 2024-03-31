import mgrs

def _convert_mgrs_to_lat_lon(mgrs_coord):
    m = mgrs.MGRS()
    return m.toLatLon(mgrs_coord)

def _convert_lat_lon_to_mgrs(lat_coord, lon_coord):
    m = mgrs.MGRS()
    c = m.toMGRS(lat_coord, lon_coord)
    return c

def convert_mgrs_lat_lon(mgrs_coord, lat_coord, lon_coord):
    if not mgrs_coord:
        mgrs_coord_output = _convert_lat_lon_to_mgrs(float(lat_coord), float(lon_coord))
        lat_coord_output = lat_coord
        lon_coord_output = lon_coord

    else:
        lat_coord_output, lon_coord_output = _convert_mgrs_to_lat_lon(mgrs_coord)
        mgrs_coord_output = mgrs_coord

    coordinate_vars = {
        "mgrs_coord_output": mgrs_coord_output,
        "lat_coord_output": lat_coord_output,
        "lon_coord_output": lon_coord_output
    }
    return coordinate_vars

def _convert_ft_to_m(feet):
    return float(feet) / 3.281

def _convert_m_to_ft(metres):
    return float(metres) * 3.281

def convert_m_ft(metres, feet):
    if not metres:
        metres_output = _convert_ft_to_m(feet)
        feet_output = feet
    else:
        feet_output = _convert_m_to_ft(metres)
        metres_output = metres
    
    distance_vars = {
        "metres_output": metres_output,
        "feet_output": feet_output
    }
    return distance_vars