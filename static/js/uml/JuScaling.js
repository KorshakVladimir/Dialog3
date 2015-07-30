/* Ju scaling module
 * © http://darkslave.net/
*/


(function($){
  var stylesBasic = [
    'font-size',
    'line-height',
    'letter-spacing',
    'text-indent',
    'width',
    'height',
    'margin-top',
    'margin-right',
    'margin-bottom',
    'margin-left',
    'padding-top',
    'padding-right',
    'padding-bottom',
    'padding-left',
    'border-top-width',
    'border-right-width',
    'border-bottom-width',
    'border-left-width',
    'border-top-left-radius',
    'border-top-right-radius',
    'border-bottom-left-radius',
    'border-bottom-right-radius'
  ];

  var stylesInner = [
    'top',
    'right',
    'bottom',
    'left'
  ];

  var regStyle = /^([0-9.+\-]+)(.*?)$/;


  function getcss($this, origin, styles){
    var n = styles.length, i, c, v, p;
    for(i = 0; i < n; i++){
      c = styles[i];
      v = $this.css(c) || "";
      if(!v.length)
        continue;

      p = v.match(regStyle);
      if(!p || !p.length)
        continue;

      origin[c] = {
        value:  parseFloat(p[1]) || 0.0,
        suffix: p[2]
      };
    }
  }


  function setcss($this, origin, styles, factor){
    var n = styles.length, i, c, p;
    for(i = 0; i < n; i++){
      c = styles[i];
      p = origin[c];

      if(typeof p == 'object')
        $this.css(c, (p.value * factor) + p.suffix);

    }
  }


  function gather(is_inner){
    var $this = $(this);

    if($this.data('juScale.origin'))
      return;

    var origin = {};

    if(is_inner){
      getcss($this, origin, stylesBasic);
      getcss($this, origin, stylesInner);
    }else{
      getcss($this, origin, stylesBasic);
    }

    $this.data('juScale.origin', origin);
  }


  function affect(factor, is_inner){
    var $this  = $(this);
    var origin = $this.data('juScale.origin');

    if(typeof origin != 'object')
      return;

    if(is_inner){
      setcss($this, origin, stylesBasic, factor);
      setcss($this, origin, stylesInner, factor);
    }else{
      setcss($this, origin, stylesBasic, factor);
    }

    $this.data('juScale.factor', factor);
  }


  $.fn.juScale = function(factor){

    this.find('*').each(function(){
      gather.call(this, true);
    });

    this.each(function(){
      gather.call(this, false);
    });

    if(typeof factor == 'undefined')
      return this.data('juScale.factor');

    factor = parseFloat(factor) || 0.0;

    if(factor <= 0.0)
      return this;

    this.find('*').each(function(){
      affect.call(this, factor, true);
    });

    this.each(function(){
      affect.call(this, factor, false);
    });

    return this;
  };

})(jQuery);



