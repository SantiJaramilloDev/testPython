def descuentos(cliente: dict):
  boleta = 0
  descuento = 0
  apto = False
  atraccion = "N/A"
  total_boleta = "N/A"

  if cliente["atraccion"] == "X-treme":
    boleta = 20000
    if cliente["edad"] > 18 and cliente["primer_ingreso"]:
      descuento = 5
      apto = True
  
  if cliente["atraccion"] == "CarrosChocones":
    boleta = 5000
    if cliente["edad"] >= 15 and cliente["edad"] <= 18 and cliente["primer_ingreso"]:
      descuento = 7
      apto = True

  if cliente["atraccion"] == "SillasVoladoras":
    boleta = 10000
    if cliente["edad"] >= 7 and cliente["edad"] < 15 and cliente["primer_ingreso"]:
      descuento = 5
      apto = True
  
  valorTotal = boleta - ((boleta * descuento) / 100)

  if apto:
    total_boleta = valorTotal
    atraccion = cliente["atraccion"]

  respuesta = dict(
    nombre= cliente["nombre"], 
    edad= cliente["edad"], 
    atraccion= atraccion, 
    primer_ingreso= cliente["primer_ingreso"],
    total_boleta= total_boleta,
    apto= apto
    )
 
  #retorno de datos ya validados
  return respuesta


#diccionario de prueba
cliente1 = {
  "id_cliente": 2,
  "nombre": "Johana Fernandez",
  "edad": 20,
  "atraccion": "X-treme",
  "apto": True,
  "primer_ingreso": False
}

#llamado a funcion con diccionario de prueba
print(descuentos(cliente1))