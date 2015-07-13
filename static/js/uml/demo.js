jsPlumb.ready(function () {

    // -------------------------
    var main_block = jsPlumb.getSelector(".statemachine-demo .all");
    var windows = jsPlumb.getSelector(".statemachine-demo .end_point_relation");

    

    // setup some defaults for jsPlumb.
    var instance = jsPlumb.getInstance({
        Endpoint: ["Dot", {radius: 1}],
         
        HoverPaintStyle: {strokeStyle: "#1e8151", lineWidth: 2, zindex:1000000 },
        ConnectionOverlays: [
            [ "Arrow", {
                location: 1,
                id: "arrow",
                length: 14,
                foldback: 0.8
            } ],
            // [ "Label", { label: "FOO", id: "label", cssClass: "aLabel" }]
        ],
        Container: "statemachine-demo"
    });

    var basicType = {
        connector: "Flowchart",
        paintStyle: { strokeStyle: "red", lineWidth: 2 },
        hoverPaintStyle: { strokeStyle: "blue",lineWidth: 2  },
        overlays: [
            "Arrow"
        ]
    };

    instance.draggable(main_block); 

    $(function() {
    $( "#statemachine-demo" ).draggable({ scroll: true });
    });



    instance.registerConnectionType("basic", basicType);
    // instance.registerConnectionType("basic", basicType);
    var make_Target  = function(el){
        instance.makeTarget(el, {
            dropOptions: { hoverClass: "dragHover" },
            // anchor: "AutoDefault", 
            // allowLoopback: true
            anchor:["Continuous", { faces:[ "right", "left" ] } ],
        }); 
    };

    var make_Source = function(el){
        instance.makeSource(el, {
            filter: ".ep",
            anchor: "RightMiddle",
            // anchor:"Continuous",
            connector: [ "Flowchart" ],
            connectorStyle: { strokeStyle: "#5c96bc", lineWidth: 2, outlineColor: "transparent", outlineWidth: 4 },
        }); 
    }

    instance.init_ep = function () {
        
        make_Source(windows);
        
        make_Target(main_block); 

    }

    initialise = ( function (){
            instance.batch(instance.init_ep);
        });

    initialise();
    
    window.jsp = instance;

    


    // instance.bind("connection", function (info) {
    //     info.connection.getOverlay("label").setLabel(info.connection.id);
    // });


    var countid = 10; 

    jsPlumb.fire("jsPlumbDemoLoaded", instance);


    for_click_rem = function(e){
        e.target.parentElement.remove();
    }

    butt_remove = function(parentEl) {
       var ev_button = document.createElement('button');   
       ev_button.innerHTML = "<i class=\"fa fa-trash-o\"></i>";
       ev_button.cssClass = "but_rem";

       ev_button.addEventListener( "click",for_click_rem );

       parentEl.appendChild(ev_button);
    }

    var remove_all_adit = function(){
        var el_edit_del = jsPlumb.getSelector(".for_edit");
        $(el_edit_del).removeClass("active_form");
    }

    var canv =  jsPlumb.getSelector("html")[0];
    canv.addEventListener( "click",remove_all_adit );

    // ------------------------------------------------

    // click_for_edit = function  (e) {
    //     remove_all_adit();
    //     e.stopPropagation();
    //     var el_panel_demo = e.target.closest(".head_section");
    //     var el_edit = el_panel_demo.querySelector(".for_edit") ;
        
    //     $(el_edit).toggleClass("active_form");
    // }


    // $("body").on("click",".edit_quest",click_for_edit);

    // ------------------------------------------------

    click_for_edit_all = function  (e) {
        remove_all_adit();
        e.stopPropagation();
        var el_klient_section = e.target.closest(".klient_section");
        var el_edit = el_klient_section.querySelector(".for_edit") ;
        
        $(el_edit).toggleClass("active_form");
        $(el_edit).find("textarea").trigger("resize");
        // $(el_edit).find("textarea").trigger("autosize");

        // var el_all  = e.target.closest(".all");
        // var el_ask = $(el_all).find("collaps");
        // $(el_all).find(".for_edit>.media-body>small").html($(el_all).attr("id"));
        // $(el_all).find(".for_edit>.media-body>textarea").html($(el_ask).html());
        // $(el_ask).each(function(){
        //     var id = $(this).attr("id");
        //     var text_quest = $(this).find("textarea").html();
        // });

    }


    $("body").on("click",".edit_answer",click_for_edit_all);

    $("body").on("click",".for_edit",function(e){
            e.stopPropagation();
        }
    );

    butt_edit = function(parentEl) {
       var ev_button = document.createElement('button');   
       ev_button.innerHTML = "Edit";
       ev_button.cssClass = "but_edit";

       ev_button.addEventListener( "click",click_for_edit);

       parentEl.appendChild(ev_button);
    }

    add_place_edit = function(parentEl){
       var place_edit = document.createElement('div');   
       place_edit.className = "for_edit hide_el";
       parentEl.appendChild(place_edit);
    }
     

    for_click_add = function(e){

        var parrent_el = $(e.target).closest(".all").find(".section_question"); 
        var id = $(parrent_el).attr('id');
        var clean_id = id.substring(0,id.indexOf("pan"));
        var max_id = parseInt( clean_id+"00");
        $(parrent_el).find(".end_point_relation").each(function(){

            var  id =  $(this).attr("id");
            var pos_ind = id.indexOf("for_dot");
            var int_id = parseInt(id.substring(0,pos_ind));
            if (int_id > max_id){
                max_id = int_id;
            }

         });

        $.post( "/tree/new_quest/",{"max_id":max_id}).done(function( data ) {

            $(parrent_el).append($(data));
            make_collapsed( $(parrent_el).last());
            // rem_all_collaps();
            var el_panel_collapsed;
            var id_el;
            $(parrent_el).find(".head_collaps").each(function(){
                el_panel_collapsed = $(this).find(".collaps");
                id_el = $(this).find(".end_point_relation").attr("id");
            });
            // $(el_panel_collapsed).addClass('activate');

            var windows = document.getElementById(id_el);
            make_Source(windows);
        });

        var el_all = $(e.target).closest(".all");
        var el_tbody = $(el_all).find(".for_edit>.ibox-content>.table>tbody");

        $.post( "/tree/for_edit_new_row/",{"max_id":max_id}).done(function( data ) {

            $(el_tbody).append($(data));

        });

        $(el_tbody).find("textarea").autosize();

            
    };


    $("body").on("click",".func_add_button",for_click_add);

    var scale = 1;
    var prop = 1;
    change_scale = function (e){
        
        var delta = e.deltaY || e.detail || e.wheelDelta;
        if (delta > 0) {
            scale += 0.1;
            prop+=1;
            }
        else{
            prop-=1;
            scale -= 0.1; 
        } 
        
        $('#main,._jsPlumb_endpoint,svg').juScale(scale);

        e.preventDefault();
        
    }

    $("textarea").autosize();        

    $(".new_ask").on("click",function(e){
        var newdiv = document.createElement('div');

        $.post( "/tree/new_ask/").done(function( data ) {

            $("#for_ajax").html(data);
            var $div = $("#for_ajax").find(".all");
            var poz = $(e.target).offset();

            poz.top = poz.top + 25;
            $div.offset(poz);
            $("#statemachine-demo").append($div);
            $($div).find("textarea").autosize();
            instance.draggable($div );
            make_collapsed($div);
            make_Target($div);
            // initialise all '.w' elements as connection targets.
            // instance.makeTarget($div, {
            //     dropOptions: { hoverClass: "dragHover" },
            //     // anchor: "AutoDefault", 
            //     // allowLoopback: true
            //     anchor:["Continuous", { faces:[ "right", "left" ] } ],
            //     });    
        });


    });

    $('body').on('click','.dell_all',function(e){

        instance.remove($(e.target).closest('.all').attr('id'));
    })
    $('body').on('click','.dell_quest',function(e){

        $quest_el = $(e.target).closest('.quest_el');
        var id_quest = $quest_el.find(".end_point_relation") .attr('id');
        
        $quest_el.detach();
        instance.remove(id_quest);
        // $(e.target).closest(".all").find(".head_collaps>.collaps").each(function(){
        //     instance.getConnections({source: $(this).attr("id")}).repaint();
        // });
        // instance.select().repaint();

    })

    var get_par_quest = function(inner_html){
       var val,atr,el ;
       el = $(inner_html).find("textarea");
       if (el.val()) {
          val = $(el).val().trim();
          atr = $(el).attr("model_field");
       };

       
       el = $(inner_html).find("input");
       if (el.val()) {
          
            val = $(el).attr("value").trim();
            atr = $(el).attr("model_field");
       };
         
       el = $(inner_html).find("p");
       if (el.val()) {
            return false
            // val = $(el).innerHTML;
            // atr = $(el).attr("model_field");
       };
       return {"atr":atr,"val":val}
    };

    $('.save_diagram').on('click',function(e){
        // var cont = {};
        // main_s = cont["main"] = [];
        // $.param({"traditional":true});
        main_s = {};
        // // 'choices[]': [ "Jon", "Susan" ] 
        $(".all").each(function(){
            
            var  dict_quest = {};
            $(this).find("tbody>tr").each(function(){

                var id_quest = $(this).find("td>p").html();
                var quest_attr =  { };
                // if (parseInt(id_quest) == 10900) {

                //     console.log(parseInt(id_quest));

                // }
                $(this).find("td").each(function(){

                    var set_dict = get_par_quest(this);
                    if (set_dict){
                        quest_attr[set_dict["atr"]] = set_dict["val"];
                    }
                });
                
                
                var con  = instance.getConnections({source:id_quest+"for_dot"});

                if (con.length){
                    quest_attr.question_answer = con[0].targetId;
                    
                };
                if (id_quest){
                    dict_quest[id_quest] = quest_attr;
                };

            });

            var text_answer = $(this).find(".input_text_sub").val().trim();
            main_s[$(this).attr('id')] = {"text_answer":text_answer, "questions":dict_quest};
                
        
        });
        
        $.post( "/tree/diagrama_save/",{"json_str":JSON.stringify(main_s)}).done(function( data ) {
        });
        
    });

    instance.bind("click", function (conn, originalEvent) {
            conn.toggleType("basic");
        });

    function make_con(){
       var $pair_con_s = $("#connectors .con"); 
       // pair_con_s =  main_el.querySelectorAll(".con");
       // for (var i = 0 ; i<pair_con_s.length; i++){

        $("#connectors .con").each(function(){
                var pair_con = this.children;
                instance.connect({source:pair_con[0].innerHTML+"for_dot", target:pair_con[1].innerHTML
                ,anchors:["Right", "Left"],
                // connectorStyle: { strokeStyle: "#000"},
               });
        });
        
    }
    make_con();

    $("body").on("click",".save_edit_all",function(e){

        var for_edit = $(e.target).closest(".for_edit");


        var text_ask = $(for_edit).find(".media-body>textarea").val().trim();

        var for_edit = $(e.target).closest(".all");

        $(for_edit).find(".pos_head_client>a").attr("title",text_ask);

        $(for_edit).find("tbody>tr").each(function(){
           var text_quest = $(this).find(".cell_ask_input>textarea").val().trim();
           var id_quest = $(this).find("td>p").html();
           $("#"+id_quest+"for_dot>a").attr("title",text_quest);
        });
    });

    var make_collapsed  = function(el){$( el ).tooltip({
      position: {
            // my: "top left ",
            at: "right+25"
          },
          show: {
            effect: "slideDown",
            delay: 350
          }
          // content: "Awesome title!"
        });
    }

    make_collapsed(".collapsed");

    $("input").each(function(){
        try{
            $(this).attr("value") = $(this).attr("value") .trim();
        } catch(e){

        };
    })

    $("body").on("click",".close_sub_form", function(e){
        
        remove_all_adit();
    });


    $("body").on("click",".dell_con",function(e){
        var $end_point_relation = $(e.target).closest(".head_collaps").find(".end_point_relation");
        var id  = $($end_point_relation).attr("id");
        var con =  instance.getConnections({source:id});

        instance.detach(con[0]);
    });

});
    