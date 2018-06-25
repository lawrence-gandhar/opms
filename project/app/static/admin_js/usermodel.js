(function ($) { 
    'use strict';
    
    $(document).ready(function() {
       /*
       # Setting field order in the admin user form. 
       # Since super user designates that this user has all permissions without explicitly assigning them. 
       # if is_admin is selected, will hide permissions and group dowdowns.
       # Else if_staff, show permissions and group dowdowns.
       */     

        var user_permissions = '<div class="form-row field-user_permissions">'+$(".field-user_permissions").html()+"</div>";
        var field_groups = '<div class="form-row field-groups">'+$(".field-groups").html()+'</div>';

        $(".field-user_permissions").remove();
        $(".field-groups").remove();

        $(".field-is_staff").after(user_permissions).after(field_groups);

        $(".field-user_permissions").hide();
        $(".field-groups").hide();

        $('[name="is_staff"]').change(function()
        {
            if ($(this).is(':checked')) {
                $(".field-user_permissions").show();
                $(".field-groups").show();
            }else{
                $(".field-user_permissions").hide();
                $(".field-groups").hide();
            }
        });

        $('[name="is_superuser"]').change(function()
        {
            $('#id_is_staff').prop("checked",false);
            $(".field-user_permissions").hide();
            $(".field-groups").hide();
        });

    });

})(django.jQuery);