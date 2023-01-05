# Pratyush
import csv
import math
from datetime import date

input_file = "ako.csv"
output_file = "acko_mapping.csv"
insdatabase = "insdatabase.csv"

#################################### Mappings ########################################

GENERATION_MAPPING = {
    "accent": {
        "1999-2013": {
            "start": 1999,
            "end": 2013,
            "mapping_id": "01"
        }
    },
    "alcazar": {
        "2021-NOW": {
            "start": 2021,
            "end": 2023,
            "mapping_id": "01"
        }
    },
    "aura": {
        "2020-NOW": {
            "start": 2020,
            "end": 2023,
            "mapping_id": "01"
        }
    },
    "creta": {
        "2015-2018": {
            "start": 2015,
            "end": 2018,
            "mapping_id": "01"
        },
        "2018-2020": {
            "start": 2018,
            "end": 2020,
            "mapping_id": "02"
        },
        "2020-NOW": {
            "start": 2020,
            "end": 2023,
            "mapping_id": "03"
        }
    },
    "elantra": {
        "2004-2007": {
            "start": 2004,
            "end": 2007,
            "mapping_id": "01"
        },
        "2016-2019": {
            "start": 2016,
            "end": 2019,
            "mapping_id": "02"
        },
        "2019-NOW": {
            "start": 2019,
            "end": 2023,
            "mapping_id": "03"
        }
    },
    "eon": {
        "2011-2019": {
            "start": 2011,
            "end": 2019,
            "mapping_id": "01"
        }
    },
    "fluidic elantra": {
        "2012-2015": {
            "start": 2012,
            "end": 2015,
            "mapping_id": "01"
        }
    },
    "getz": {
        "2004-2007": {
            "start": 2004,
            "end": 2007,
            "mapping_id": "01"
        }
    },
    "getz prime": {
        "2007-2010": {
            "start": 2007,
            "end": 2010,
            "mapping_id": "01"
        }
    },
    "grand i10": {
        "2013-2016": {
            "start": 2013,
            "end": 2016,
            "mapping_id": "01"
        },
        "2016-2021": {
            "start": 2016,
            "end": 2021,
            "mapping_id": "02"
        },
        "2007-2010": {
            "start": 2007,
            "end": 2010,
            "mapping_id": "03"
        },
        "2010-2013": {
            "start": 2010,
            "end": 2013,
            "mapping_id": "04"
        }
    },
    "grand i10 nios": {
        "08.2019-NOW": {
            "start": 2019,
            "end": 2023,
            "mapping_id": "01"
        }
    },
    "i10": {
        "2013-2016": {
            "start": 2013,
            "end": 2016,
            "mapping_id": "01"
        },
        "2016-2021": {
            "start": 2016,
            "end": 2021,
            "mapping_id": "02"
        },
        "2007-2010": {
            "start": 2007,
            "end": 2010,
            "mapping_id": "03"
        },
        "2010-2013": {
            "start": 2010,
            "end": 2013,
            "mapping_id": "04"
        }
    },
    "i20": {
        "2008-2012": {
            "start": 2008,
            "end": 2012,
            "mapping_id": "01"
        },
        "2012-2014": {
            "start": 2012,
            "end": 2014,
            "mapping_id": "02"
        },
        "09.2020-NOW": {
            "start": 2020,
            "end": 2023,
            "mapping_id": "03"
        }
    },
    "i20 active": {
        "2015-2018": {
            "start": 2015,
            "end": 2018,
            "mapping_id": "01"
        }
    },
    "i20 elite": {
        "2014-2018": {
            "start": 2014,
            "end": 2018,
            "mapping_id": "01"
        },
        "2018-2020": {
            "start": 2018,
            "end": 2020,
            "mapping_id": "02"
        }
    },
    "kona electric": {
        "06.2019-NOW": {
            "start": 2019,
            "end": 2023,
            "mapping_id": "01"
        }
    },
    "santa fe": {
        "2009-2013": {
            "start": 2009,
            "end": 2013,
            "mapping_id": "01"
        },
        "2013-2017": {
            "start": 2013,
            "end": 2017,
            "mapping_id": "02"
        }
    },
    "santro": {
        "1998-2003": {
            "start": 1998,
            "end": 2003,
            "mapping_id": "01"
        },
        "2018-NOW": {
            "start": 2018,
            "end": 2023,
            "mapping_id": "02"
        },
        "2003-2014": {
            "start": 2003,
            "end": 2014,
            "mapping_id": "03"
        }
    },
    "santro xing": {
        "1998-2003": {
            "start": 1998,
            "end": 2003,
            "mapping_id": "01"
        },
        "2018-NOW": {
            "start": 2018,
            "end": 2023,
            "mapping_id": "02"
        },
        "2003-2014": {
            "start": 2003,
            "end": 2014,
            "mapping_id": "03"
        }
    },
    "sonata": {
        "2001-2006": {
            "start": 2001,
            "end": 2006,
            "mapping_id": "01"
        },
        "2005-2011": {
            "start": 2005,
            "end": 2011,
            "mapping_id": "02"
        },
        "2012-2014": {
            "start": 2012,
            "end": 2014,
            "mapping_id": "03"
        }
    },
    "terracan": {
        "2003-2005": {
            "start": 2003,
            "end": 2005,
            "mapping_id": "01"
        }
    },
    "tucson": {
        "2004-2008": {
            "start": 2004,
            "end": 2008,
            "mapping_id": "01"
        },
        "2013-2015": {
            "start": 2013,
            "end": 2015,
            "mapping_id": "02"
        },
        "2016-2020": {
            "start": 2016,
            "end": 2020,
            "mapping_id": "03"
        }
    },
    "venue": {
        "2019-2021": {
            "start": 2019,
            "end": 2021,
            "mapping_id": "01"
        }
    },
    "verna": {
        "2011-2014": {
            "start": 2011,
            "end": 2014,
            "mapping_id": "01"
        },
        "2014-2017": {
            "start": 2014,
            "end": 2017,
            "mapping_id": "02"
        },
        "2006-2011": {
            "start": 2006,
            "end": 2011,
            "mapping_id": "03"
        },
        "08.2017-05.2020": {
            "start": 2017,
            "end": 2020,
            "mapping_id": "04"
        },
        "03.2020-NOW": {
            "start": 2020,
            "end": 2023,
            "mapping_id": "05"
        }
    },
    "verna fluidic": {
        "2011-2014": {
            "start": 2011,
            "end": 2014,
            "mapping_id": "01"
        },
        "2014-2017": {
            "start": 2014,
            "end": 2017,
            "mapping_id": "02"
        },
        "2006-2011": {
            "start": 2006,
            "end": 2011,
            "mapping_id": "03"
        },
        "08.2017-05.2020": {
            "start": 2017,
            "end": 2020,
            "mapping_id": "04"
        },
        "03.2020-NOW": {
            "start": 2020,
            "end": 2023,
            "mapping_id": "05"
        }
    },
    "xcent": {
        "2013-2016": {
            "start": 2013,
            "end": 2016,
            "mapping_id": "01"
        },
        "2016-2020": {
            "start": 2016,
            "end": 2020,
            "mapping_id": "02"
        }
    }
}

VARIANT_TYPE_TO_NUMBER = {
    'SX': 'AA',
    'S(o)': 'AB',
    'Asta(o)':'AC',
    'Sportz': 'AD',
    'Era': 'AE',
    'Magna': 'AF',
    'Asta': 'AG',
    'Base': 'AH',
    'Ex': 'AI',
    'E': 'AJ',
    'SPlus': 'AK',
    'Turbo': 'AL',
    'SXPlus': 'AM',
    'SXPlusTurbo': 'AM',
    'SX(o)': 'AN',
    'Sportz(o)': 'AO',
    'Magna(o)': 'AP',
    'EraPlus': 'AQ',
    'S': 'AR', 
    'MagnaPlus': 'AS', 
    'EPlus': 'AT',
    'GLE': 'AU',
    'GVS': 'AV',
    'GVS(o)': 'AW',
    'GVS(option)': 'AW',
    'GLS': 'AX',
    'TRANSFORM': 'AY',
    'EMBERA': 'AZ',
    'GL': 'BA'
}

VARIANT = {
    'sx_abs': 'SX',
    's(o)': 'S(o)', 
    'asta(o)': 'Asta(o)',
    'sport': 'Sportz',
    'sports': 'Sportz',
    'sportz': 'Sportz', 
    'era': 'Era', 
    'magna': 'Magna', 
    'asta': 'Asta', 
    'base': 'Base', 
    'optional': '(o)', 
    '(o)': '(o)', 
    'ex': 'Ex', 
    'e': 'E',
    'era': 'Era',
    'sx': 'SX', 
    'plus': 'Plus', 
    's+': 'SPlus', 
    'option': '(o)', 
    's': 'S', 
    'turbo': 'Turbo',
    'sx+': 'SXPlus', 
    'sx(o)': 'SX(o)',
    'gle': 'GLE',
    'gvs': 'GVS',
    'gvs(o)': 'GVS(o)',
    'gvs(option)': 'GVS(o)',
    'gls': 'GLS',
    'transform': 'TRANSFORM',
    'EMBERA': 'embera',
    'gl': 'GL'
}

MAKE = {
    'hyundai': 1
}

MODEL = {
    'creta': "01",
    'verna': "02",
    'verna fluidic': "02",
    'eon': "03",
    'elantra': "04",
    'fluidic elantra': "04",
    'venue': "05",
    'aura': "06",
    'i10': "07",
    'grand i10': "07",
    'new grand i10': "07",
    'grand i10 nios': "08",
    'i20': "09",
    'elite i20': "10",
    'i20 active': "11",
    'i20 elite': "10",
    'elite i20': "10",
    'active i20': "11",
    'new elite i20': "10",
    'accent': "12",
    'santro': "13",
    'santro xing': "13",
    'xcent': "14",
    'alcazar': "15",
    'getz': "16",
    'getz prime': "17",
    'tucson': "18",
    'sonata': "19",
    'santa fe': "20",
    'terracan': "21",
    'kona electric': "22"
}

FUEL_TYPE = {
    "petrol": 2,
    "internal_lpg_cng": 2,
    "diesel": 1,
    "electric": 3
}

########################################################################################


def engine_capacity(capacity_in_cc):
    cc = capacity_in_cc.lower().replace("cc", "").replace("kwh", "")
    cc = math.ceil(int(cc)/100)
    return f"{cc}" if cc >= 10 else f"0{cc}"

def get_formatted_variant(variant): 
    formatted_variant = ""
    for ele in variant.split(" "):
        formatted_variant += VARIANT[ele]
    return formatted_variant

def get_model_number(model):
    li = model.lower().replace("(2020)","").strip().split(" ")
    for key in MODEL.keys():
        found = True
        for ele in li:
            print(f"{key}->{ele}")
            if ele not in key:
                found = False
        if not found:
            continue
        return MODEL.get(key)
    return None

def vehicle_generation_mapping_id(model,registration_year):
    if registration_year == "NA":
        return None
    registration_year = int(registration_year)
    li = model.lower().replace("(2020)","").strip().split(" ")
    model_generation_mapping = None
    for key, value in GENERATION_MAPPING.items():
        found = True
        for ele in li:
            if ele not in key:
                print(f"{key}->{ele}")
                found = False
        if not found:
            continue
        model_generation_mapping = value
        break
    if model_generation_mapping:
        print(model_generation_mapping)
        generation_mapping_id = None
        for key, value in model_generation_mapping.items():
            print(registration_year)
            if value["start"] <= registration_year and value["end"] >= registration_year:
                generation_mapping_id = value["mapping_id"]
        return generation_mapping_id
    return None

def generate_mapping_id(make, model, variant, fuel_type, capacity_in_cc, registration_year):
    if variant == "":
        return None
    return f"{MAKE.get(make.lower())}{get_model_number(model)}{vehicle_generation_mapping_id(model, registration_year)}{VARIANT_TYPE_TO_NUMBER.get(get_formatted_variant(variant.lower()), VARIANT_TYPE_TO_NUMBER['Base'])}{engine_capacity(capacity_in_cc)}{FUEL_TYPE.get(fuel_type.lower())}"

def process_variant(car_variant):
    car_info = {}
    car_data = car_variant.split(" ")
    car_info["fuel_type"] = car_data[-1]
    car_info["engine_capacity"] = car_data[-2].replace("(", "").replace(")", "")
    engine_info = ""
    for ele in car_data:
        if ele.lower() in VARIANT:
            engine_info += ele.lower() + " "
    car_info["variant"] = "base" if engine_info == "" else engine_info.strip() # if model is not found then makeing it empty
    return car_info

def read_csv():
    cars_data = []
    with open(input_file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            car_data = process_variant(row["variant"].replace(row["model"], "").replace(row["make"], ""))
            make = row["make"]
            made = row["model"]
            registration_year = row["registration_year"]
            variant = car_data["variant"]
            fuel_type = car_data["fuel_type"]
            engine_capacity = car_data["engine_capacity"]
            mapping_id = generate_mapping_id(make, made, variant, fuel_type, engine_capacity, registration_year)
            di = {
                "inspection_id": row["inspection_id"],
                "make": make,
                "model": made,
                "variant": variant,
                "fuel_type": fuel_type,
                "engine_capacity": engine_capacity,
                "mapping_id": mapping_id
            }
            cars_data.append(di)
    return cars_data
    
def write_csv(cars_data):
    fieldnames = ['mapping_id', 'inspection_id', 'make', 'model', 'variant', 'fuel_type', 'engine_capacity']
    with open(output_file, mode='w') as hyundai_file:
        cars_data_writer = csv.DictWriter(hyundai_file, fieldnames=fieldnames)
        for di in cars_data:
            cars_data_writer.writerow(di)
            
def prepare_for_insdatabase():
    current_counter = {}
    todays_date = date.today()
    with open("insdatabase.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            model = row["Model"].lower().split("/")[0].strip()
            if model not in GENERATION_MAPPING:
                GENERATION_MAPPING[model] = {}
                current_counter[model] = 1
            year = row["Variant"].replace("-", " ").replace("(", " ").replace(")","").split(" ")
            end = year[-1]
            start = year[-2]
            year = f"{start}-{end}"
            if year not in GENERATION_MAPPING[model]:
                cnt = current_counter[model]
                GENERATION_MAPPING[model][year] = {
                    "start": int(start.split(".")[-1]),
                    "end": int(end.split(".")[-1]) if end.lower() != "now" else todays_date.year,
                    "mapping_id": f"0{cnt}" if cnt < 10 else f"{cnt}"
                }
                current_counter[model] = cnt + 1
                
def generate_unique_id_for_insdatabase():
    di = {}
    with open("insdatabase.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            model = row["Model"].lower().split("/")[0].strip()
            make = row["Make"].lower()
            sub_variant = row["Sub_variant"].lower()
            variant = row["Variant"]
            fuel_identifier = FUEL_TYPE[next(key for key in FUEL_TYPE.keys() if key in sub_variant)]
            engine_capacity_in_cc = int(sub_variant.split(" ")[1].replace("L", "")) * 1000
            date_range = variant.split("")
            generation_mapping = GENERATION_MAPPING.get(model)
            unique_id = f"{MAKE.get(make)}{get_model_number(model)}{vehicle_generation_mapping_id(model, registration_year)}{VARIANT_TYPE_TO_NUMBER.get(get_formatted_variant(variant.lower()), VARIANT_TYPE_TO_NUMBER['Base'])}{engine_capacity(engine_capacity_in_cc)}{fuel_identifier}"

if __name__ == "__main__":
    # read_insdatabase()
    cars_data = read_csv()
    write_csv(cars_data)
    # print(GENERATION_MAPPING)