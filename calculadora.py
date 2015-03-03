#!/usr/bin/python


class suma():

    def parse(self, request, rest):
        try:
            primero = int(rest.split("/")[1])
            segundo = int(rest.split("/")[2])
        except ValueError:
            return "Fallo"
        return (primero, segundo)

    def process(self, parsedRequest):
        if parsedRequest:
            resultado = int(parsedRequest[0]) + int(parsedRequest[1])
            return ("200 OK", "<html><body><h1>" +
                    str(resultado) + "</h1></body></html>")
        else:
            return ("400 Error", "<html>" +
                    "<body><h1>Mal uso de la funcion suma</h1>" +
                    "</body></html>")

class resta():

    def parse(self, request, rest):
        try:
            primero = int(rest.split("/")[1])
            segundo = int(rest.split("/")[2])
        except ValueError:
            return "Fallo"
        return (primero, segundo)

    def process(self, parsedRequest):
        if parsedRequest:
            resultado = int(parsedRequest[0]) - int(parsedRequest[1])
            return ("200 OK", "<html><body><h1>" +
                    str(resultado) + "</h1></body></html>")
        else:
            return ("400 Error", "<html>" +
                    "<body><h1>Mal uso de la funcion suma</h1>" +
                    "</body></html>")

class mult():

    def parse(self, request, rest):
        try:
            primero = int(rest.split("/")[1])
            segundo = int(rest.split("/")[2])
        except ValueError:
            return "Fallo"
        return (primero, segundo)

    def process(self, parsedRequest):
        if parsedRequest:
            resultado = int(parsedRequest[0]) * int(parsedRequest[1])
            return ("200 OK", "<html><body><h1>" +
                    str(resultado) + "</h1></body></html>")
        else:
            return ("400 Error", "<html>" +
                    "<body><h1>Mal uso de la funcion suma</h1>" +
                    "</body></html>")

class div():

    def parse(self, request, rest):
        try:
            primero = int(rest.split("/")[1])
            segundo = int(rest.split("/")[2])
        except ValueError:
            return "Fallo"
        return (primero, segundo)

    def process(self, parsedRequest):
        if parsedRequest:
            resultado = int(parsedRequest[0]) / int(parsedRequest[1])
            return ("200 OK", "<html><body><h1>" +
                    str(resultado) + "</h1></body></html>")
        else:
            return ("400 Error", "<html>" +
                    "<body><h1>Mal uso de la funcion suma</h1>" +
                    "</body></html>")
