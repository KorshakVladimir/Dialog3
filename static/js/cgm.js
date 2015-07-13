// Fixed Sidebar
$(window).bind("load", function () {
    
    var element=document.getElementById('GamePlayForm');

    if (!element) {
        
        // $("body").toggleClass("mini-navbar");
        
    }

    $("body").on("click",".dialog_btn",function(e){
    	var target = e.target;
    	var tar_href = target.getAttribute("href");
    	// $("#place-botton").load("/tree/load_button/",{"href":tar_href});
    	// $("#place-botton").load("/tree/load_button/");
    	// var posting = $.post("/tree/load_button/",{"2":3});

    // 	$.get( "/tree/load_button/", { name: "John", time: "2pm" } )
		  // .done(function( data ) {
		  //   alert( "Data Loaded: " + data );
		  // });

    	
		// --------------------------------------------------------------------------------------
		
      	$.post( "/tree/load_button/",{"href":tar_href} )
		  .done(function( data ) {
		  	$data = $(data);
		  	$("#for_ajax").html(data);
		  	
		  	var w = $("#for_ajax").find("#form_buttons");
		  	$("#form_buttons").html(w);	

		  	var popover_content = $("#for_ajax").find(".popover-content>p");
		  	$(".popover-content").html(popover_content);

		  	var points = $("#for_ajax").find("#points");	
		  	$("#left-progres-bar").html(points);

		  	var emotions = $("#for_ajax").find("#emotions");	
		  	$("#right-progres-bar").html(emotions);

		    $("#for_ajax").html("");
		  });
		if (tar_href.indexOf("/0/")!=-1){
			return true
		}	  
    	return false;
    });

})

// function f_test () {
// 	console.log('good');
// 	// document.querySelect
// 	doc_el = document.documentElement;
// 	el_backg =   doc_el.querySelector('.backg');
// 	if (!el_backg) {
// 		return;
// 	}
// 	var height_document = doc_el.clientHeight;
// 	var height_user_place = el_backg.clientHeight;
// 	if (height_document < height_user_place){
// 		el_backg.style.top ="40px";
// 		}
// 		else{
// 			el_backg.style.top = (height_document - height_user_place)/2 +"px";
// 		}
	
// }


// document.documentElement.addEventListener('onload',f_test());

// document.onload = f_test()