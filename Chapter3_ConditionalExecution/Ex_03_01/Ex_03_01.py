sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
fh = float(sh)
fr = float(sr)
#print(fh, fr)
if fh > 40:
  #print('Overtime')
  regular = fh * fr
  otp = (fh - 40) * (fr * 0.5)
  #print(regular, otp)
  xp = regular + otp
else :
  #print('Regular')
  xp = fh * fr
print('Pay:',xp)