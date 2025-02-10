class Doctor:
    # decidi no meter mas tda dentro de este objeto para no hacerlo mas complicado(numero de licencia)
    # tambien procure no mencionar atributos que pudieran pertenecer facilmente a otras clases, ejemplo:
    #  persona:  nombre,edad
    #
    #
    def __init__(self, especialidad, experiencia, hospital, pacientes, horario_consulta, consultas_diarias):
        # Atributos del TDA

        self._especialidad = especialidad
        self._experiencia = experiencia
        self._hospital = hospital
        self._pacientes = pacientes
        self._horario_consulta = horario_consulta
        self._consultas_diarias = consultas_diarias
        self._total_consultas = 0
    ''' 
    def __str__(self):
        return (f"ID: {self.id}, Especialidad: {self.especialidad}, Hospital: {self.hospital}, experiencia: {self._experiencia}, "
                f"pacientes: {self._pacientes}, horario_consulta: {self._horario_consulta}, consultas_diarias: {self._consultas_diarias}, total_consultas: {self._total_consultas}")
    '''

    # getters

    def obtener_especialidad(self):
        """Devuelve la especialidad del doctor"""
        self._especialidad = self._especialidad
        return self._especialidad

    def obtener_experiencia(self):
        """Devuelve los años de experiencia del doctor"""
        self._experiencia = self._experiencia
        return self._experiencia

    def obtener_hospital(self):
        """Devuelve el nombre del hospital donde trabaja el doctor"""
        self._hospital = self._hospital
        return self._hospital

    def obtener_pacientes(self):
        """Devuelve el numero de pacientes del doctor del doctor"""
        self._pacientes = self._pacientes
        return self._pacientes

    def obtener_horario_consulta(self):
        """Devuelve el horario de consulta del doctor"""
        self._horario_consulta = self._horario_consulta
        return self._horario_consulta

    def obtener_consultas_diarias(self):
        self._consultas_diarias = self._consultas_diarias
        return self._consultas_diarias

    def obtener_total_consultas(self):
        self._total_consultas = self._total_consultas
        return self.total_consultas


    # Metodos
    def presentar_doctor(self):
        """Devuelve una representación en forma de cadena con la información del doctor"""
        return f"Doctor: {self._nombre}, Especialidad: {self._especialidad}, Licencia: {self._numero_licencia}"


    def diagnostico(self):
        "da un diagnostico"

    def operacion_quirurgica(self):
        "inicia operacion"

    def primeros_auxilios(self):
        "da los primeros auxilios"

    def preescribir_medicamento(self):
        "preescribe el medicamento"

    def realizar_consulta(self, duracion):
        """
        Realiza una consulta y actualiza el total de consultas y el tiempo promedio.

        :param duracion: Duración de la consulta en minutos
        :return: Tiempo promedio actualizado de consultas
        """
        self._total_consultas += 1

        # Calculamos el nuevo tiempo promedio de consultas
        tiempo_total = self._total_consultas * self._consultas_diarias * duracion
        tiempo_promedio = tiempo_total / (self._total_consultas * self._consultas_diarias)

        return tiempo_promedio

    def calcular_eficiencia(self):
        """
        Calcula la eficiencia del doctor basada en su experiencia y número de pacientes.

        :return: Puntuación de eficiencia (0-100)
        """
        factor_experiencia = min(self._experiencia / 10, 1)  # Máximo 1 para 10 años o más
        factor_pacientes = min(self._pacientes / 100, 1)  # Máximo 1 para 100 pacientes o más

        eficiencia = (factor_experiencia * 0.6 + factor_pacientes * 0.4) * 100
        return round(eficiencia, 2)

