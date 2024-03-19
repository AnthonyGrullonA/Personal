def obtener_empresa_del_usuario(usuario):
    """
    Obtiene la empresa asociada al usuario dado.

    Parámetros:
    - usuario: instancia del modelo CustomUser

    Retorna:
    - Instancia del modelo Cliente asociada al usuario, o None si el usuario no tiene una empresa asociada.
    """
    return usuario.empresa
