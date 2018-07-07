(function ($) { 
    'use strict';

    $(document).ready(function(){

        var html = '<span class="unselect" style="cursor:pointer;background-color:#ff0000;color:#fff;padding:5px 7px;margin-left:10px;border-radius:4px;">Unselect All</span>';
        $("div.related-widget-wrapper").append(html); 


        $("span.unselect").on("click", function(){
            $(this).parent().find("select option:selected").removeAttr("selected");
        });

    });

    // functions




})(django.jQuery);
