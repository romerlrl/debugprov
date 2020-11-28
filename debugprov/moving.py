import os
import datetime
import shutil

def MyMove(ambiente=None):
    arvorefinal=os.environ['modulo']=modulo
    resumo=input("Por favor, resuma o relatório:")
    if not ambiente:
        ambiente=os.environ.get("modulo")
    pasta='.\\logs\\'
    if not os.path.isdir('logs'):
        os.makedirs(pasta)
    pasta=f'.\\logs\\{ambiente}\\'
    try:
        os.makedirs(pasta)
        with open(f'{pasta}\\readme.txt', 'w', encoding='utf-8') as _: pass
    except:
        pass
    agora = str(datetime.datetime.now())[2:18].replace(':', '_')
    pastah=pasta+agora+'\\'
    print(pastah)
    os.makedirs(pastah)
    mydir= '.noworkflow'
    ehGv=lambda nome:nome[:4].isdigit()
    gvs=list(filter(ehGv, os.listdir()))
    adress=lambda n: os.getcwd()+'\\'+n
    try:
        for item in gvs:
            novo=f'logs\\{dia}\\{item}'
            shutil.move(adress(item), adress(pastah))
            print(f'Transferido: {item}')
    except:
        pass
    
    if '.noworkflow' in os.listdir():
        shutil.move(adress('.noworkflow'), adress(pastah))
        print("Cópia feita")
    else:
        print("A pasta não existe")
    
    
    json=f'{ambiente}.json'
    if arvorefinal.endswith('r'):
        json=arvorefinal+'.json'
    
    shutil.move(adress(f'{arvorefinal}.gv.pdf'), adress(pastah))
    shutil.move(adress(f'{arvorefinal}.gv'), adress(pastah))
    shutil.move(adress(json), adress(pastah))
    if resumo:
        with open(f'{pasta}\\readme.txt', 'a', encoding='utf-8') as saida:
            saida.write(agora)
            saida.write('\n')
            saida.write(resumo)
            saida.write('\n')
            saida.write('\n')
            print("Resumo atualizado")

#MyMove('parado2', 'ProdCons')