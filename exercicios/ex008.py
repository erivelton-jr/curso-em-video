m = float(input('Quantos metros você gostaria de converter?'))
cm = m*100
mm = m*1000
km = m/1000
mc = m * 10000
print(f'Metros: {m}m \n'
      f'Centimetros: {cm:.0f}cm \n'
      f'Milimetros: {mm:.0f}mm \n'
      f'Kilometros: {km:.0f}km'
      f'Micrometros: {mc}')
