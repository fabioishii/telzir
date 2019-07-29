import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout


#biblioteca de ddds e valores
ddd11={"16":1.9,"17":1.7,"18":0.9}
ddd16={"11":2.9,"17":'-',"18":'-'}
ddd17={"11":2.7,"16":'-',"18":'-'}
ddd18={"11":1.9,"16":'-',"17":'-'}
ddds={"11":ddd11,"16":ddd16,"17":ddd17,"18":ddd18}


#cria devolve um objeto com origem destino tempo plano e valores
def calcular(ori,dest,tempo,fale_mais):
    origem=str(ori)
    destino=str(dest)
    #verifica se existe origem-destino
    if destino not in ddds[origem]:
        valor='-'
        valores={"Origem":origem,"destino":destino,"tempo":tempo,"plano":fale_mais,"com fale mais":'-',"sem fale mais":'-'}
    else:    
        valor=ddds[origem][destino]
        pagar_com=0.00
        if valor !='-':
            cont=tempo-fale_mais
            pagar_sem=valor*tempo
            
            if cont>0:
                pagar_com=valor*1.1*cont

            valores={"Origem":origem,"destino":destino,"tempo":tempo,"plano":fale_mais,"com fale mais":round(pagar_com,2),"sem fale mais":round(pagar_sem,2)}
        else:
            pagar_com=valor
            pagar_sem=valor
            valores={"Origem":origem,"destino":destino,"tempo":tempo,"plano":fale_mais,"com fale mais":pagar_com,"sem fale mais":pagar_sem}
        
    return valores

    
#cria interface
class MyGrid(Widget):
    #obtem valores da aplicação
    origem=ObjectProperty(None)
    destino=ObjectProperty(None)
    tempo=ObjectProperty(None)
    plano=ObjectProperty(None)
    #inicia variaveis de preços
    com_fa=""
    sem_fa=""

    #comando para calcular preços
    def btn(self):

        #inicia variaveis com os valores digitados
        ori=self.origem.text
        des=self.destino.text
        temp=self.tempo.text
        plan=self.plano.text
        #obtem do objeto gerado pela função calcular(L22) os preços com e sem fale mais
        a=calcular(ori,des,int(temp),int(plan))
        com_fa=a["com fale mais"]
        sem_fa=a["sem fale mais"]
        
        #atualiza preços na aplicação
        self.com.text=("com fale mais: "+str(com_fa))
        self.sem.text=("sem fale mais: "+str(sem_fa))

#gera aplicação
class MyApp(App):
    def build(self):
        return MyGrid()
#roda aplicação
if __name__ == "__main__":
    MyApp().run()
