$(document).ready(function(){

    var categoria = $("#categorias_ticket")

    if(categoria.val()){

        sistema_id = $(".sistema_ticket").attr('id');
        unidade_id = $(".unidade_ticket").attr('id');

        $.get('/tickets/json/categorias?sistema='+sistema_id, function (data) {
            data = JSON.parse(data);
            for (var i = 0; i < data.length; i++) {
                $("#categorias_ticket").append(`<option value="`+data[i].pk+`">`+data[i].fields.nome+`</option>`)
            }
        });

        $("#categorias_ticket").change(function(){
            $.get('/tickets/json/subcategorias?categoria='+this.value, function (data) {
                data = JSON.parse(data);
                $("#subcategorias_ticket").append("<option>Selecione uma categoria</option>");
                for (var i = 0; i < data.length; i++) {
                    $("#subcategorias_ticket").append(`<option value="`+data[i].pk+`">`+data[i].fields.nome+`</option>`)
                }
            });
        });

        $("#subcategorias_ticket").change(function(){
            $.get('/tickets/json/classificacoes?subcategoria='+this.value, function (data) {
                data = JSON.parse(data);
                $("#classificacoes_ticket").append("<option>Selecione uma categoria</option>");
                for (var i = 0; i < data.length; i++) {
                    $("#classificacoes_ticket").append(`<option value="`+data[i].pk+`">`+data[i].fields.nome+`</option>`)
                }
            });
        });

        $("#classificacoes_ticket").change(function(){
            $.get('/tickets/json/operacoes?classificacao='+this.value, function (data) {
                $("#operacoes_ticket").append("<option>Selecione uma categoria</option>");
                data = JSON.parse(data);
                for (var i = 0; i < data.length; i++) {
                    $("#operacoes_ticket").append(`<option value="`+data[i].pk+`">`+data[i].fields.nome+`</option>`)
                }
            });
        });

        $.get('/tickets/json/estados?unidade='+unidade_id, function (data) {
            data = JSON.parse(data);
            $("#estados_ticket_new").append("<option>Selecione uma categoria</option>");
            for (var i = 0; i < data.length; i++) {
                $("#estados_ticket_new").append(`<option value="`+data[i].pk+`">`+data[i].fields.nome+`</option>`)
            }
        });
	}

    $('input, select, textarea').on('blur', function() {
        if ($(".ticket-form").valid() == true) {
            $('.bt-registrar').prop('disabled', false);  
        } else {
            $('.bt-registrar').prop('disabled', true);
        }
    });

    $(".ticket-form").validate({
        messages: {
            categorias_ticket: "Campo obrigatório",
            subcategorias_ticket: "Campo obrigatório",
            classificacoes_ticket: "Campo obrigatório",
            operacoes_ticket: "Campo obrigatório",
            estados_ticket_new: "Campo obrigatório",
            assunto_ticket: "Campo obrigatório",
            descricao_ticket: "Campo obrigatório",
        }
    });
});