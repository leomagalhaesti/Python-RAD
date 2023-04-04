from tkinter import *
from tkinter import ttk 
from tkinter import messagebox 

def inserir():
    if vid.get()=="" or vnomeproduto.get()=="" or vdescricao.get()=="" or vregistro.get()=="" or vquantiloja.get()=="" or vquantiestoque.get()=="" or vfone.et()=="":
       messagebox.showinfo(title="ERRO", message="Digite todos os dados")
       return
    tv.insert("","end",values=(vid.get(),vnomeproduto.get(),vdescricao.get(),vregistro.get(),vquantiloja.get(),vquantiestoque.get(),vfone.get()))
    vid.delete(0,END)
    vnomeproduto.delete(0,END)
    vdescricao.delete(0,END)
    vregistro.delete(0,END)
    vquantiloja.delete(0,END)
    vquantiestoque.delete(0,END)
    vfone.delete(0,END)
    vid.focus()


def deletar():
    print()

def modificar():
    print()



app=Tk()
app.title("Loja Eletroeletrônica")
app.geometry("600x900")



lbid=Label(app,text="ID")#,anchor=W)
vid=Entry(app)

lbnomeproduto=Label(app,text="Produto")#,anchor=W)
vnomeproduto=Entry(app)

lbdescricao=Label(app,text="Descrição")#,anchor=W)
vdescricao=Entry(app)

lbregistro=Label(app,text="N Registro")#,anchor=W)
vregistro=Entry(app)

lbquantiloja=Label(app,text="Qntd Loja")#,anchor=W)
vquantiloja=Entry(app)

lbquantiestoque=Label(app,text="Qntd Estoque")#,anchor=W)
vquantiestoque=Entry(app)

lbfone=Label(app,text="Telefone")#,anchor=W)
vfone=Entry(app)


tv=ttk.Treeview(app,columns=('id','nomeproduto','descricao','registro','quantiloja','quantiestoque','fone'), show='headings')

tv.column('id',minwidth=0,width=140)
tv.column('nomeproduto',minwidth=0,width=140)
tv.column('descricao',minwidth=0,width=140)
tv.column('registro',minwidth=0,width=140)
tv.column('quantiloja',minwidth=0,width=140)
tv.column('quantiestoque',minwidth=0,width=140)
tv.column('fone',minwidth=0,width=140)

tv.heading('id',text='ID')
tv.heading('nomeproduto',text='Produto')
tv.heading('descricao',text='Descrição')
tv.heading('registro',text='N Registro')
tv.heading('quantiloja',text='Qntd Loja')
tv.heading('quantiestoque',text='Qntd Estoque')
tv.heading('fone',text='Telefone')


btn_inserir=Button(app,text="Inserir",command=inserir)
btn_deletar=Button(app,text="Deletar",command=deletar)
btn_modificar=Button(app,text="Modificar",command=modificar)



lbid.grid(column=0,row=0,sticky="w")
vid.grid(column=0,row=1,sticky="w")


lbnomeproduto.grid(column=1,row=0)
vnomeproduto.grid(column=1,row=1)


lbdescricao.grid(column=2,row=0)
vdescricao.grid(column=2,row=1)


lbregistro.grid(column=3,row=0)
vregistro.grid(column=3,row=1)


lbquantiloja.grid(column=4,row=0)
vquantiloja.grid(column=4,row=1)

lbquantiestoque.grid(column=5,row=0)
vquantiestoque.grid(column=5,row=1)

lbfone.grid(column=6,row=0)
vfone.grid(column=6,row=1)


btn_inserir.grid(column=2,row=8)
btn_deletar.grid(column=3,row=8)
btn_modificar.grid(column=4,row=8)


tv.grid(column=0,row=7,columnspan=7)


app.mainloop()
