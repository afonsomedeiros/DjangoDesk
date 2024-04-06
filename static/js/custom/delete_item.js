$(document).ready(function(){
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');


    $(deleteBtn).on('click', function(e){
        e.preventDefault();

        var delLink = $(this).attr('href');
        var information = $(this).attr('rel');
        var result = confirm("Deseja excluir o item: "+information)
        if(result){
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function(){
        searchForm.submit();
    });
});