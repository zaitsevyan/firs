from economy import Economy

economy = Economy(
    id="MILD_MILD_WEST",
    numeric_id=6,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",
        "acetic_acid",
        "mail",
        "alcohol",
        "ammonia",
        "apples",
        "bitumen",
        "cement",
        "chemical_intermediates",
        "coal",
        "coke",
        "food",
        "engineering_supplies",
        "food_additives",
        "farm_supplies",
        "fish",
        "glass",
        "grain",
        "iron_ore",
        "kaolin",
        "limestone",
        "livestock",
        "logs",
        "lumber",
        "milk",
        "molasses",
        "naphtha",
        "nuclear_fuel",
        "nuclear_waste",
        "oil",
        "packaging",
        "paper",
        "paper_chemicals",
        "petrol",
        "phosphate",
        "phosphoric_acid",
        "plastics",
        "potash",
        "pulp_wood",
        "quicklime",
        "salt",
        "scrap_metal",
        "slag",
        "steel_sections",
        "steel_sheet",
        "steel_wire_rod",
        "sulphuric_acid",
        "tin",
        "tinplate",
        "vegetables",
        "vehicles",
        "yeast",
        "zinc",
        "zinc_ore",
    ],
    cargoflow_graph_tuning={
        "group_edges_subgraphs": [],
        "ranking_subgraphs": [
            # ("same", ["port", "goods"]),
            # ("sink", ["T_town_industries", "N_force_rank"]),
        ],
        "clusters": [
            # {"nodes": [], "rank": "", "color": ""},
        ],
    },
)

economy.add_region(
    "cabbage",
    min_x_percent = 66,
    max_x_percent = 100,
    min_y_percent = 0,
    max_y_percent = 100,
)

economy.add_region(
    "potato",
    min_x_percent = 0,
    max_x_percent = 33,
    min_y_percent = 0,
    max_y_percent = 100,
)
