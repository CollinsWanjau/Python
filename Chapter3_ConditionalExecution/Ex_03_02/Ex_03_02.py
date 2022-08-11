sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
try:
  fh = float(sh)
  fr = float(sr)
except:
  print('Error, please enter numeric input')

quit()
#print(fh, fr)
if fh > 40:
  regular = fh * fr
  otp = (fh - 40) * (fr * 0.5)
  xp = regular + otp
else :
  xp = fh * fr
print('Pay:',xp)