import phonenumbers

def validar_telefono(telefono_str, codigo_pais=None):
    try:
        telefono = phonenumbers.parse(telefono_str, codigo_pais)
        return phonenumbers.is_valid_number(telefono)
    except Exception as e:
        print(e)
        return "Por favor valide el numero o el indicativo"

valido = validar_telefono("+573702281125")
print(valido)