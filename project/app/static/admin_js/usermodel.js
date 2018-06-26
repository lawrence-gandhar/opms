(function ($) { 
    'use strict';
    
    $(document).ready(function() {

        /* Edit Form Details Start */ 
        var pathname = window.location.pathname;
		var path_id = pathname.split("/");
        
        var user_details = "";

		if(path_id[path_id.length - 2] == "change"){
			
			var user_id = parseInt(path_id[path_id.length - 3]);
			
			$.post("/admin-userform-details/",{'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),"id":user_id},function(data){
                user_details = $.parseJSON(data);
                location_change($("select#id_location option:selected").val(), user_details);
            });
        }
        /* Edit Form Details End */ 



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
        Add a parent select for Department
        */
       $("select#id_department").before('<select style="margin-right:10px;" name="department_parents" id="id_department_parents"></select>')


        /*
        Populate department field on location change. 
        */

        $("select#id_location").change(function(){
            $("select#id_department_parents, select#id_department, select#id_designation,select#id_assigned_to").empty();
            location_change($("select#id_location").val(), user_details)
        });  

        /*
        Populate child department field on parent department change. 
        */

        $("select#id_department_parents").change(function(){
            //console.log(user_details);
            $("select#id_department, select#id_designation,select#id_assigned_to").empty();
            department_change($("select#id_department_parents").val(), user_details)
        });

        /*
        Populate child department field on parent department change. 
        */

        $("select#id_department").change(function(){
            $("select#id_designation,select#id_assigned_to").empty();
            designation_change($("select#id_department").val(), user_details)
        });
        
        /* 
        Dropdown values for already selected fields
        */   
       
    });

    function location_change(id, user_details){
        $.post("/location-select/",{'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),"id":id},function(data){
           
            var fetched_data = '<option value="">---------</option>';

            $.each($.parseJSON(data),function(i,v){
                if(user_details.parent_department == v.id)
                    fetched_data += '<option value="'+v.id+'" selected>'+v.name+' ( '+v.abbr+' )</option>';
                else
                    fetched_data += '<option value="'+v.id+'">'+v.name+' ( '+v.abbr+' )</option>';
            });

            $("select#id_department_parents").empty().html(fetched_data);
            department_change($("select#id_department_parents option:selected").val(), user_details);
        });
    }

    function department_change(id, user_details){
        $.post("/department-select/",{'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),"id":id},function(data){
            
            var fetched_data = '<option value="">---------</option>';

            $.each($.parseJSON(data),function(i,v){
                if(user_details.department_id == v.id)
                    fetched_data += '<option value="'+v.id+'" selected>'+v.name+' ( '+v.abbr+' )</option>';
                else
                    fetched_data += '<option value="'+v.id+'">'+v.name+' ( '+v.abbr+' )</option>';
            });

            $("select#id_department").empty().html(fetched_data);
            designation_change($("select#id_department option:selected").val(), user_details);
            user_list(user_details);
        });
    }

    function designation_change(id, user_details){
        $.post("/designation-select/",{'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),"id":id},function(data){
            
            var fetched_data = '<option value="">---------</option>';

            $.each($.parseJSON(data),function(i,v){
                if(user_details.designation_id == v.id)
                    fetched_data += '<option value="'+v.id+'" selected>'+v.name+' ( '+v.abbr+' )</option>';
                else
                    fetched_data += '<option value="'+v.id+'">'+v.name+' ( '+v.abbr+' )</option>';
            });

            $("select#id_designation").empty().html(fetched_data);
        });
    }


    function user_list(user_details){
        $.post("/admin-userform-list/",{'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),"id":$("select#id_department option:selected").val(), "usertype_id":$("select#id_usertype option:selected").val()},function(data){
            var fetched_data = '<option value="">---------</option>';

            $.each($.parseJSON(data),function(i,v){
                if(user_details.assigned_to_id == v.id)
                    fetched_data += '<option value="'+v.id+'" selected>'+v.name+'</option>';
                else
                    fetched_data += '<option value="'+v.id+'">'+v.name+'</option>';
            });

            $("select#id_assigned_to").empty().html(fetched_data);
        });
    }

})(django.jQuery);