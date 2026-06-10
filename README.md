# CryptoMania
## Un sistema de encriptación de mensajes junto a su librería original

---

CryptoMania sirve para programadores que quieren encriptar sus mensajes de manera rapida y sencilla usando POO

CryptoMania posee como funciones principales encriptar en cifrados o sistemas de encriptación comúnmente conocidos como el cifrado cesar o el cifrado Hash

---

# Conceptos de POO Utilizados en CryptoMania

1. Encapsulamiento
Linea 10 de cryptomania.py
```python
        self.__message = message
```

2. Herencia
Se utiliza en general en la libreria de CryptoMania y en la GUI heredando esta de mainGUI.py

3. Abstracción
Linea 1 -> 18 de template.py
```python
from abc import ABC, abstractmethod


class CryptoTemplate(ABC):
    def __init__(self, message : str):
        self.__message = message
        if not isinstance(self.__message, str):
            raise TypeError("The Attributes must be its types!")
    
    @abstractmethod
    def encode(self):
        pass
    
    def return_encoded_message(self):
        return self.encode()
    
    def return_original_message(self):
        return self.__message
```

4. Polimorfismo
Se puede apreciar en el codigo anterior siendo una plantilla del resto de Metodos de encriptación

---
## Criterios de Aceptación

1. El sistema debe permitir al usuario ingresar un mensaje de texto y
   seleccionar un método de encriptación desde el menú de consola,
   retornando el mensaje encriptado correctamente.

2. La clase `CryptoTemplate` debe ser abstracta y no debe poder
   instanciarse directamente; solo sus clases hijas pueden ser usadas.

3. Cada método de encriptación (César, Hash, etc.) debe implementar
   obligatoriamente el método `encode()`, y cada implementación debe
   producir un resultado diferente para el mismo mensaje de entrada.

4. El atributo `__message` debe estar encapsulado y no debe ser
   accesible ni modificable directamente desde fuera de la clase;
   solo a través de los métodos públicos definidos.

5. Si el usuario ingresa un valor que no sea string como mensaje,
   el sistema debe lanzar un `TypeError` con un mensaje de error
   descriptivo, sin romper la ejecución del programa.

6. El menú de consola debe incluir como mínimo las opciones de
   encriptar un mensaje, mostrar el resultado y salir del sistema,
   funcionando de forma controlada sin errores inesperados.