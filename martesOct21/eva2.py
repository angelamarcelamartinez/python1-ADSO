print("Calcule su indice de masa")
peso=77
alt=1.80
gen="hombre"
imc= peso/alt**2

if gen == "mujer":
    if imc<20:
       print("bajo peso")
    elif imc>=20 and imc<=23.9:
       print("peso normal")
    elif imc>=24 and imc<=28.9:
       print("Obevisad leve")
    elif imc>=29 and imc<=37:
       print("obesidad severa")
    else:
       print("obesidad muy severa")
else:
    if gen=="hombre":
      if imc<20:
          print("bajo peso")
      elif imc>=20 and imc<=24.9:
        print("peso normal")
      elif imc>=25 and imc<=29.9:
        print("Obevisad leve")
      elif imc>=30 and imc<=40:
        print("obesidad severa")
      else:
        print("obesidad muy severa")
    else:
      print("opcion invalida")
