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
		if (tar_href.indexOf("/0/")!=-1){
			return true
		}
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
			  
    	return false;
    });

	$("body").on("click",".ajax_body",function(e){
		var a_href;
		if (e.target.tagName != "A"){
			a_href = $(e.target).closest("a");
		}else{
			a_href = e.target;
		}
		var href = $(a_href).attr("href");
		$("#page-wrapper").load(href+ " #ajax-wrapper");
		return false;
	});

	var refresh_menu = function(tar){
		$("[role=presentation]").each(function(){
			$(this).removeClass("active");
		});
		$(tar).closest("li").addClass("active");

	};

	$("body").on("click",".ajax_child",function(e){
		
		var a_href;
		if (e.target.tagName != "A"){
			a_href = $(e.target).closest("a");
		}else{
			a_href = e.target;
		}
		var href = $(a_href).attr("href");
		var load_button = function(){
			$(".backg").load(href+ " .backg_child");
			if (href.indexOf("myprofile")!=-1){
			refrech_radar();
			};
			refresh_menu();
		};
		if (href.indexOf("prod")!=-1){
			$("#offer_prod").modal("hide");
			setTimeout(load_button,500);
			} else {
			load_button();
				};		
		return false;
	});

})

