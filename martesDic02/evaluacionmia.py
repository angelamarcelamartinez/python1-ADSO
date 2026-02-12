clientes={10901:{"nombre":"Catalina Forero",
                              "contrasena":"Qwe1rt#a",
                              "saldo":10000}
                              ,11123:{"nombre":"Miguel Triana",
                                      "contrasena":"A123bx$n",
                                      "saldo":20000}}
print("Bienvenido a la billetera virtual JONA")
print(f"\n 3 oportunidades para ingresar credenciales")
print("--------------------")
for i in range (3):
    cedula=int(input("Ingrese su cedula :_"))
    if cedula in clientes:
         for i in clientes:
            if cedula == i:
                print(f"Bienvenido {clientes[cedula]["nombre"]}")
                print("--------------------")
                for i in range (3):
                    contra=input("Ingrese su contrasena:_")
                    if contra==(clientes[cedula]["contrasena"]):
                        print("--------------------")
                        print("validacion exitosa")
                        print("-------MENU------")
                        print("1.Ver saldo")
                        print("2.Consignar")
                        print("3.Retirar")
                        print("4.Ver movimientos")
                        print("5.Salir")
                        print("--------------------")
                        opc=int(input("Escoja una opcion:_"))
                        print("--------------------")
                        retic=[]
                        montc=[]
                        while opc!= 5:
                            match opc:
                                case 1:
                                    print(f"Saldo actualizado:_{clientes[cedula]["saldo"]}")
                                    print("-------MENU------")
                                    print("1.Ver saldo")
                                    print("2.Consignar")
                                    print("3.Retirar")
                                    print("4.Ver movimientos")
                                    print("5.Salir")
                                    print("--------------------")
                                    opc=int(input("Escoja una opcion:_"))
                                    print("--------------------")
                                case 2:
                                    mont=int(input("Ingrese el monto a consignar:_"))
                                    print("--------------------")
                                    if mont >=5000:
                                        montoa=clientes[cedula]["saldo"]+ mont
                                        print(f"Su saldo actualizado es:_{montoa}")
                                        montc.append(mont,)
                                        print("-------MENU------")
                                        print("1.Ver saldo")
                                        print("2.Consignar")
                                        print("3.Retirar")
                                        print("4.Ver movimientos")
                                        print("5.Salir")
                                        print("--------------------")
                                        opc=int(input("Escoja una opcion:_"))
                                        print("--------------------")
                                    else:
                                        print("Error el monto es minimo de $5000")
                                        mont=int(input("Ingrese el monto a consignar:_"))
                                        print("--------------------")
                                        if mont >=5000:
                                            montoa=clientes[cedula]["saldo"]+ mont
                                            print(f"Su saldo actualizado es:_{montoa}")
                                            montc.append(mont,)
                                            print("-------MENU------")
                                            print("1.Ver saldo")
                                            print("2.Consignar")
                                            print("3.Retirar")
                                            print("4.Ver movimientos")
                                            print("5.Salir")
                                            print("--------------------")
                                            opc=int(input("Escoja una opcion:_"))
                                            print("--------------------")
                                    (clientes[cedula]["saldo"])=(montoa)
                                case 3:
                                    ret=int(input("Ingrese el monto a retirar:_"))
                                    print("--------------------")
                                    if ret >=5000:
                                        reta=clientes[cedula]["saldo"]-ret
                                        print(f"Su saldo actualizado es:_{reta}")
                                        retic.append(ret,)
                                        print("-------MENU------")
                                        print("1.Ver saldo")
                                        print("2.Consignar")
                                        print("3.Retirar")
                                        print("4.Ver movimientos")
                                        print("5.Salir")
                                        print("--------------------")
                                        opc=int(input("Escoja una opcion:_"))
                                        print("--------------------")
                                    else:
                                        print("Error el monto es minimo de $5000")
                                        print("--------------------")
                                        ret=int(input("Ingrese el monto a retirar:_"))
                                        if ret >=5000:
                                            reta=clientes[cedula]["saldo"]-ret
                                            print(f"Su saldo actualizado es:_{reta}")
                                            retic.append(ret,)
                                            print("-------MENU------")
                                            print("1.Ver saldo")
                                            print("2.Consignar")
                                            print("3.Retirar")
                                            print("4.Ver movimientos")
                                            print("5.Salir")
                                            print("--------------------")
                                            opc=int(input("Escoja una opcion:_"))
                                            print("--------------------")
                                    (clientes[cedula]["saldo"])=(reta)
                                case 4:
                                    print("Movimientos")
                                    print("Consignaciones de ", clientes[cedula]["nombre"],montc)
                                    print("Retiros de ", clientes[cedula]["nombre"],retic)
                                    print("-------MENU------")
                                    print("1.Ver saldo")
                                    print("2.Consignar")
                                    print("3.Retirar")
                                    print("4.Ver movimientos")
                                    print("5.Salir")
                                    print("--------------------")
                                    opc=int(input("Escoja una opcion:_"))
                                    print("--------------------")
                                    
                        print("Hasta pronto", clientes[cedula]["nombre"])
                        exit()
                    else:
                        print("no hay mas intentos")
    else:
        print("Cedula paila")