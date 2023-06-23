class ObjetoEjemplo:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def metodo1(self,salto,rebota,color,):
        self.salto = salto
        self.rebota = rebota
        self.color = color

        # Define aquí lo que hace el método 1
        pass

    def metodo2(self,correr,caminar,trotar):
        self.correr = correr
        self.caminar = caminar
        self.trotar = trotar
        # Define aquí lo que hace el método 2
        pass

# Crear una instancia del objeto
objeto = ObjetoEjemplo("valor1", "valor2")

# Acceder a los atributos del objeto
print(objeto.atributo1)
print(objeto.atributo2)
print(objeto.salto)
print(objeto.rebota)
print(objeto.color)
print(objeto.correr)
print(objeto.caminar)
print(objeto.trotar)

# Llamar a los métodos del objeto
objeto.metodo1()
objeto.metodo2()
