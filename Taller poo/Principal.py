from Cliente import Cliente
from Saludo import Saludo 
# ******** Codigo principal *****


# Creando objetos
objCliente= Cliente()
objSaludo= Saludo()

#usp los metodos de los objetivos
objCliente.tomar_datos()
aux_mensaje=objSaludo.hacer_saludo_formal()
objCliente.hacer_saludo(aux_mensaje)