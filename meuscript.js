$( document ).ready(function() {
    
    $("conteudoInicial").removeClass("invisible");

    $("#link_listar_times").click(function(){

        $.ajax({
            url: 'http://localhost:5000/listar_times',
            method: 'GET',
            dataType: 'json',
            sucess: listar_times,
            error: function() {
                alert("errro ao ler dados, verifique o backend")
            }
        });
        function listar_times(times) {
            linhas = ""
            for (var i in times) {
                lin = "<tr>" +
            "<th>" + times[i].nome + "</th>"
            "<td>" + times[i].esporte + "</td>"
            "<td>" + times[i].numero_jogadores + "</td>"
            "</tr>";

            linhas = linhas + lin;
            }
            $("#corpoTabelaTimes").html(linhas);

            $("conteudoInicial").addClass("invisible")
            $("tabelaTimes").addClass("invisible")

            $("#tabelaTimes").removeClasss("invisible")
        }
});