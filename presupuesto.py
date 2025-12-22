import os

# Limpiar pantalla al iniciar
os.system('clear')

# --- CODIGO DE PRESUPUESTO --- #
print("=== GESTOR DE PRESUPUESTO ===\n")

ingreso_mensual = float(input("Pon lo que ganas al mes: "))
gastos_mensuales = float(input("Pon los gastos del mes: "))
ganancia_mensual = ingreso_mensual - gastos_mensuales

if ganancia_mensual < 0:
    resultado = "Perdida"
elif ganancia_mensual == 0:
    resultado = "Tablas"
else:
    resultado = "Ganancia"

gasto_extra = float(input("Pon el valor de un gasto extra: "))

if ganancia_mensual < gasto_extra or resultado == "Tablas":
    Permitible = "no esta autorizado"
else:
    Permitible = "si esta autorizado"

print("\nAqui esta tu ganancia o perdida mensual")
print("Monto sin gasto extra:", ganancia_mensual)
print("El gasto extra", Permitible)

gasto_total = ganancia_mensual - gasto_extra
print(f"\nEl monto total con gasto extra incluido es: {gasto_total}")
print("El resultado es:", resultado)

# ───── IMPUESTOS ─────
añadir_impuestos = input("\n¿Desea que le agreguemos impuestos? (si/no): ").lower()
resultado_actual = gasto_total # Guardamos el progreso aquí

if añadir_impuestos == 'si' or añadir_impuestos == 's':
    print("\nAplicando impuesto al resultado anterior...")
    valor_impuesto_1 = float(input("¿De cuanto es tu impuesto (%): "))
    valor_impuesto = valor_impuesto_1 / 100
    impuesto = (ganancia_mensual * valor_impuesto)
    resultado_actual = round(gasto_total - impuesto, 4)
    print(f"El resultado con impuesto es: {resultado_actual}")
else:
    print("Ok, no se aplican impuestos.")

# ───── AHORRO (Fuera de impuestos para que siempre pregunte) ─────
ahorro_pregunta = input("\n¿Quiere restar un ahorro? (s/n): ").lower()

if ahorro_pregunta == 'si' or ahorro_pregunta == 's':
    cantidad_ahorro = float(input("Pon lo que quieres ahorrar: "))
    total_final = resultado_actual - cantidad_ahorro
    print(f"\n✅ Tu total descontando tu ahorro es: {total_final}")
else:
    print(f"\nOk, tu total final queda en: {resultado_actual}")

print("\n--- Proceso finalizado ---")

