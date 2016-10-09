var $=require('jquery');
var moment=require('moment');
moment.locale('es');

// recorremos todos los articulos para activarles el icono de favorito en caso
// de haber sido marcados.

$(".article").each(function() {
    var id=localStorage.getItem($(this).data().id.toString());
    var user=$(this).find('.section-user').data('user');

    var iconFavorito=$(this).find(".icon-heart");
    // colocar a cada articulo si marca de favorito almacenada en el navegador.
    if(id!=null){
        iconFavorito.addClass("favup");
    }
    else {
        iconFavorito.removeClass("favup");
    }


     //colocar fecha de creacion del articulo en formato moment 2 years ago.
    var creado=$(this).data().fecha.toString();
    var fecha=moment(creado,"MMMM Do, YYYY, h:mm:ss a").format();
    var fechaFomart=moment(fecha).fromNow();
    $(this).find(".fecha > span").text(fechaFomart);
    //console.log(moment(fecha).format('LLL'));

    //cargar foto de perfil
    var url_image="./articles/"+user+"/img-profile/profile.jpg";
    $(this).find('.picture-profile >img').attr("src", url_image);

});

