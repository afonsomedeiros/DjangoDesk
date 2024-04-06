function show_modal_ramal(unidade){
	$.get("/unidades/ramais/json/"+unidade, function(data){
		data = JSON.parse(data);

		var html = `<tr><th scope="col">Setor</th>
			<th scope="col">contato</th>
			<th scope="col">Número Ramal</th></tr>`;

		for (var i = 0; i < data.length; i++) {
		    html += `<tr><td>`+ data[i]['fields']['setor']+`</td>`
		    html += `<td>`+ data[i]['fields']['contato']+`</td>`
		    html += `<td>`+ data[i]['fields']['numero']+`</td></tr>`
		}
        html += `</table>`
        $("#lista_ramais").html(html);

	});
}

function show_modal_ticket(ticket){
	$.get("/tickets/json/"+ticket, function(data){
		//data = JSON.parse(data);
		$("#ticket_id").html(data['id']);
		$("#nome_usuario").html(data['user_name']);
		$("#empresa_nome").html(data['empresa_nome']);
		$("#empresa_cnpj").html(data['empresa_cnpj']);
		$("#nome_contato").html(data['contato']);
		$("#telefone_contato").html(data['telefone']);
		$("#unidade_nome").html(data['unidade_nome']);
		$("#categoria").html(data['categoria']);
		$("#subcategoria").html(data['subcategoria']);
		$("#classificacao").html(data['classificacao']);
		$("#operacao").html(data['operacao']);
		$("#estado").html(data['estado']);

		var html = ``;

		for (var i = 0; i < data['interacoes'].length; i++) {
			html += `<div class="row row-iteracoes"><div class="col-2"><label>`+ data['interacoes'][i]['data'] +`
</div><div class="col-10"><p>`+ data['interacoes'][i]['descricao'] +`</p></div></div>`;
		}
		$(".interacoes").html(html);

		$.get('/tickets/json/estados?unidade='+data['unidade_id'], function (data) {
            data = JSON.parse(data);
            $("#estados_ticket").append("<option value='0'>Selecione uma categoria</option>");
            for (var i = 0; i < data.length; i++) {
                $("#estados_ticket").append(`<option value="`+data[i].pk+`">`+data[i].fields.nome+`</option>`)
            }
        });

		$("#form-nova-interacao").attr("action", "/tickets/nova/interacao/"+data['id']);
		$("#form-nova-interacao").attr("method", "POST");
	})
}