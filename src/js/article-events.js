var $=require('jquery');
var moment= require('moment');

$('.cerrar').on("click",function(){
    history.back();
});

//evento de click del articulo para rediccionar a la plantilla de detalle.
$('.article-click').on("click",function(){

    var id=$(this).parent().data().id;
    var userArticle=$(this).parent().children().data().user;

    window.location = userArticle+"/"+id;
    //mostrarArticulo(self,id,userArticle,0);
});


//evento de click para el boton de agregar a favoritos.
$('.icon-heart').on("click",function(){
    if (typeof(Storage) !== "undefined") {
        // Code for localStorage/sessionStorage.
          var id=$(this).parent().parent().data().id;
          var favorito=localStorage.getItem(id);
          console.log(favorito);
          if(favorito!="1"){
              localStorage.setItem(id,"1");
              $(this).addClass("favup");
          }
          else {
              localStorage.removeItem(id);
              $(this).removeClass("favup");
          }
    } else {
      // Sorry! No Web Storage support..
      console.log("Sorry! No Web Storage support..");
    }
});
// evento de click sobre el numero de comentarios.
$('.icon-bubbles').on("click",function(){
    var self=$(this).parent().parent().find('.article-click');
    var id=$(self).parent().data().id;
    var userArticle=$(self).parent().children().data().user;

    mostrarArticulo(self,id,userArticle, $(document).height());
    //console.log("scroll hasta abajo");
});
//evento cuando no carga imagen de perfil pone por defecto un placeholder.
$(".picture-profile >img").on("error",function(){
    $(this).attr("src","/../static/image/profile-placeholder.png");
});

// evento sobre el usuario para redirigirlo a su perfil.
$(".user-name").on("click", function(){
    window.location = this.innerHTML.trim();
});