precios = [8500, 32000, 15900, 7200, 54000, 12300]
impuesto = 0.19

total = 0

for precio in precios:
    precio_final = precio * (1 + impuesto)
    total += precio_final
    print(f"Precio base: ${precio} → Precio final: ${precio_final:,.2f}")

print(f"\nTotal general: ${total:,.2f}")



