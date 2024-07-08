def convert_seg(seg,min,hora):
    hora_convert = hora*3600
    min_convert = min*60
    total = (seg)+min_convert+hora_convert

    print(f"\nSegundos: {seg}\nMinutos em seg: {min_convert}\nHoras em seg: {hora_convert}\nTotal: {total}")

seg = int(input("Digite a quantidade de segundos: "))
min = int(input("Digite a quantidade de minutos: "))
hora = int(input("Digite a quantidade de horas: "))

convert_seg(seg, min, hora)