$( function(){

	var refresh_game = function(){
		$("#game_list").load("/game/refresh_game/ li")
	}

	var save_form_config  = function(href,data){
		$.ajax({
		    url: href,
		    type: "POST",
		    data: data,
		    cache: false,
		    processData: false,
		    contentType: false,
		    success: function(data) {
		        $data = $(data);
		    	$("#page-wrapper").html($data);

		    }
		});
	}

	$("body").on("click","#new_form", function(e){

		// $.post( "/game/add_game/",$("#foorm_add_game").serialize() )
		//   .done(function( data ) {
		//   		$data = $(data);
		//     	$("#page-wrapper").html($data);
		//   });

		e.preventDefault();
		var data = new FormData($('#foorm_add_game').get(0));
		
		save_form_config("/game/add_game/",data);
		setTimeout(refresh_game,1000);
		return false;
	});


	$("body").on("click","#save_config", function(e){
		var form = $("#foorm_save_game");
		e.preventDefault();
		var data = new FormData($('#foorm_save_game').get(0));

		save_form_config(form.attr("action"),data);
	
		setTimeout(refresh_game,1000);
		return false;
	});

	$("body").on("click","#cancel-buttom", function(){
		
		$("#page-wrapper").load("/ #ajax-wrapper");
		return false;
	});

	$("body").on("click",".button_del_game",function(e){
		var game_id = $(e.target).parent().attr("game_id");
		$.post("/game/del_game/",{"game_id":game_id})
		
		$("#"+game_id).remove();
		refresh_game();
	});

	$("body").on("click",".ajax_config_game",function(e){
		var href = _$.get_href_a(e);
		$("#page-wrapper").load(href+ " #ajax-wrapper");
		return false;
	});

});