# -*- encoding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

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
        texto = _("formato Incorrecto:")
        raise ValidationError(("{1} {0} ").format(imageUrl, texto, ))
    return True
