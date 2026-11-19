// Condo IV Capital Reserve Funding Plan (October 2026, re-based to start 1/1/2027).
// Source: ~/projects/hoa/maintenance_responsibilities/Condo_IV_Reserve_Plan.xlsx and
// Condo_IV_Statement_of_Income_and_Liabilities.md (Becht 2026 study, Falcon 2022 entity allocations).
// maintenance/expenses = Long-Term Maintenance disbursements, inflated 3%/yr to the year spent.
// contributions follow the plan's three-fund rules (3% growth; Emergency and Operating stop once
// target/floor is reached); closing_balances include 1% interest. Unaudited planning estimates.
define([], function() {
    return {
        colors: [
            '#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe',
            '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080',
            '#ffffff', '#000000', '#19a9e6', '#f4e619', '#d86343', '#b491e6', '#f0a146', '#31f0f0', '#e632f0', '#6cf60c',
            '#bebebe', '#800860', '#e6ffbe', '#63429a', '#c8facc', '#000800', '#aac3ff', '#8000ff', '#b1ffd8', '#750000',
            '#606080', '#cfcfcf', '#a919e6', '#194ee6', '#31f46f', '#e619c3', '#46f0b4', '#f0329c', '#bcf06c', '#fabcbe'
        ],
        "yearly": {
            "2027": {
                "maintenance": {
                    "Deck Railings & Balusters (safety)": 23175,
                    "Exterior Caulk/Sealant & Trim Maintenance": 15450,
                    "Window Wells (rebuild program)": 49440
                },
                "expenses": 88065,
                "full_contribution": 171500,
                "contributions": {
                    "Emergency Reserve": 23800,
                    "Long-Term Maintenance": 135100,
                    "Operating Reserve": 12600
                },
                "closing_balances": {
                    "Emergency Reserve": 47131,
                    "Long-Term Maintenance": 139556,
                    "Operating Reserve": 75118
                }
            },
            "2028": {
                "maintenance": {
                    "Entry Stoops — Leveling & Stair Nosing (safety)": 31190,
                    "Window Wells (rebuild program)": 127308
                },
                "expenses": 158498,
                "full_contribution": 176645,
                "contributions": {
                    "Emergency Reserve": 24514,
                    "Long-Term Maintenance": 139153,
                    "Operating Reserve": 12978
                },
                "closing_balances": {
                    "Emergency Reserve": 72116,
                    "Long-Term Maintenance": 121607,
                    "Operating Reserve": 88847
                }
            },
            "2029": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 181944,
                "contributions": {
                    "Emergency Reserve": 25249,
                    "Long-Term Maintenance": 143328,
                    "Operating Reserve": 13367
                },
                "closing_balances": {
                    "Emergency Reserve": 98087,
                    "Long-Term Maintenance": 266150,
                    "Operating Reserve": 103103
                }
            },
            "2030": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 187403,
                "contributions": {
                    "Emergency Reserve": 26007,
                    "Long-Term Maintenance": 147627,
                    "Operating Reserve": 13768
                },
                "closing_balances": {
                    "Emergency Reserve": 125075,
                    "Long-Term Maintenance": 416439,
                    "Operating Reserve": 117902
                }
            },
            "2031": {
                "maintenance": {
                    "Chimney Chase Covers": 145095
                },
                "expenses": 145095,
                "full_contribution": 152056,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 152056,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 126325,
                    "Long-Term Maintenance": 427565,
                    "Operating Reserve": 119081
                }
            },
            "2032": {
                "maintenance": {
                    "Entry Stoops — Concrete Replacement": 234034
                },
                "expenses": 234034,
                "full_contribution": 156618,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 156618,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 127589,
                    "Long-Term Maintenance": 354424,
                    "Operating Reserve": 120272
                }
            },
            "2033": {
                "maintenance": {
                    "Deck Boards (surface)": 161163,
                    "Deck Framing & Footings": 184186,
                    "Deck Railings & Balusters (safety)": 115116,
                    "Exterior Caulk/Sealant & Trim Maintenance": 18448
                },
                "expenses": 478913,
                "full_contribution": 161316,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 161316,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 128865,
                    "Long-Term Maintenance": 40372,
                    "Operating Reserve": 121475
                }
            },
            "2034": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 166156,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 166156,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 130153,
                    "Long-Term Maintenance": 206932,
                    "Operating Reserve": 122690
                }
            },
            "2035": {
                "maintenance": {
                    "Entry Stoops — Leveling & Stair Nosing (safety)": 38360
                },
                "expenses": 38360,
                "full_contribution": 171141,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 171141,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 131455,
                    "Long-Term Maintenance": 341782,
                    "Operating Reserve": 123917
                }
            },
            "2036": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 176275,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 176275,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 132769,
                    "Long-Term Maintenance": 521474,
                    "Operating Reserve": 125156
                }
            },
            "2037": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 181563,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 181563,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 134097,
                    "Long-Term Maintenance": 708252,
                    "Operating Reserve": 126407
                }
            },
            "2038": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 187010,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 187010,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 135438,
                    "Long-Term Maintenance": 902345,
                    "Operating Reserve": 127671
                }
            },
            "2039": {
                "maintenance": {
                    "Exterior Caulk/Sealant & Trim Maintenance": 22028
                },
                "expenses": 22028,
                "full_contribution": 192620,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 192620,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 136792,
                    "Long-Term Maintenance": 1081961,
                    "Operating Reserve": 128948
                }
            },
            "2040": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 198399,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 198399,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 138160,
                    "Long-Term Maintenance": 1291179,
                    "Operating Reserve": 130238
                }
            },
            "2041": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 204351,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 204351,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 139542,
                    "Long-Term Maintenance": 1508442,
                    "Operating Reserve": 131540
                }
            },
            "2042": {
                "maintenance": {
                    "Entry Stoops — Leveling & Stair Nosing (safety)": 47178
                },
                "expenses": 47178,
                "full_contribution": 210481,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 210481,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 140937,
                    "Long-Term Maintenance": 1686830,
                    "Operating Reserve": 132855
                }
            },
            "2043": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 216796,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 216796,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 142347,
                    "Long-Term Maintenance": 1920494,
                    "Operating Reserve": 134184
                }
            },
            "2044": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 223300,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 223300,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 143770,
                    "Long-Term Maintenance": 2162998,
                    "Operating Reserve": 135526
                }
            },
            "2045": {
                "maintenance": {
                    "Deck Railings & Balusters (safety)": 164128,
                    "Exterior Caulk/Sealant & Trim Maintenance": 26303
                },
                "expenses": 190431,
                "full_contribution": 229999,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 229999,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 145208,
                    "Long-Term Maintenance": 2224196,
                    "Operating Reserve": 136881
                }
            },
            "2046": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 236899,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 236899,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 146660,
                    "Long-Term Maintenance": 2483337,
                    "Operating Reserve": 138250
                }
            },
            "2047": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 244006,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 244006,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 148126,
                    "Long-Term Maintenance": 2752176,
                    "Operating Reserve": 139632
                }
            },
            "2048": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 251326,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 251326,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 149608,
                    "Long-Term Maintenance": 3031023,
                    "Operating Reserve": 141029
                }
            },
            "2049": {
                "maintenance": {
                    "Entry Stoops — Leveling & Stair Nosing (safety)": 58023,
                    "Siding, Vinyl": 3260083
                },
                "expenses": 3318106,
                "full_contribution": 258866,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 258866,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 151104,
                    "Long-Term Maintenance": 2093,
                    "Operating Reserve": 142439
                }
            },
            "2050": {
                "maintenance": {},
                "expenses": 0,
                "full_contribution": 266632,
                "contributions": {
                    "Emergency Reserve": 0,
                    "Long-Term Maintenance": 266632,
                    "Operating Reserve": 0
                },
                "closing_balances": {
                    "Emergency Reserve": 152615,
                    "Long-Term Maintenance": 268745,
                    "Operating Reserve": 143863
                }
            }
        },
        "starting_balance_2027": {
            "Emergency Reserve": 23100,
            "Long-Term Maintenance": 91605,
            "Operating Reserve": 61899
        },
        "emergency_reserve_target": 125000,
        "operating_reserve_floor": 117860,
        "units": 98
    };
});
