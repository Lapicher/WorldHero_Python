from django.core.exceptions import ValidationError

BADWORDS = (
            "Caranabo",
            "Carapan",
            "Chimpamonas",
            "Chupaescrotos",
            "Cuerpoescombro"
            )


def formatURLImage(imageUrl):
    """
    Valida que la url de la imagen contenga el string "http"

    Nota: Despues se puede evaluar mejor la cadena con Expresion Regular para url de imagenes.

    :return: diccionario con los datos limpios y validados
    """

    if "http" not in imageUrl:
        raise ValidationError("format incorrect: {0} ".format(imageUrl))
    return True
