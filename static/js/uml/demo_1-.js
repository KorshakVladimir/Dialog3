jsPlumb.ready(function () {

    // setup some defaults for jsPlumb.
    var instance = jsPlumb.getInstance({
        Endpoint: ["Dot", {radius: 2}],
        HoverPaintStyle: {strokeStyle: "#1e8151", lineWidth: 2 },
        ConnectionOverlays: [
            [ "Arrow", {
                location: 1,
                id: "arrow",
                length: 14,
                foldback: 0.8
            } ],
            [ "Label", { label: "FOO", id: "label", cssClass: "aLabel" }]
        ],
        Container: "statemachine-demo"
    });


    instance.init_ep = function () {
        instance.makeSource(windows, {
            filter: ".ep",
            anchor: "Continuous",
            connector: [ "StateMachine", { curviness: 20 } ],
            connectorStyle: { strokeStyle: "#5c96bc", lineWidth: 2, outlineColor: "transparent", outlineWidth: 4 },
            maxConnections: 5,
            onMaxConnections: function (info, e) {
                alert("Maximum connections (" + info.maxConnections + ") reached");
             }
         });

        // initialise all '.w' elements as connection targets.
        instance.makeTarget(windows, {
            dropOptions: { hoverClass: "dragHover" },
            anchor: "Continuous", 
            allowLoopback: true
        });

        

    }

    initialise = ( function (){
            instance.batch(instance.init_ep);
        });

    initialise();

    
    
    
    
    window.jsp = instance;

    var main_block = jsPlumb.getSelector(".statemachine-demo .all");
    var windows = jsPlumb.getSelector(".statemachine-demo .w, .klient_section");


    // initialise draggable elements.
    instance.draggable(main_block);
     instance.draggable(jsPlumb.getSelector(".statemachine-demo .all")) 

    // bind a click listener to each connection; the connection is deleted. you could of course
    // just do this: jsPlumb.bind("click", jsPlumb.detach), but I wanted to make it clear what was
    // happening.
    instance.bind("click", function (c) {
        instance.detach(c);
    });

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

    

    add_butt = function(parentEl) {
       var ev_button = document.createElement('button');   
       ev_button.innerHTML = "<i class=\"fa fa-plus\"></i>";
       ev_button.setAttribute("class", "add_button button_diag");
       
       parentEl.appendChild(ev_button);
    }

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

    var canv =  jsPlumb.getSelector("#statemachine-demo")[0];
    canv.addEventListener( "click",remove_all_adit );


    click_for_edit = function  (e) {
        remove_all_adit();
        e.stopPropagation();
        parrent_el = e.target.parentElement;
        var el_edit = parrent_el.querySelector(".for_edit");
        $(el_edit).toggleClass("active_form");
    }

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
    var el_w = jsPlumb.getSelector(".w");
    for (var i = 0 ; i<el_w.length; i++){
        var el = el_w[i];
        // butt_remove(el); 
        // butt_edit(el);
        add_place_edit(el);
    }

    

    //initialise el all
    var el_s_head_client = jsPlumb.getSelector(".consultant");
    for (var i = 0 ; i<el_s_head_client.length; i++){
        var el_all = el_s_head_client[i];
        add_butt(el_all); 
        
    };

    for_click_add = function(e){
            
        var parrent_el = e.target.closest(".consultant");

        var block_a = jsPlumb.getSelector(".block_answers")[0];

        var newdiv = document.createElement('div');

        var id_el = countid++;
        newdiv.setAttribute("id", id_el );
        newdiv.className = "w block_answers jsplumb-droppable";
        newdiv.innerHTML = block_a.innerHTML;
        newdiv.querySelector('.input_text').innerText = "";

        parrent_el.appendChild(newdiv, parrent_el.lastElementChild);

        windows = document.getElementById(id_el)
        initialise();
    }

    var button_el_s = jsPlumb.getSelector(".add_button");

    for (var i = 0 ; i<button_el_s.length; i++){
        button_el = button_el_s[i];
        button_el.addEventListener( "click",for_click_add );
    }   

    $(function() {
    $( "#statemachine-demo" ).draggable({ containment: "main" });
    });

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
    canv.addEventListener( "wheel",change_scale );
    

    function resize_text_area(e) {
        $(e).css({'height':'auto','overflow-y':'hidden'}).height(e.scrollHeight);
    }

    $('.input_text').each(function () {
      resize_text_area(this);
    }).on('input', function () {
      resize_text_area(this);
    });


    function make_con(){
       var main_el = jsPlumb.getSelector("#connectors")[0]; 
       pair_con_s =  main_el.querySelectorAll(".con");
       // for (var i = 0 ; i<pair_con_s.length; i++){
        for (var i = 0 ; i<10; i++){
            var pair_con = pair_con_s[i];
            pair_con.children[0];
            instance.connect({source:pair_con.children[0].innerText, target:pair_con.children[1].innerText
                ,anchors:["Right", "Left"],});
       }
    }
    make_con()

    // instance.connect({source:"108297001", target:"1083"});
});
