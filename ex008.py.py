medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida *1000
print('A média de {}m corresponde a {}km, {}hm, {}dam, {}dm, {}cm e {}mm'.format(medida, km, hm, dam, dm, cm, mm))
###para adicionar um número flutuante sem casas decimais, coloque dentro das chaves :.0f, se quiser casas decimais, substitua o 0 pelo número de casas