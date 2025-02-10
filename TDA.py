class Doctor:
    # decidi no meter mas tda dentro de este objeto para no hacerlo mas complicado(numero de licencia)
    # tambien procure no mencionar atributos que pudieran pertenecer facilmente a otras clases, ejemplo:
    #  persona:  nombre,edad
    #
    #
    def __init__(self, especialidad,experiencia,hospital,pacientes,horario_consulta):
        # Atributos del TDA
        self._especialidad = especialidad
        self._experiencia = experiencia
        self._hospital = hospital
        self._pacientes = pacientes
        self._horario_consulta =  horario_consulta

    # getters

    def obtener_especialidad(self):
        """Devuelve la especialidad del doctor"""
        return self._especialidad

    def obtener_numero_licencia(self):
        """Devuelve el número de licencia del doctor"""
        return self._numero_licencia

    def obtener_experiencia(self):
        """Devuelve los años de experiencia del doctor"""
        return self._experiencia

    def obtener_hospital(self):
        """Devuelve el nombre del hospital donde trabaja el doctor"""
        return self._hospital

    def obtener_pacientes(self):
        """Devuelve el numero de pacientes del doctor del doctor"""
        return self._pacientes

    def horario_consulta(self):
        """Devuelve el horario de consulta del doctor"""
        return self._horario_consulta


    # Metodos
    def presentar_doctor(self):
        """Devuelve una representación en forma de cadena con la información del doctor"""
        return f"Doctor: {self._nombre}, Especialidad: {self._especialidad}, Licencia: {self._numero_licencia}"

