# ****** Zona de clases ******
#Se crea la clase

class Cliente:
    def __init__(self):                                                #el constructor no tiene retorno y debe ser publico
        #se crean los atributos de la clase
        self.nombre_cliente= ""
        self.apellido_cliente=""
        
    #crear metodos get y set por atributos
    def get_nombre(self):
        return self.nombre_cliente
    
    def get_apellido(self):
        return self.apellido_cliente
    
    def set_nombre(self, dato_nombre):          #puede tener retorno pero no deberia
        self.nombre_cliente=dato_nombre
        
    def set_apellido(self, dato_apellido):
        self.apellido_cliente=dato_apellido
        
        
        
    
    #Se crean los metodos normales de la clase
    def tomar_datos(self):
        self.nombre_cliente=input("digite el apellido del cliente: ")
        self.apellido_cliente=input("digite el apellido del cliente: ")
    
    def procesar_datos(self):
        aux=self.nombre_cliente + " " + self.apellido_cliente
    
    def mostrar_info_cliente(self):
        print(f"Nombre Cliente: {self.nombre_cliente} - Apellido  cliente: {self.apellido_cliente}")