import re

# Lista de registros médicos de pacientes
# Cada registro es un diccionario con los campos
# patient_id, age, gender, diagnosis, medications y last_visit_id
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

# Esta función verifica que cada campo cumpla con el formato esperado
# Devuelve una lista con los nombres de los campos que NO cumplen las reglas
# Si todos los campos son válidos devuelve una lista vacía
def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {

        # patient_id debe ser un string que empiece con 'p' (mayúscula o minúscula)
        'patient_id': isinstance(patient_id, str) and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE), # r'p' -> que comience con p, r'\d+' y que tenga más de un dígito

        # age debe ser un entero y mayor de 18
        'age': isinstance(age, int) and age >= 18,

        # gender debe ser un string y su valor (ignorando mayúsculas) debe ser 'male' or 'female'
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),

        # diagnosis puede ser un string o None
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # medications debe ser una lista y cada elemento de esta lista debe ser un string
        'medications': isinstance(medications, list) and all([isinstance(i, str) for i in medications]),

        # last_visit_id debe ser un string que empiece con 'v' (mayúscula o minúscula) y que tenga uno o más dígitos
        'last_visit_id': isinstance(last_visit_id, str) and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
    }

    # Retorna solo los campos cuya validación es False
    return [key for key, value in constraints.items() if not value]

# 
def validate(data):
    is_sequence = isinstance(data, (list, tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False

    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)

        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True

    if is_invalid:
        return False
    print('Valid format.')
    return True

validate(medical_records)
