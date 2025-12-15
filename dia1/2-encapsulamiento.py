class Usuario:
    __usuario_email = 'admin@gmail.com'
    __usuario_password = '123'
    
    def __init__(self):
        pass
    
    def login(self,email,password):
        if email == self.__usuario_email and password == self.__usuario_password:
            print("Longin Existoso")
        else:
            print("Longin Fallido")
    

print("Login Usuario")
email = input("Ingrese el email: ")
password = input("Ingrese el Password: ")

# Utilizamos el __ delante de la variable, para que no se pueda accedar a los datos de esa variable
print(Usuario.usuario_email)
print(Usuario.__usuario_email)

Usuario = Usuario()
Usuario.login(email,password)   
print(f"{email}, {password}")