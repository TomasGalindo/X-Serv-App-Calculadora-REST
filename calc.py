
import webapp
import csv


class calc (webapp.webApp):
    """Calculadora utilizando un solo recurso"""

    # Declare and initialize content
    op1 = 0
    op2 = 0
    operacion = ''

    def parse(self, request):
        """Return the resource name (including /)"""
        # devuelve nombre recurso (GET,..)
        # valor del recurso /calc
        # si es un PUT lo que haya en el body
        return (request.split(' ', 1)[0],
                request.split(' ', 2)[1],
                request.split('\r\n\r\n')[-1])

    def process(self, parsed):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """
        method, resourceName, body = parsed
        # favicon.ico
        if (resourceName == "favicon.ico"):
            httpCode = "404 Not Found"
            htmlBody = ("<html><body>Encontrado favicon</html>")
            recvSocket.close()

        if (method == "GET"):
            try:
                if (self.operacion == "+"):
                    Resultado = int(self.op1) + int(self.op2)
                elif (self.operacion == "-"):
                    Resultado = int(self.op1) - int(self.op2)
                elif (self.operacion == "*"):
                    Resultado = int(self.op1) * int(self.op2)
                elif (self.operacion == "/"):
                    Resultado = int(self.op1) / int(self.op2)
                else:
                    Resultado = "operacion desconocida"

                httpCode = "200 OK"
                htmlBody = ("<html><body>" + str(self.op1) +
                            str(self.operacion) + str(self.op2) + " = " +
                            str(Resultado) + "</html>")
            except(ZeroDivisionError):
                httpCode = "200 OK"
                htmlBody = ("<html><body>Division entre cero</html>")

        elif (method == "PUT"):
            self.op1, self.op2, self.operacion = body.split(',')
            print("op1 = " + self.op1)
            print("op2 = " + self.op2)

            print("operac = " + self.operacion)
            httpCode = "200 OK"
            htmlBody = ("<html><body>Quieres hacer la operacion: " +
                        str(self.op1) + str(self.operacion) +
                        str(self.op2) + "</html>")
        else:
            print("No se puede hacer otra operacion")
            httpCode = "405 Method Not Allowed"
            htmlBody = ("<html><body>No se puede utilizar esa operacion" +
                        "</html>")

        return (httpCode, htmlBody)

if __name__ == "__main__":
    testWebApp = calc("localhost", 1234)
