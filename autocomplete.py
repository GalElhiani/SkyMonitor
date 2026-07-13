import pycountry
import geonamescache

gc = geonamescache.GeonamesCache()

def _initialize_locations():
    """compiles global cities once at startup."""
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

# runs once on server startup
ALL_LOCATIONS = _initialize_locations()

def get_locations():
    """a function that returns the full static list used for validation"""
    return ALL_LOCATIONS

def search_locations(query, limit=10):
    """a function that filters the static list instantly in memory"""
    if not query:
        return []
    
    query = query.lower()
    matches = []
    for loc in ALL_LOCATIONS:
        if query in loc.lower():
            matches.append(loc)
            if len(matches) >= limit:  # Break early to keep it blazing fast
                break
    return matches
