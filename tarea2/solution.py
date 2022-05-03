class Solution():
    # ============Pregunta 1 (3pts)============
    def leer_directorio(self, directorio):
        nombres = []
        apellidos = []
        edades = []
        telefonos = []
        
        # Codigo para Pregunta 1 comienza aqui
        

        # Codigo para Pregunta 1 acaba aqui

        self.nombres = nombres
        self.apellidos = apellidos
        self.edades = edades
        self.telefonos = telefonos
        return nombres, apellidos, edades, telefonos

    
# ============Pregunta 2 (2pts)============
    def consulta_edades(self, edad_minima):
        nombres = self.nombres
        apellidos = self.apellidos
        edades = self.edades
        telefonos = self.telefonos

        cantidad = 0
        # Codigo para Pregunta 2 comienza aqui
        

        # Codigo para Pregunta 2 acaba aqui
        return cantidad

    
    # ============Pregunta 3 (3pts)============
    # 4 puntos
    def consulta_letra_nombre(self, primera_letra):
        nombres = self.nombres
        apellidos = self.apellidos
        edades = self.edades
        telefonos = self.telefonos

        edades_letra = []
        # Codigo para Pregunta 3 comienza aqui
        

        # Codigo para Pregunta 3 acaba aqui
        return edades_letra

    
    # ============Pregunta 4 (5pts)============
    # 4 puntos
    def consulta_numero_telefonico(self):
        nombres = self.nombres
        apellidos = self.apellidos
        edades = self.edades
        telefonos = self.telefonos

        contactos = []
        # Codigo para Pregunta 4 comienza aqui
        

        # Codigo para Pregunta 4 acaba aqui
        return contactos

  
    # ============Pregunta 5 (7pts)============
    # 6 puntos
    def consulta_letra_apellido(self, letra):
        nombres = self.nombres
        apellidos = self.apellidos
        edades = self.edades
        telefonos = self.telefonos

        contactos = []
        # Codigo para Pregunta 5 comienza aqui
        

        # Codigo para Pregunta 5 acaba aqui
        return contactos


# NO MODIFICAR NADA BAJO ESTA LINEA
if __name__ == '__main__':
  s = Solution()
  text = 'Mauricio Roizman 21 999999099 Mariana Gomez 19 998878112 Christian Ferrero 22 902991783 Manuela Sanchez 60 991725440 Daniel Gonzales 42 912006826'
  print("-------- Pregunta 1 --------")
  nombres, apellidos, edades, telefonos = s.leer_directorio(text)  # <- aqui puede verificar que su lectura sea correcta.
  print(f'Nombres:\n {nombres}')
  print(f'Apellidos:\n {apellidos}')
  print(f'Edades:\n {edades}')
  print(f'Telefonos:\n {telefonos}')

  print("\n\n-------- Pregunta 2 --------")
  print(s.consulta_edades(20))

  print("\n\n-------- Pregunta 3 --------")
  print(s.consulta_letra_nombre('M'))

  print("\n\n-------- Pregunta 4 --------")
  print(s.consulta_numero_telefonico())

  print("\n\n-------- Pregunta 5 --------")
  print(s.consulta_letra_apellido('r'))
# NO MODIFICAR NADA SOBRE ESTA LINEA
