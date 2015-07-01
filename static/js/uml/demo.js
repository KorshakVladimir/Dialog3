jsPlumb.ready(function () {

    // setup some defaults for jsPlumb.
    // var instance = jsPlumb.getInstance({
    //     Endpoint: ["Dot", {radius: 2}],
    //     HoverPaintStyle: {strokeStyle: "#1e8151", lineWidth: 2 },
    //     ConnectionOverlays: [
    //         [ "Arrow", {
    //             location: 1,
    //             id: "arrow",
    //             length: 14,
    //             foldback: 0.8
    //         } ],
    //         [ "Label", { label: "FOO", id: "label", cssClass: "aLabel" }]
    //     ],
    //     Container: "statemachine-demo"
    // });


    // instance.init_ep = function () {
    //     instance.makeSource(windows, {
    //         filter: ".ep",
    //         anchor: "Continuous",
    //         connector: [ "StateMachine", { curviness: 20 } ],
    //         connectorStyle: { strokeStyle: "#5c96bc", lineWidth: 2, outlineColor: "transparent", outlineWidth: 4 },
    //         maxConnections: 5,
    //         onMaxConnections: function (info, e) {
    //             alert("Maximum connections (" + info.maxConnections + ") reached");
    //          }
    //      });

    //     // initialise all '.w' elements as connection targets.
    //     instance.makeTarget(windows, {
    //         dropOptions: { hoverClass: "dragHover" },
    //         anchor: "Continuous", 
    //         allowLoopback: true
    //     });

        

    // }

    // initialise = ( function (){
    //         instance.batch(instance.init_ep);
    //     });

    // initialise();

    // ----------------------------------------------------------------------------------------
    var instance = jsPlumb.getInstance({
        // default drag options
        DragOptions: { cursor: 'pointer', zIndex: 2000 },
        // the overlays to decorate each connection with.  note that the label overlay uses a function to generate the label text; in this
        // case it returns the 'labelText' member that we set on each connection in the 'init' method below.
        ConnectionOverlays: [
            [ "Arrow", { location: 1 } ],
            [ "Label", {
                location: 0.1,
                id: "label",
                cssClass: "aLabel"
            }]
        ],
        Container: "flowchart-demo"
    });

    var basicType = {
        connector: "StateMachine",
        paintStyle: { strokeStyle: "red", lineWidth: 4 },
        hoverPaintStyle: { strokeStyle: "blue" },
        overlays: [
            "Arrow"
        ]
    };
    instance.registerConnectionType("basic", basicType);
    // this is the paint style for the connecting lines..
   // this is the paint style for the connecting lines..
    var connectorPaintStyle = {
            lineWidth: 4,
            strokeStyle: "#61B7CF",
            joinstyle: "round",
            outlineColor: "white",
            outlineWidth: 2
        },
    // .. and this is the hover style.
        connectorHoverStyle = {
            lineWidth: 4,
            strokeStyle: "#216477",
            outlineWidth: 2,
            outlineColor: "white"
        },
        endpointHoverStyle = {
            fillStyle: "#216477",
            strokeStyle: "#216477"
        },
    // the definition of source endpoints (the small blue ones)
        sourceEndpoint = {
            endpoint: "Dot",
            paintStyle: {
                strokeStyle: "#7AB02C",
                fillStyle: "transparent",
                radius: 7,
                lineWidth: 3
            },
            isSource: true,
            connector: [ "Flowchart", { stub: [40, 60], gap: 10, cornerRadius: 5, alwaysRespectStubs: true } ],
            connectorStyle: connectorPaintStyle,
            hoverPaintStyle: endpointHoverStyle,
            connectorHoverStyle: connectorHoverStyle,
            dragOptions: {},
            // overlays: [
            //     [ "Label", {
            //         location: [0.5, 1.5],
            //         label: "Drag",
            //         cssClass: "endpointSourceLabel"
            //     } ]
            // ]
        },
    // the definition of target endpoints (will appear when the user drags a connection)
        targetEndpoint = {
            endpoint: "Dot",
            paintStyle: { fillStyle: "#7AB02C", radius: 11 },
            hoverPaintStyle: endpointHoverStyle,
            maxConnections: -1,
            dropOptions: { hoverClass: "hover", activeClass: "active" },
            isTarget: true,
            // overlays: [
            //     [ "Label", { location: [0.5, -0.5], label: "Drop", cssClass: "endpointTargetLabel" } ]
            // ]
        },
        init = function (connection) {
            connection.getOverlay("label").setLabel(connection.sourceId.substring(15) + "-" + connection.targetId.substring(15));
        };
    var _addEndpoints = function (toId, sourceAnchors, targetAnchors) {
        for (var i = 0; i < sourceAnchors.length; i++) {
            var sourceUUID = toId + sourceAnchors[i];
            instance.addEndpoint(toId, sourceEndpoint, {
                anchor: sourceAnchors[i], uuid: sourceUUID
            });
        }
        for (var j = 0; j < targetAnchors.length; j++) {
            var targetUUID = toId + targetAnchors[j];
            instance.addEndpoint(toId, targetEndpoint, { anchor: targetAnchors[j], uuid: targetUUID });
        }
    };

    // ----------------------------------------------------------------------------------------
    
    
    
    window.jsp = instance;

    var main_block = jsPlumb.getSelector(".statemachine-demo .all");
    var windows = jsPlumb.getSelector(".statemachine-demo .w, .klient_section");



    // initialise draggable elements.
    instance.draggable(main_block);

    var draggable_all = function(){

       instance.draggable($(".all")); 
    };
    draggable_all();
    // instance.draggable(jsPlumb.getSelector(".statemachine-demo .window"), { grid: [20, 20] });
    // bind a click listener to each connection; the connection is deleted. you could of course
    // just do this: jsPlumb.bind("click", jsPlumb.detach), but I wanted to make it clear what was
    // happening.
    
    // instance.bind("click", function (c) {
    //     instance.detach(c);
    // });

    // bind a connection listener. note that the parameter passed to this function contains more than
    // just the new connection - see the documentation for a full list of what is included in 'info'.
    // this listener sets the connection's internal
    // id as the label overlay's text.
    instance.bind("connection", function (info) {
        info.connection.getOverlay("label").setLabel(info.connection.id);
    });


    // suspend drawing and initialise.
    
    
    var countid = 10; 

    jsPlumb.fire("jsPlumbDemoLoaded", instance);

    

    // add_butt = function(parentEl) {
    //    var ev_button = document.createElement('button');   
    //    ev_button.innerHTML = "<i class=\"fa fa-plus\"></i>";
    //    ev_button.setAttribute("class", "add_button button_diag");
       
    //    parentEl.appendChild(ev_button);
    // }

    for_click_rem = function(e){
        e.target.parentElement.remove();
    }

    butt_remove = function(parentEl) {
       var ev_button = document.createElement('button');   
       ev_button.innerHTML = "<i class=\"fa fa-trash-o\"></i>";
       // ev_button.setAttribute("class", "but_rem");
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

    click_for_edit = function  (e) {
        remove_all_adit();
        e.stopPropagation();
        var el_panel_demo = e.target.closest(".head_section");
        var el_edit = el_panel_demo.querySelector(".for_edit") ;
        
        $(el_edit).toggleClass("active_form");
    }

    // var edit_quest_el_s = jsPlumb.getSelector(".edit_quest");

    // for (var i = 0 ; i<edit_quest_el_s.length; i++){
    //     var edit_quest_el = edit_quest_el_s[i];
    //     edit_quest_el.addEventListener( "click",click_for_edit);
    // }

    $("body").on("click",".edit_quest",click_for_edit);

    // ------------------------------------------------

    click_for_edit_all = function  (e) {
        remove_all_adit();
        e.stopPropagation();
        var el_klient_section = e.target.closest(".klient_section");
        var el_edit = el_klient_section.querySelector(".for_edit") ;
        
        $(el_edit).toggleClass("active_form");
    }

    // var edit_answer_el_s = jsPlumb.getSelector(".edit_answer");

    // for (var i = 0 ; i<edit_answer_el_s.length; i++){
    //     var edit_answer_el = edit_answer_el_s[i];
    //     edit_answer_el.addEventListener( "click",click_for_edit_all);
    // }
    $("body").on("click",".edit_answer",click_for_edit_all);
    // ------------------------------------------------

    // var for_edit_el_s =  jsPlumb.getSelector(".for_edit");

    // for (var i = 0 ; i<for_edit_el_s.length; i++){
    //     var for_edit_el = for_edit_el_s[i];
        // for_edit_el.addEventListener( "click",function(e){
        //     e.stopPropagation();
        // });
    // }
    $("body").on("click",".for_edit",function(e){
            e.stopPropagation();
        }
    );




    butt_edit = function(parentEl) {
       var ev_button = document.createElement('button');   
       ev_button.innerHTML = "Edit";
       // ev_button.setAttribute("class", "but_rem");
       ev_button.cssClass = "but_edit";

       ev_button.addEventListener( "click",click_for_edit);

       parentEl.appendChild(ev_button);
    }

    add_place_edit = function(parentEl){
       var place_edit = document.createElement('div');   
       // ev_button.innerHTML = "-";
       // place_edit.setAttribute("class", "for_edit hide_el");
       place_edit.className = "for_edit hide_el";

       // ev_button.addEventListener( "click",for_click_rem );

       parentEl.appendChild(place_edit);
    }
     

    //initialise el_w
    // var el_w = jsPlumb.getSelector(".w");
    // for (var i = 0 ; i<el_w.length; i++){
    //     var el = el_w[i];
    //     // butt_remove(el); 
    //     // butt_edit(el);
    //     add_place_edit(el);
    // }

    

    //initialise el all
    // var el_s_head_client = jsPlumb.getSelector(".consultant");
    // for (var i = 0 ; i<el_s_head_client.length; i++){
    //     var el_all = el_s_head_client[i];
    //     add_butt(el_all); 
        
    // };

    var rem_all_collaps = function(el_col){
        var collapsed_el_s = jsPlumb.getSelector(".collaps");
        for (var i = 0 ; i < collapsed_el_s.length; i++){
            var el = collapsed_el_s[i]
            if (el_col != el){
            $(el).removeClass("activate"); 
            }
        };      
    }

    var click_collapsed = function(e){
        var this_col =  e.target.closest(".head_collaps").querySelector(".collaps");
        rem_all_collaps(this_col);
        var id = this.getAttribute("child");
        var $id = $(id); 
        $(id).toggleClass("activate");
        $input_text = $id.find(".input_text")
        resize_text_area.call($input_text[0]);
        // place_holder.setAttribute("style","");
        
    };

    // collapsed_el_s = jsPlumb.getSelector(".collapsed");

    // for (var i = 0 ; i < collapsed_el_s.length; i++){
    //     collapsed_el_s[i].addEventListener( "click",click_collapsed);        
    // };

    $('body').on("click",".collapsed", click_collapsed);

    for_click_add = function(e){
            
        var parrent_el = e.target.closest(".consultant").querySelector(".section_question");

        var block_q = jsPlumb.getSelector("#new_questions")[0];

        var newdiv = document.createElement('div');

        var id_el = ++countid;
        
        var enter_id = "#"+countid+"ans";

        newdiv.setAttribute("id", id_el );
        
        newdiv.innerHTML = block_q.innerHTML;

        var a_el =  newdiv.querySelector('.collapsed');       

        a_el.setAttribute("child",enter_id);
        
        var el_span = newdiv.querySelector('.head_section');

        // <a child="#108397002ans" class="collapsed">
                
        //     <span class="head_section client "> 108397002 </span>
        //     <span class="badge_down"> 
        //         <i class="fa fa-sort-desc"></i>
        //     </span>
                 
        // </a>
        el_span.innerText = id_el;

        var el_panel_collapsed = newdiv.querySelector(".collaps");
        el_panel_collapsed.setAttribute("id",enter_id.slice(1));
        rem_all_collaps();
        $(el_panel_collapsed).addClass('activate');
        parrent_el.appendChild(newdiv, parrent_el.lastElementChild);

        windows = document.getElementById(id_el);
        // initialise();
    }

    // var button_el_s = jsPlumb.getSelector(".add_button");

    $("body").on("click",".add_button",for_click_add);

    // for (var i = 0 ; i<button_el_s.length; i++){
    //     button_el = button_el_s[i];
    //     button_el.addEventListener( "click",for_click_add );
    // }   

    // $(function() {
    // $( "#statemachine-demo" ).draggable({ containment: "main" });
    // });

    // instance.draggable(main_block);
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
        
        // canv.style.transform = canv.style.WebkitTransform  = canv.style.MsTransform= "scale("+scale+")";
        // canv.style.transform = translateY(1000*scale+"px");
        $('#main,._jsPlumb_endpoint,svg').juScale(scale);
        // $(canv).css('transform', 'translateY('+ 100+"px" +')');
        // canv.style.left = 20px;
        e.preventDefault();
        
    }
    // canv.addEventListener( "wheel",change_scale );
    

    function resize_text_area(el) {
       
        var cont = this.value.trim();
       
        var need_height = Math.max(10,cont.length)*1.3;
        $(this).css({'height':'auto','overflow-y':'hidden'}).height(need_height);
    }   

    // $('.input_text').each(function () {
    //     resize_text_area(this);
    //     }
    // ).on('input', function () {
    //   resize_text_area(this);
    //     }
    // );
        
    $("body").on("input",".input_text",resize_text_area);
        
    // function make_con(){
    //    var main_el = jsPlumb.getSelector("#connectors")[0]; 
    //    pair_con_s =  main_el.querySelectorAll(".con");
    //    // for (var i = 0 ; i<pair_con_s.length; i++){
    //     for (var i = 0 ; i<10; i++){
    //         var pair_con = pair_con_s[i];
    //         pair_con.children[0];
    //         instance.connect({source:pair_con.children[0].innerText, target:pair_con.children[1].innerText
    //             ,anchors:["Right", "Left"],});
    //    }
    // }
    // make_con()
    $(".new_ask").on("click",function(e){
        var newdiv = document.createElement('div');
        // var newdiv;
        $(newdiv).load("/tree/new_ask/",draggable_all);
        $("#statemachine-demo").append(newdiv);
        
    });

    // suspend drawing and initialise.
    instance.batch(function () {
        var main_el = jsPlumb.getSelector(".all"); 
        for (var i = 0 ; i<main_el.length; i++){

           // _addEndpoints(main_el[i].id, [], [[1, 0, 0, 0,0,40],[0,0,0,0,0,40]]);
           // _addEndpoints(main_el[i].id, [], []);
        }

        // var main_el_w = jsPlumb.getSelector(".text_head_client"); 
        var main_el_w = jsPlumb.getSelector(".end_point_relation");
        for (var i = 0 ; i < main_el_w.length; i++){

            // _addEndpoints(main_el_w[i].id, [[1,0,0,0,16,15]], []);
           
        }
        // listen for new connections; initialise them the same way we initialise the connections at startup.
        instance.bind("connection", function (connInfo, originalEvent) {
            init(connInfo.connection);
        });

        // make all the window divs draggable
        // instance.draggable(jsPlumb.getSelector(".flowchart-demo .window"), { grid: [20, 20] });
        // THIS DEMO ONLY USES getSelector FOR CONVENIENCE. Use your library's appropriate selector
        // method, or document.querySelectorAll:
        //jsPlumb.draggable(document.querySelectorAll(".window"), { grid: [20, 20] });

        // connect a few up
        // instance.connect({uuids: ["Window2BottomCenter", "Window3TopCenter"], editable: true});
        // instance.connect({uuids: ["Window2LeftMiddle", "Window4LeftMiddle"], editable: true});
        // instance.connect({uuids: ["Window4TopCenter", "Window4RightMiddle"], editable: true});
        // instance.connect({uuids: ["Window3RightMiddle", "Window2RightMiddle"], editable: true});
        // instance.connect({uuids: ["Window4BottomCenter", "Window1TopCenter"], editable: true});
        // instance.connect({uuids: ["Window3BottomCenter", "Window1BottomCenter"], editable: true});
        //

        //
        // listen for clicks on connections, and offer to delete connections on click.
        //
        instance.bind("click", function (conn, originalEvent) {
           // if (confirm("Delete connection from " + conn.sourceId + " to " + conn.targetId + "?"))
             //   instance.detach(conn);
            conn.toggleType("basic");
        });

        instance.bind("connectionDrag", function (connection) {
            console.log("connection " + connection.id + " is being dragged. suspendedElement is ", connection.suspendedElement, " of type ", connection.suspendedElementType);
        });

        instance.bind("connectionDragStop", function (connection) {
            console.log("connection " + connection.id + " was dragged");
        });

        instance.bind("connectionMoved", function (params) {
            console.log("connection " + params.connection.id + " was moved");
        });
    });

    // instance.connect({source:"108297001", target:"1083"});
});
