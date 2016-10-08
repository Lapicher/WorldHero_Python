var $=require('jquery');

//evento para boton de tipo sandwich-event
$('.icon-sandwich').on("click",eventoSandwich);

$('.icon-lupa').on("click", eventoLupa);

function eventoSandwich(){

    //alert("click en san");
    $('.icon-sandwich').toggleClass("active");
    $('.categorias, .header').toggleClass("phone-active");
    $('.txt-buscar').css("display","none");

    //console.log("click en sandwich-event");
    //$( ".icon-lupa").unbind( "click" );

    $('.icon-lupa').off();
    if(!$('.header').is(":visible")){
        console.log("no visible header");
        $('.icon-lupa').on("click",eventoLupa);
    }
}
function eventoLupa(){
    //alert("lskd");
    $('.icon-lupa').toggleClass("active");
    $('.header').toggleClass("phone-active");
    $('.access').toggleClass("phone-inactive");
    $('.txt-buscar').css("display","inline-block");


    $('.icon-sandwich').off();
    if(!$('.txt-buscar').is(":visible")){
        $( ".icon-sandwich").on( "click",eventoSandwich);
    }
}
