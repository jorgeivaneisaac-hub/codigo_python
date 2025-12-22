  #codigo de presupuesto
#========================#
ingreso_mensual=int(input("Pon lo que ganas al mes\n"))

gastos_mensuales=int(input("Pon los gastos del mes\n"))
ganancia_mensual=ingreso_mensual-gastos_mensuales
if ganancia_mensual<0:
    resultado="Perdida"
else:
    resultado="Ganancia"
    
if ganancia_mensual==0:
    resultado="Tablas"
    
gasto_extra=int(input("Pon el valor de un gasto extra"))
if ganancia_mensual<gasto_extra:
    Permitible="no esta autorizado"
else:
    Permitible="si esta autrizado"
    
print("A qui esta tu ganancia o perdida mensual\n")
print("Monto sin gasto extra:",ganancia_mensual)
print("\nEl gasto extra",Permitible)
gasto_total=ganancia_mensual-gasto_extra
print("\nEl monto total con gasto extra incluido es igual a:\n", gasto_total)

if resultado=="Tablas":
     print("\nEl resultado es",resultado)
else:
    print("\nEl resultado es una",resultado)
    