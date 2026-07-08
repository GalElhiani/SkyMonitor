import pycountry
import geonamescache

gc = geonamescache.GeonamesCache()

def get_locations():
    """
    Compiles all global cities with a population over 15,000,
    mapping their country codes to full country names.
    """
    cities_dict = gc.get_cities()
    local_locations = []
    
    for city_id, info in cities_dict.items():
        code = info['countrycode']
        try:
            full_country = pycountry.countries.get(alpha_2=code).name
        except AttributeError:
            full_country = code
            
        local_locations.append(f"{info['name']}, {full_country}")
        
    local_locations.sort()
    return local_locations