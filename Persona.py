class Persona:
    def __init__(self, nombre, apellido, correo, telefono, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.cedula = cedula
    def Obtenernombre(self):
        return f"mi nombre es {self.nombre} {self.apellido} {self.correo} {self.telefono} {self.cedula}"