class Doctor:
    def __init__(self, nombre, especialidad, numero_licencia):
        # Atributos del TDA
        self._nombre = nombre
        self._especialidad = especialidad
        self._numero_licencia = numero_licencia

    def obtener_nombre(self):
        """Devuelve el nombre del doctor"""
        return self._nombre

    def obtener_especialidad(self):
        """Devuelve la especialidad del doctor"""
        return self._especialidad

    def obtener_numero_licencia(self):
        """Devuelve el número de licencia del doctor"""
        return self._numero_licencia

    def presentar_doctor(self):
        """Devuelve una representación en forma de cadena con la información del doctor"""
        return f"Doctor: {self._nombre}, Especialidad: {self._especialidad}, Licencia: {self._numero_licencia}"
