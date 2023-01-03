# Pratyush
import csv
import math

input_file = "Book2.csv"
output_file = "Hyundai_mapping2.csv"

#################################### Mappings ########################################

GENERATION_MAPPING = {
    '1ST GEN': 1
}

VARIANT_TYPE_TO_NUMBER = {
    'SX': 'A',
    'S(o)': 'B',
    'Asta(o)':'C',
    'Sportz': 'D',
    'Era': 'E',
    'Magna': 'F',
    'Asta': 'G',
    'Base': 'H',
    'Ex': 'I',
    'E': 'J',
    'SPlus': 'K',
    'Turbo': 'L',
    'SXPlus': 'M',
    'SXPlusTurbo': 'M',
    'SX(o)': 'N',
    'Sportz(o)': 'O',
    'Magna(o)': 'P',
    'EraPlus': 'Q',
    'S': 'R', 
    'MagnaPlus': 'S', 
    'EPlus': 'T'
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
    's+': 'S Plus', 
    'option': '(o)', 
    's': 'S', 
    'turbo': 'Turbo',
    'sx+': 'SX Plus', 
    'sx(o)': 'SX(o)'
}

MAKE = {
    'hyundai': 1
}

MODEL = {
    'creta': 1,
    'verna': 2,
    'fluidic verna': 2,
    'eon': 3,
    'elantra': 4,
    'venue': 5,
    'aura': 6,
    'i10': 7,
    # 'grand i10': 7,
    # 'new grand i10': 7,
    # 'grand i10 nios': 7,
    'i20': 8,
    # 'elite i20': 8,
    # 'i20 active': 8,
    # '120 elite': 8,
    # 'new elite i20': 8,
    'accent': 9,
    'santro': 13,
    'xcent': 16
}

FUEL_TYPE = {
    "petrol": 2,
    "internal_lpg_cng": 2,
    "diesel": 1,
}

########################################################################################


def engine_capacity(capacity_in_cc):
    cc = capacity_in_cc.replace("CC", "").replace("cc", "")
    cc = math.ceil(int(cc)/100)
    return f"{cc}" if cc >= 10 else f"0{cc}"
def get_formatted_variant(variant): 
    formatted_variant = ""
    for ele in variant.split(" "):
        formatted_variant += VARIANT[ele]
    return formatted_variant

def get_model_number(model):
    li = model.split(" ")
    for ele in li:
        if ele.lower() in MODEL.keys():
            return MODEL[ele.lower()]
    return None

def generate_mapping_id(make, model, variant, fuel_type, capacity_in_cc):
    print(f"{make} {model} {variant} {fuel_type} {capacity_in_cc}")
    if variant == "":
        return None
    return f"{MAKE.get(make.lower())}{get_model_number(model)}{VARIANT_TYPE_TO_NUMBER.get(get_formatted_variant(variant.lower()), VARIANT_TYPE_TO_NUMBER['Base'])}{engine_capacity(capacity_in_cc)}{FUEL_TYPE.get(fuel_type.lower())}"

def process_variant(car_variant):
    car_info = {}
    car_data = car_variant.split(" ")
    car_info["fuel_type"] = car_data[-1]
    car_info["engine_capacity"] = car_data[-2].replace("(", "").replace(")", "")
    engine_info = ""
    for ele in car_data:
        if ele.lower() in VARIANT:
            engine_info += ele.lower() + " "
    car_info["variant"] = "" if engine_info == "" else engine_info.strip() # if model is not found then makeing it empty
    return car_info

def read_csv():
    cars_data = []
    with open(input_file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            car_data = process_variant(row["variant"].replace(row["model"], "").replace(row["make"], ""))
            make = row["make"]
            made = row["model"]
            variant = car_data["variant"]
            fuel_type = car_data["fuel_type"]
            engine_capacity = car_data["engine_capacity"]
            print(row["inspection_id"], sep="->")
            mapping_id = generate_mapping_id(make, made, variant, fuel_type, engine_capacity)
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

if __name__ == "__main__":
    cars_data = read_csv()
    write_csv(cars_data)
    input()