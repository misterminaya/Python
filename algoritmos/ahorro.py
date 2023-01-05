def validar(message):
    while True:
        try:
            data = float(input("Coloca " + message))
            return data
        except ValueError:
            print("El dato debe ser el precio de una moneda")


goal_save_money = validar("Ingresar cuando quieres ahorrar : ")
money_save_per_month = validar("Ingresar cuanto ahorras por cada mes : ")


result_save = goal_save_money - money_save_per_month
months_to_save = int(goal_save_money / money_save_per_month)


print("Te falta por ahorrar " , result_save)
print("Si sigues ahorrando : " , money_save_per_month , "lograras tu objetivo en : " , months_to_save  , "meses")
