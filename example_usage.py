import logging

from mapping_united_states import CensusData
from mapping_united_states import mapping

logging.basicConfig(
    format='%(asctime)s %(message)s',
    encoding='utf-8',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.ERROR
)

census_data = CensusData()


def map_single_state():
    # Map a single state
    mapping.map_area(
        'output/California.png',
        [
            'CA'
        ],
        mapping.MappingOptions(),
        census_data
    )


def map_multiple_states():
    # Map multiple states
    mapping.map_area(
        'output/California_Nevada.png',
        [
            '06',  # FIPS Code for CA
            'NV'
        ],
        mapping.MappingOptions(),
        census_data
    )


def map_multiple_counties():
    # Mapping based on counties
    mapping.map_area(
        'output/Sub-California.png',
        [
            '06027',
            '06071'
        ],
        mapping.MappingOptions(),
        census_data
    )


def map_multiple_counties_with_custom_theme():
    # Adjusting the mapping colors while mapping part of Nevada and Cali
    options = mapping.MappingOptions()
    options.border.line_color = '#FF0000'
    options.border.fill_color = '#00FF00'
    options.primary_roads.line_color = '#0000FF'
    options.primary_roads.line_thickness = 10
    options.secondary_roads.is_visible = False
    options.neighborhood_roads.is_visible = False
    options.water.min_water_area = None

    mapping.map_area(
        'output/Sub-California-Nevada.png',
        [
            '06027',
            '06071',
            '32003',
            '32023',
            '32017',
            '32009'
        ],
        options,
        census_data
    )


if __name__ == "__main__":
    map_single_state()
    map_multiple_states()
    map_multiple_counties()
    map_multiple_counties_with_custom_theme()
