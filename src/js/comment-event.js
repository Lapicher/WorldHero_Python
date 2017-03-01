var $=require('jquery');
var moment=require('moment');
//var apiClient=require('api-client');

$('.escribir > form').on("submit",function(){
    var self=this;

    //terminada la validacion de los campos se prosigue a enviar el comentario.
    var id=$(".plantilla-detalle").data("id");
    var user=$("#nombre").val();
    //var email=$("#email").val();
    var mensaje= $("#message").val();

    var datos={
        idArticle: id,
        userArticle: user,
        //emailUser: email,
        //fecha: new Date(),
        message: mensaje
    };
    // se guarda el comentario en el spaREST.
    /*
    apiClient.save(datos,function(){
        console.log("se inserto correctamente");
        alert("comentario agregado correctamente");
        self.reset();
    },
    function(err){
        console.error(e);
        alert("ocurrio un error, volver a intentar");
        self.reset();
    });
    */
    $.ajax({
        url: "/python/api/comments/",
        method: "post",
        data: datos,
        success: function(){
            ///console.log("se inserto correctamente");

            alert("comentario agregado correctamente");
            var fecha=moment(new Date(),"DD-MM-YYYY h:mm:ss a").format('LLL');
            var item = '<div class="item-comment row">'+
                 '<div class="row user-comment">'+
                     '<label id="fecha_comment">'+fecha+'</label>'+
                     '<label>'+datos.userArticle+'</label>'+
                  '</div>'+
                  '<div class="coment">'+
                      '<p>'+datos.message+'</p>'+
                  '</div>'+
                '</div>';
            $('.sectionComments').prepend(item);
            self.reset();
        },
        error: function(e){
            console.error(e);
            alert("ocurrio un error, volver a intentar");
            self.reset();
        }
    });
    return false;
});
// evento keyup para evitar que escriba mas de 150 palabras.
if ($('#message').length > 0) {
    var mensaje=document.getElementById('message');
    mensaje.setAttribute("onpaste","return false;");
    mensaje.palabras=150;
    mensaje.addEventListener("keyup",function(evt){

          var arrPalabras=$(this).val().toString().split(' ');
          var totalPalabras=0;
          for(var i in arrPalabras){
              if(arrPalabras[i].length!=0 && arrPalabras[i]!="\n"){
                  var enters=arrPalabras[i].split("\n");
                  for(var j in enters){
                      if(enters[j].length!=0)
                          totalPalabras++;
                  }
              }
          }
          if(totalPalabras>this.palabras && evt.keyCode!=8){
              var texto=$(this).val().toString();
              $(this).val(texto.substring(0,texto.length-1));
          }
          else{
              if(totalPalabras<=this.palabras){
                  $('.indicador').css("color","red");
                  $('.indicador').text(totalPalabras);
              }
          }
    });
}


$(window).on("scroll",function(){
      var scroll = $(window).scrollTop();
      var plantillaVisible=$(".plantilla-detalle").css("display");

      var porcentScroll=((scroll + $(window).height())*100)/$(document).height();
      //console.log(porcentScroll);
      if( porcentScroll > 70 && $(document).data("loadedComments") != "true" && plantillaVisible == 'block'){
           $(document).data("loadedComments","true");
           console.log("Async traera los comentarios");
            /*
            apiClient.list(function(comments){
                console.log(comments);
            },
            function(err){
                console.error(err);
            });
            */
            var idpost= $(".plantilla-detalle").data("id");
            console.log(idpost);
            $.ajax({
                url: "/python/api/comments/?_order=fecha",
                method: "get",
                data: {'idpost':idpost},
                success: function(respuesta){
                    //console.log(respuesta);
                    for(var item in respuesta.results){
                        //console.log(respuesta.results[item]);
                        var fecha=moment(respuesta.results[item].created_at,"DD-MM-YYYY h:mm:ss a").format('LLL');
                        var item = '<div class="item-comment row">'+
                             '<div class="row user-comment">'+
                                 '<label id="fecha_comment">'+fecha+'</label>'+
                                 '<label>'+respuesta.results[item].owner+'</label>'+
                              '</div>'+
                              '<div class="coment">'+
                                  '<p>'+respuesta.results[item].text+'</p>'+
                              '</div>'+
                            '</div>';
                        $('.sectionComments').append(item);
                    }
                },
                error: function(err){
                    console.error(err);
                }
            });
       }
});
