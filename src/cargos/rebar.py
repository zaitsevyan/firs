from cargo import Cargo

cargo = Cargo(id='rebar',
              type_name='string(STR_CARGO_NAME_REBAR)',
              unit_name='string(STR_CARGO_NAME_REBAR)',
              type_abbreviation='string(STR_CID_REBAR)',
              sprite='NEW_CARGO_SPRITE',
              weight='1.0',
              cargo_payment_list_colour='63',
              is_freight='1',
              cargo_classes='bitmask(CC_PIECE_GOODS)',
              cargo_label='RBAR',
              town_growth_effect='TOWNGROWTH_NONE',
              town_growth_multiplier='1.0',
              units_of_cargo='TTD_STR_TONS',
              items_of_cargo='string(STR_CARGO_UNIT_REBAR)',
              penalty_lowerbound='30',
              single_penalty_length='42',
              price_factor=133,
              capacity_multiplier='1',
              icon_indices=(3, 5))
