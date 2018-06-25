(function ($) { 
    'use strict';
    
    $(document).ready(function() {
       /*
       # Setting field order in the admin user form. 
       */     

        var field_username = '<div class="form-row field-username">'+$(".field-username").html()+"</div>";
        var field_last_login = '<div class="form-row field-last_login">'+$(".field-last_login").html()+"</div>";
        var field_user_permissions = '<div class="form-row field-user_permissions">'+$(".field-user_permissions").html()+"</div>";
        var field_groups = '<div class="form-row field-groups">'+$(".field-groups").html()+'</div>';
        var field_date_joined = '<div class="form-row field-date_joined">'+$(".field-date_joined").html()+'</div>';
        var field_is_superuser = '<div class="form-row field-is_superuser">'+$(".field-is_superuser").html()+'</div>';

        $(".field-username").remove();
        $(".field-last_login").remove();
        $(".field-user_permissions").remove();
        $(".field-groups").remove();
        $(".field-date_joined").remove();
        $(".field-is_superuser").remove();

        $(".field-password").before(field_username);
        $(".field-is_staff").after(field_user_permissions).after(field_groups);
        $(".field-assigned_to").after(field_date_joined);
        $(".field-date_joined").after(field_last_login);
        $(".field-email").after(field_is_superuser);

        $(".field-user_permissions").hide();
        $(".field-groups").hide();

        
        /*
        # Since super user designates that this user has all permissions without explicitly assigning them. 
        # if is_admin is selected, will hide permissions and group dowdowns.
        # Else if_staff, show permissions and group dowdowns.
        */

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

        /* 
        Default values set to blank in select fields
        */

        $("select#id_department").empty();
        $("select#id_designation").empty();

        /* 
        Add a parent select for Deparment
        */
       $("select#id_department").before('<select style="margin-right:10px;" name="department_parents" id="id_department_parents"></select>')


        /*
        Populate department field on location change. 
        */

        $("select#id_location").change(function(){

            $("select#id_department_parents, select#id_department, select#id_designation,select#id_assigned_to").empty();

            $.post("/location-select/",{'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),"id":$(this).val()},function(data){
               
                var fetched_data = '<option value="" selected="">---------</option>';

                $.each($.parseJSON(data),function(i,v){
                    console.log(v);
                    fetched_data += '<option value="'+v.id+'">'+v.name+' ( '+v.abbr+' )</option>';
                });

                $("select#id_department_parents").empty().html(fetched_data);

            });
        });  
        
        /*
        Populate child department field on parent department change. 
        */

        $("select#id_department_parents").change(function(){
            $("select#id_department, select#id_designation,select#id_assigned_to").empty();

            $.post("/department-select/",{'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),"id":$(this).val()},function(data){
            
                var fetched_data = '<option value="" selected="">---------</option>';

                $.each($.parseJSON(data),function(i,v){
                    console.log(v);
                    fetched_data += '<option value="'+v.id+'">'+v.name+' ( '+v.abbr+' )</option>';
                });

                $("select#id_department").empty().html(fetched_data);

            });
        });

        /*
        Populate child department field on parent department change. 
        */

        $("select#id_department").change(function(){
            $("select#id_designation,select#id_assigned_to").empty();

            $.post("/designation-select/",{'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),"id":$(this).val()},function(data){
            
                var fetched_data = '<option value="" selected="">---------</option>';

                $.each($.parseJSON(data),function(i,v){
                    console.log(v);
                    fetched_data += '<option value="'+v.id+'">'+v.name+' ( '+v.abbr+' )</option>';
                });

                $("select#id_designation").empty().html(fetched_data);

            });
        });        
    });

})(django.jQuery);