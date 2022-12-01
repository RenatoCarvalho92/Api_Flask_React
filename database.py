import psycopg2
import psycopg2.extras
from psycopg2 import sql
from flask import Flask, request,jsonify
from flask_cors import CORS,cross_origin

hostname = 'localhost'
database = 'postgres'
nomeUsuario = 'postgres'
senha = 'admin'
portId = '5432'

teste1 =4
teste2='Ronaldo'
teste3='ronaldo@email'
teste4="1234"

variavel_nome_calendario = "Calendario_Todos"

app = Flask(__name__)
CORS(app)



@app.route('/teste')
def testando(): 
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = nomeUsuario,
            password = senha,
            port =portId)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute ('DROP TABLE IF EXISTS empressa')

    script_criar = '''CREATE TABLE IF NOT EXISTS empressa (
                    id int PRIMARY KEY,
                    nomeempressa varchar(360) NOT NULL,
                    emailempressa varchar(360) NOT NULL,
                    senha varchar(360) NOT NULL)'''

    script_inserir ='INSERT INTO empressa (id, nomeEmpressa, emailempressa, senha) VALUES (%s,%s,%s,%s)'
    script_valores = (teste1,teste2,teste3,"123456")

    cur.execute(script_criar)
    cur.execute(script_inserir,script_valores)


    # cur.execute('SELECT *  FROM EMPRESSA WHERE ID = 4')
    # for record in cur.fetchall():
    #     print(record['emailempressa'],record['senha'])
    
    cur.execute(f'SELECT *  FROM EMPRESSA WHERE ID = {teste1}') #Verificar email se existe no banco de dados
    x= cur.fetchone()
    if x == None: 
        print ("Vazio") #Voltar para pagina porque não encontrou algo ou algo está errado
    else:               #SENÃO , vai para verificar se a senha recebida está correta 
        if teste4 == x[3]: 
            print("Tudo Correto") #Vai para proxima pagina 
        else:
            print("Senha Errada") #Volta a pagina anterior// mensagaem para tentar novamente
        
        
    conn.commit()

    conn.close()
    return "Teste Completo"



@app.route('/')
def criarTabelaCalendario():

    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = nomeUsuario,
            password = senha,
            port =portId)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cur.execute (f'''DROP TABLE IF EXISTS {variavel_nome_calendario}''')
    script_tabela_calendario = f'''CREATE TABLE IF NOT EXISTS  {variavel_nome_calendario}
                    (dia_mes_ano VARCHAR(8) NOT NULL,
                     email_empressa VARCHAR NOT NULL,
                     nota_Dia VARCHAR NOT NULL)'''
                     
    # script_tabela_calendario_valores = "Teste"
    
    cur.execute(script_tabela_calendario)
    
    conn.commit()

    conn.close()
    
    return {},200


@app.route('/AdicionarDia',methods=["POST"])
def AddDia():
    json_data = request.get_json()
    
    dia_aser_adicionado = json_data['dia_aser_adicionado']
    email_da_empressa = json_data['email_da_empressa']
    nota_do_dia = json_data['nota_do_dia']
    
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = nomeUsuario,
            password = senha,
            port =portId)
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    script_adicionar_dia = "INSERT INTO Calendario_Todos (dia_mes_ano,email_empressa,nota_dia)  VALUES (%s,%s,%s)"
    script_adicionar_dia_value = (dia_aser_adicionado,email_da_empressa,nota_do_dia)

    cur.execute(script_adicionar_dia,script_adicionar_dia_value)
    
    conn.commit()
    conn.close()
    return {}, 200

@app.route('/DeletarDia',methods=["DELETE"])
def DeleteDia():
    json_data = request.get_json()
    
    dia_aser_deletado = json_data['dia_aser_adicionado']
    email_da_empressa = json_data['email_da_empressa']
    nota_do_dia = json_data['nota_do_dia']
    
    
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = nomeUsuario,
            password = senha,
            port =portId)   
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    script_deletar_dia = "DELETE from Calendario_Todos WHERE nota_dia = %s AND email_empressa = %s AND dia_mes_ano = %s"
    script_deletar_dia_value = (nota_do_dia,email_da_empressa,dia_aser_deletado,) 
    # A virgula no final não é um erro mas sim um forma de converter o json para string 
    
    cur.execute(script_deletar_dia,script_deletar_dia_value)
    conn.commit()
    conn.close()
    
    return{},200


@app.route('/TodosDia',methods=["GET"])
def AllDia():
    json_data = request.get_json()
    
    dia_ase_procurar = json_data['dia_aser_adicionado']
    email_da_empressa = json_data['email_da_empressa']
    
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = nomeUsuario,
            password = senha,
            port =portId)   
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    script_pegar_todo_dia = "SELECT * FROM Calendario_Todos WHERE dia_mes_ano = %s AND email_empressa = %s"
    script_pegar_todo_dia_valores = (dia_ase_procurar,email_da_empressa,)
    # A virgula no final não é um erro mas sim um forma de converter o json para string 
    
    cur.execute(script_pegar_todo_dia,script_pegar_todo_dia_valores)
    toda_informacao_dia_especifico=cur.fetchall()
    conn.commit()
    
    # books =[{'id':59595,'name':"JAJSJSJ"},{'id':59595,'name':"JAJSJSJ"},]
    
    lista_retornar_json = []
    for x in toda_informacao_dia_especifico:
        informacao_dia_retornadas={}
        informacao_dia_retornadas["Dia"]= x[0]
        informacao_dia_retornadas["Email"]= x[1]
        informacao_dia_retornadas["Nota"]= x[2]
        print(x)
        lista_retornar_json.append(informacao_dia_retornadas)
    conn.close()
    
    
    return jsonify(lista_retornar_json),200


@app.route('/todomes',methods=['POST'])
def allmes():
    json_data = request.get_json()    
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = nomeUsuario,
            password = senha,
            port =portId)   
    
    email_da_empressa = json_data['email_da_empressa']
   
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    script_pegar_todo_dia = "SELECT * FROM Calendario_Todos WHERE email_empressa = %s"
    script_pegar_todo_dia_valores = (email_da_empressa,)
    # A virgula no final não é um erro mas sim um forma de converter o json para string 
    
    cur.execute(script_pegar_todo_dia,script_pegar_todo_dia_valores)
    toda_informacao_email_especifico=cur.fetchall()
    conn.commit()
   
    lista_retornar_json = []
    for x in toda_informacao_email_especifico:
        toda_informacao_email_especifico={}
        toda_informacao_email_especifico["Dia"]= x[0]
        toda_informacao_email_especifico["Email"]= x[1]
        toda_informacao_email_especifico["Nota"]= x[2]
        # print(x)
        lista_retornar_json.append(toda_informacao_email_especifico)
    conn.close()
    
    # testejson ={"data":"Data"}
    # testejson["soparaver"] = lista_retornar_json   
    return jsonify(lista_retornar_json),200

app.run()