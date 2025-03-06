from flask import Blueprint, render_template
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)
 
@cliente_route.route('/')  
def lista_clientes():
    """ lista de clientes """
    return render_template('lista_clientes.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])  
def inserir_cliente():
    """ novo cliente """
    return {'pagina': "formulario clientes"} 


@cliente_route.route('/new')  
def form_cliente():
    """ formulario para novo cliente """
    return render_template('form_cliente.html')
 

@cliente_route.route('/<int:clinte_id>')  
def detalhe_cliente(cliente_id):
    """ exbir detalhe cliente """
    return render_template('detalhe_cliente.html')
 

@cliente_route.route('/<int:clinte_id>/edit')  
def edit_cliente(cliente_id):
    """ exbir detalhe cliente """
    return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:clinte_id>/update', methods=['PUT'])  
def atualizar_cliente(cliente_id):
    """ atualizar info cliente """
    pass

@cliente_route.route('/<int:clinte_id>/delete', methods=['DELETE'])  
def deletar_cliente(cliente_id):
    """ delete info cliente """
    pass
 
