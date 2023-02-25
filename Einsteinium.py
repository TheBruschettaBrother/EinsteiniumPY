def periodic_table_get(element_name):
    # Dictionary containing information about each element
    elements = {
        "hydrogen": {
            "symbol": "H",
            "atomic number": 1,
            "atomic mass": 1.008,
            "group": 1,
            "period": 1,
            "category": "nonmetal"
        },
        "helium": {
            "symbol": "He",
            "atomic number": 2,
            "atomic mass": 4.003,
            "group": 18,
            "period": 1,
            "category": "noble gas"
        },
        "lithium": {
            "symbol": "Li",
            "atomic number": 3,
            "atomic mass": 6.941,
            "group": 1,
            "period": 2,
            "category": "alkali metal"
        },
        "beryllium": {
            "symbol": "Be",
            "atomic number": 4,
            "atomic mass": 9.012,
            "group": 2,
            "period": 2,
            "category": "alkaline earth metal"
        },
        "boron": {
            "symbol": "B",
            "atomic number": 5,
            "atomic mass": 10.81,
            "group": 13,
            "period": 2,
            "category": "metalloid"
        },
        "carbon": {
            "symbol": "C",
            "atomic number": 6,
            "atomic mass": 12.01,
            "group": 14,
            "period": 2,
            "category": "nonmetal"
        },
        "nitrogen": {
            "symbol": "N",
            "atomic number": 7,
            "atomic mass": 14.01,
            "group": 15,
            "period": 2,
            "category": "nonmetal"
        },
        "oxygen": {
            "symbol": "O",
            "atomic number": 8,
            "atomic mass": 16.00,
            "group": 16,
            "period": 2,
            "category": "nonmetal"
        },
        "fluorine": {
            "symbol": "F",
            "atomic number": 9,
            "atomic mass": 19.00,
            "group": 17,
            "period": 2,
            "category": "halogen"
        },
        "neon": {
            "symbol": "Ne",
            "atomic number": 10,
            "atomic mass": 20.18,
            "group": 18,
            "period": 2,
            "category": "noble gas"
        },
        "sodium": {
            "symbol": "Na",
            "atomic number": 11,
            "atomic mass": 22.99,
            "group": 1,
            "period": 3,
            "category": "alkali metal"
        },
        "magnesium": {
            "symbol": "Mg",
            "atomic number": 12,
            "atomic mass": 24.31,
            "group": 2,
            "period": 3,
            "category": "alkaline earth metal"
        },
        "aluminium": {
            "symbol": "Al",
            "atomic number": 13,
            "atomic mass": 26.982,
            "group": 13,
            "period": 3,
            "category": "metal"
        },
        "silicon": {
            "symbol": "Si",
            "atomic number": 14,
            "atomic mass": 28.086,
            "group": 14,
            "period": 3,
            "category": "metalloid"
        },
        "phosphorus": {
            "symbol": "P",
            "atomic number": 15,
            "atomic mass": 30.974,
            "group": 15,
            "period": 3,
            "category": "nonmetal"
        },
        "sulfur": {
                "symbol": "S",
                "atomic number": 16,
                "atomic mass": 32.06,
                "group": 16,
                "period": 3,
                "category": "nonmetal"
            },
        "chlorine": {
                "symbol": "Cl",
                "atomic number": 17,
                "atomic mass": 35.45,
                "group": 17,
                "period": 3,
                "category": "halogen"
            },
        "argon": {
                "symbol": "Ar",
                "atomic number": 18,
                "atomic mass": 39.948,
                "group": 18,
                "period": 3,
                "category": "noble gas"
            },
        "potassium": {
                "symbol": "K",
                "atomic number": 19,
                "atomic mass": 39.098,
                "group": 1,
                "period": 4,
                "category": "alkali metal"
            },
        "calcium": {
                "symbol": "Ca",
                "atomic number": 20,
                "atomic mass": 40.078,
                "group": 2,
                "period": 4,
                "category": "alkaline earth metal"
            },
        "scandium": {
                "symbol": "Sc",
                "atomic number": 21,
                "atomic mass": 44.956,
                "group": 3,
                "period": 4,
                "category": "transition metal"
            },
        "titanium": {
                "symbol": "Ti",
                "atomic number": 22,
                "atomic mass": 47.867,
                "group": 4,
                "period": 4,
                "category": "transition metal"
            },
        "vanadium": {
                "symbol": "V",
                "atomic number": 23,
                "atomic mass": 50.942,
                "group": 5,
                "period": 4,
                "category": "transition metal"
            },
        "chromium": {
                "symbol": "Cr",
                "atomic number": 24,
                "atomic mass": 52.0,
                "group": 6,
                "period": 4,
                "category": "transition metal"
            },
        "manganese": {
                "symbol": "Mn",
                "atomic number": 25,
                "atomic mass": 54.938,
                "group": 7,
                "period": 4,
                "category": "transition metal"
            },
        "iron": {
            "symbol": "Fe",
            "atomic number": 26,
            "atomic mass": 55.845,
            "group": 8,
            "period": 4,
            "category": "transition metal"
        },
        "cobalt": {
            "symbol": "Co",
            "atomic number": 27,
            "atomic mass": 58.933,
            "group": 9,
            "period": 4,
            "category": "transition metal"
        },
        "nickel": {
            "symbol": "Ni",
            "atomic number": 28,
            "atomic mass": 58.693,
            "group": 10,
            "period": 4,
            "category": "transition metal"
        },
        "copper": {
            "symbol": "Cu",
            "atomic number": 29,
            "atomic mass": 63.546,
            "group": 11,
            "period": 4,
            "category": "transition metal"
        },
        "zinc": {
            "symbol": "Zn",
            "atomic number": 30,
            "atomic mass": 65.38,
            "group": 12,
            "period": 4,
            "category": "transition metal"
        },
        "gallium": {
            "symbol": "Ga",
            "atomic number": 31,
            "atomic mass": 69.723,
            "group": 13,
            "period": 4,
            "category": "post-transition metal"
        },
        "germanium": {
            "symbol": "Ge",
            "atomic number": 32,
            "atomic mass": 72.63,
            "group": 14,
            "period": 4,
            "category": "metalloid"
        },
        "arsenic": {
            "symbol": "As",
            "atomic number": 33,
            "atomic mass": 74.922,
            "group": 15,
            "period": 4,
            "category": "metalloid"
        },
        "selenium": {
            "symbol": "Se",
            "atomic number": 34,
            "atomic mass": 78.96,
            "group": 16,
            "period": 4,
            "category": "nonmetal"
        },
        "bromine": {
            "symbol": "Br",
            "atomic number": 35,
            "atomic mass": 79.904,
            "group": 17,
            "period": 4,
            "category": "halogen"
        },
        "krypton": {
            "symbol": "Kr",
            "atomic number": 36,
            "atomic mass": 83.798,
            "group": 18,
            "period": 4,
            "category": "noble gas"
        },
        "rubidium": {
            "symbol": "Rb",
            "atomic number": 37,
            "atomic mass": 85.468,
            "group": 1,
            "period": 5,
            "category": "alkali metal"
        },
        "strontium": {
            "symbol": "Sr",
            "atomic number": 38,
            "atomic mass": 87.62,
            "group": 2,
            "period": 5,
            "category": "alkaline earth metal"
        },
        "yttrium": {
            "symbol": "Y",
            "atomic number": 39,
            "atomic mass": 88.905,
            "group": 3,
            "period": 5,
            "category": "transition metal"
        },
        "zirconium": {
            "symbol": "Zr",
            "atomic number": 40,
            "atomic mass": 91.224,
            "group": 4,
            "period": 5,
            "category": "transition metal"
        },
        "niobium": {
            "symbol": "Nb",
            "atomic number": 41,
            "atomic mass": 92.906,
            "group": 5,
            "period": 5,
            "category": "transition metal"
        },
        "molybdenum": {
            "symbol": "Mo",
            "atomic number": 42,
            "atomic mass": 95.94,
            "group": 6,
            "period": 5,
            "category": "transition metal"
        },
        "technetium": {
            "symbol": "Tc",
            "atomic number": 43,
            "atomic mass": 98,
            "group": 7,
            "period": 5,
            "category": "transition metal"
        },
        "ruthenium": {
            "symbol": "Ru",
            "atomic number": 44,
            "atomic mass": 101.07,
            "group": 8,
            "period": 5,
            "category": "transition metal"
        },
        "rhodium": {
            "symbol": "Rh",
            "atomic number": 45,
            "atomic mass": 102.91,
            "group": 9,
            "period": 5,
            "category": "transition metal"
        },
        "palladium": {
            "symbol": "Pd",
            "atomic number": 46,
            "atomic mass": 106.42,
            "group": 10,
            "period": 5,
            "category": "transition metal"
        },
        "silver": {
            "symbol": "Ag",
            "atomic number": 47,
            "atomic mass": 107.87,
            "group": 11,
            "period": 5,
            "category": "transition metal"
        },
        "cadmium": {
            "symbol": "Cd",
            "atomic number": 48,
            "atomic mass": 112.41,
            "group": 12,
            "period": 5,
            "category": "transition metal"
        },
        "indium": {
            "symbol": "In",
            "atomic number": 49,
            "atomic mass": 114.82,
            "group": 13,
            "period": 5,
            "category": "post-transition metal"
        },
        "tin": {
            "symbol": "Sn",
            "atomic number": 50,
            "atomic mass": 118.710,
            "group": 14,
            "period": 5,
            "category": "metal"
        },
        "antimony": {
            "symbol": "Sb",
            "atomic number": 51,
            "atomic mass": 121.760,
            "group": 15,
            "period": 5,
            "category": "metalloid"
        },
        "tellurium": {
            "symbol": "Te",
            "atomic number": 52,
            "atomic mass": 127.600,
            "group": 16,
            "period": 5,
            "category": "metalloid"
        },
        "iodine": {
            "symbol": "I",
            "atomic number": 53,
            "atomic mass": 126.90447,
            "group": 17,
            "period": 5,
            "category": "halogen"
        },
        "xenon": {
            "symbol": "Xe",
            "atomic number": 54,
            "atomic mass": 131.293,
            "group": 18,
            "period": 5,
            "category": "noble gas"
        },
        "cesium": {
            "symbol": "Cs",
            "atomic number": 55,
            "atomic mass": 132.90545196,
            "group": 1,
            "period": 6,
            "category": "alkali metal"
        },
        "barium": {
            "symbol": "Ba",
            "atomic number": 56,
            "atomic mass": 137.327,
            "group": 2,
            "period": 6,
            "category": "alkaline earth metal"
        },
        "lanthanum": {
            "symbol": "La",
            "atomic number": 57,
            "atomic mass": 138.90547,
            "group": None,
            "period": 6,
            "category": "lanthanide"
        },
        "cerium": {
            "symbol": "Ce",
            "atomic number": 58,
            "atomic mass": 140.116,
            "group": None,
            "period": 6,
            "category": "lanthanide"
        },
        "praseodymium": {
            "symbol": "Pr",
            "atomic number": 59,
            "atomic mass": 140.90766,
            "group": None,
            "period": 6,
            "category": "lanthanide"
        },
        "neodymium": {
            "symbol": "Nd",
            "atomic number": 60,
            "atomic mass": 144.242,
            "group": None,
            "period": 6,
            "category": "lanthanide"
        },
        "promethium": {
            "symbol": "Pm",
            "atomic number": 61,
            "atomic mass": 145,
            "group": None,
            "period": 6,
            "category": "lanthanide"
        },
        "samarium": {
            "symbol": "Sm",
            "atomic number": 62,
            "atomic mass": 150.36,
            "group": 3,
            "period": 6,
            "category": "lanthanide"
        },
        "europium": {
            "symbol": "Eu",
            "atomic number": 63,
            "atomic mass": 151.964,
            "group": "n/a",
            "period": 6,
            "category": "lanthanide"
        },
        "gadolinium": {
            "symbol": "Gd",
            "atomic number": 64,
            "atomic mass": 157.25,
            "group": 3,
            "period": 6,
            "category": "lanthanide"
        },
        "terbium": {
            "symbol": "Tb",
            "atomic number": 65,
            "atomic mass": 158.925,
            "group": 3,
            "period": 6,
            "category": "lanthanide"
        },
        "dysprosium": {
            "symbol": "Dy",
            "atomic number": 66,
            "atomic mass": 162.5,
            "group": 3,
            "period": 6,
            "category": "lanthanide"
        },
        "holmium": {
            "symbol": "Ho",
            "atomic number": 67,
            "atomic mass": 164.93,
            "group": 3,
            "period": 6,
            "category": "lanthanide"
        },
        "erbium": {
            "symbol": "Er",
            "atomic number": 68,
            "atomic mass": 167.259,
            "group": 3,
            "period": 6,
            "category": "lanthanide"
        },
        "thulium": {
            "symbol": "Tm",
            "atomic number": 69,
            "atomic mass": 168.934,
            "group": 3,
            "period": 6,
            "category": "lanthanide"
        },
        "ytterbium": {
            "symbol": "Yb",
            "atomic number": 70,
            "atomic mass": 173.054,
            "group": 3,
            "period": 6,
            "category": "lanthanide"
        },
        "lutetium": {
            "symbol": "Lu",
            "atomic number": 71,
            "atomic mass": 174.967,
            "group": 3,
            "period": 6,
            "category": "lanthanide"
        },
        "hafnium": {
            "symbol": "Hf",
            "atomic number": 72,
            "atomic mass": 178.49,
            "group": 4,
            "period": 6,
            "category": "transition metal"
        },
        "tantalum": {
            "symbol": "Ta",
            "atomic number": 73,
            "atomic mass": 180.948,
            "group": 5,
            "period": 6,
            "category": "transition metal"
        },
        "tungsten": {
            "symbol": "W",
            "atomic number": 74,
            "atomic mass": 183.84,
            "group": 6,
            "period": 6,
            "category": "transition metal"
        },
        "rhenium": {
            "symbol": "Re",
            "atomic number": 75,
            "atomic mass": 186.207,
            "group": 7,
            "period": 6,
            "category": "transition metal"
        },
        "osmium": {
            "symbol": "Os",
            "atomic number": 76,
            "atomic mass": 190.23,
            "group": 8,
            "period": 6,
            "category": "transition metal"
        },
        "iridium": {
            "symbol": "Ir",
            "atomic number": 77,
            "atomic mass": 192.217,
            "group": 9,
            "period": 6,
            "category": "transition metal"
        },
        "platinum": {
            "symbol": "Pt",
            "atomic number": 78,
            "atomic mass": 195.084,
            "group": 10,
            "period": 6,
            "category": "transition metal"
        },
        "gold": {
            "symbol": "Au",
            "atomic number": 79,
            "atomic mass": 196.967,
            "group": 11,
            "period": 6,
            "category": "transition metal"
        },
        "mercury": {
            "symbol": "Hg",
            "atomic number": 80,
            "atomic mass": 200.592,
            "group": 12,
            "period": 6,
            "category": "transition metal"
        },
        "thallium": {
            "symbol": "Tl",
            "atomic number": 81,
            "atomic mass": 204.38,
            "group": 13,
            "period": 6,
            "category": "post-transition metal"
        },
        "lead": {
            "symbol": "Pb",
            "atomic number": 82,
            "atomic mass": 207.2,
            "group": 14,
            "period": 6,
            "category": "post-transition metal"
        },
        "bismuth": {
            "symbol": "Bi",
            "atomic number": 83,
            "atomic mass": 208.98,
            "group": 15,
            "period": 6,
            "category": "post-transition metal"
        },
        "polonium": {
            "symbol": "Po",
            "atomic number": 84,
            "atomic mass": 209,
            "group": 16,
            "period": 6,
            "category": "metalloid"
        },
        "astatine": {
            "symbol": "At",
            "atomic number": 85,
            "atomic mass": 210,
            "group": 17,
            "period": 6,
            "category": "halogen"
        },
        "radon": {
            "symbol": "Rn",
            "atomic number": 86,
            "atomic mass": 222,
            "group": 18,
            "period": 6,
            "category": "noble gas"
        },
        "francium": {
            "symbol": "Fr",
            "atomic number": 87,
            "atomic mass": 223.02,
            "group": 1,
            "period": 7,
            "category": "alkali metal"
        },
        "radium": {
            "symbol": "Ra",
            "atomic number": 88,
            "atomic mass": 226.03,
            "group": 2,
            "period": 7,
            "category": "alkaline earth metal"
        },
        "actinium": {
            "symbol": "Ac",
            "atomic number": 89,
            "atomic mass": 227.03,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "thorium": {
            "symbol": "Th",
            "atomic number": 90,
            "atomic mass": 232.04,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "protactinium": {
            "symbol": "Pa",
            "atomic number": 91,
            "atomic mass": 231.04,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "uranium": {
            "symbol": "U",
            "atomic number": 92,
            "atomic mass": 238.03,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "neptunium": {
            "symbol": "Np",
            "atomic number": 93,
            "atomic mass": 237.05,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "plutonium": {
            "symbol": "Pu",
            "atomic number": 94,
            "atomic mass": 244.06,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "americium": {
            "symbol": "Am",
            "atomic number": 95,
            "atomic mass": 243.06,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "curium": {
            "symbol": "Cm",
            "atomic number": 96,
            "atomic mass": 247.07,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "berkelium": {
            "symbol": "Bk",
            "atomic number": 97,
            "atomic mass": 247.07,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "californium": {
            "symbol": "Cf",
            "atomic number": 98,
            "atomic mass": 251.08,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "einsteinium": {
            "symbol": "Es",
            "atomic number": 99,
            "atomic mass": 252.08,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "fermium": {
            "symbol": "Fm",
            "atomic number": 100,
            "atomic mass": 257,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "mendelevium": {
            "symbol": "Md",
            "atomic number": 101,
            "atomic mass": 258,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "nobelium": {
            "symbol": "No",
            "atomic number": 102,
            "atomic mass": 259,
            "group": None,
            "period": 7,
            "category": "actinide"
        },
        "lawrencium": {
            "symbol": "Lr",
            "atomic number": 103,
            "atomic mass": 262,
            "group": 3,
            "period": 7,
            "category": "transition metal"
        },
        "rutherfordium": {
            "symbol": "Rf",
            "atomic number": 104,
            "atomic mass": 261,
            "group": 4,
            "period": 7,
            "category": "transition metal"
        },
        "dubnium": {
            "symbol": "Db",
            "atomic number": 105,
            "atomic mass": 262,
            "group": 5,
            "period": 7,
            "category": "transition metal"
        },
        "seaborgium": {
            "symbol": "Sg",
            "atomic number": 106,
            "atomic mass": 266,
            "group": 6,
            "period": 7,
            "category": "transition metal"
        },
        "bohrium": {
            "symbol": "Bh",
            "atomic number": 107,
            "atomic mass": 264,
            "group": 7,
            "period": 7,
            "category": "transition metal"
        },
        "hassium": {
            "symbol": "Hs",
            "atomic number": 108,
            "atomic mass": 267,
            "group": 8,
            "period": 7,
            "category": "transition metal"
        },
        "meitnerium": {
            "symbol": "Mt",
            "atomic number": 109,
            "atomic mass": 268,
            "group": 9,
            "period": 7,
            "category": "transition metal"
        },
        "darmstadtium": {
            "symbol": "Ds",
            "atomic number": 110,
            "atomic mass": 271,
            "group": 10,
            "period": 7,
            "category": "transition metal"
        },
        "roentgenium": {
            "symbol": "Rg",
            "atomic number": 111,
            "atomic mass": 272,
            "group": 11,
            "period": 7,
            "category": "transition metal"
        },
        "copernicium": {
            "symbol": "Cn",
            "atomic number": 112,
            "atomic mass": 277,
            "group": 12,
            "period": 7,
            "category": "transition metal"
        },
        "nihonium": {
            "symbol": "Nh",
            "atomic number": 113,
            "atomic mass": 284,
            "group": 13,
            "period": 7,
            "category": "metal"
        },
        "flerovium": {
            "symbol": "Fl",
            "atomic number": 114,
            "atomic mass": 289,
            "group": 14,
            "period": 7,
            "category": "metal"
        },
        "moscovium": {
            "symbol": "Mc",
            "atomic number": 115,
            "atomic mass": 288,
            "group": 15,
            "period": 7,
            "category": "metal"
        },
        "livermorium": {
            "symbol": "Lv",
            "atomic number": 116,
            "atomic mass": 293,
            "group": 16,
            "period": 7,
            "category": "metal"
        },
        "tennessine": {
            "symbol": "Ts",
            "atomic number": 117,
            "atomic mass": 294,
            "group": 17,
            "period": 7,
            "category": "halogen"
        },
        "oganesson": {
            "symbol": "Og",
            "atomic number": 118,
            "atomic mass": 294,
            "group": 18,
            "period": 7,
            "category": "noble gas"
        }
    }

    # Convert the input to lowercase for easier comparison
    element_name = element_name.lower()

    # Check if the element exists in the dictionary
    if element_name in elements:
        # Return the information about the element
        return elements[element_name]
    else:
        # If the element doesn't exist in the dictionary, return None
        return None
