// for csrftoken



var cook = (name)=>{
    let cookieValue = null;
    if(document.cookie && document.cookie !== ''){
        var cooki = document.cookie.split(";");
        for(let i = 0; i < cooki.length; i++){
            var cookie = cooki[i].trim();
            // does this cookie string begin with the name we want?
            if (cookie.substring(0,name.length + 1)===(name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// for sending ajax requests
var AjaxRequestPost=(data,onsuccess,onerror,url)=>{
    data.append('csrfmiddlewaretoken',tok)
    data.forEach(element => {
        console.log(element);
    })
    $.ajax({
        type:'POST',
        url: url,
        data:data,
        cache:false,
        processData:false,
        contentType:false,
        enctype:'multipart/form-data',
        success: (response)=>{
            onsuccess(response)
           },
        error:(error)=>{
            onerror(error)
           }

           
    })
}
// jquery plugin to prevent double submission
// jquery351Min.fn.preventDoubleSubmission = (form)=>{
//     $(this).on('submit',)
// }
var tok = cook('csrftoken');
var student_form = $("#student_form");
student_form.submit((e)=>{
    document.getElementById("s_submit").disabled=true;
    e.preventDefault();
    var formData =  new FormData();
    formData.append('firstname',$('#firstname').val()),
    formData.append('lastname',$('#lastname').val()),
    formData.append('dob',$('#dob').val()),
    formData.append('gender',$('#gender').val()),
    formData.append('photo',$('#photo')[0].files[0]),
    formData.append('age',$('#age').val()),
    formData.append('class',$('#class').val())
    formData.append('unique_ref',$('#photo')[0].files[0].lastModified)
    var success = (response)=>{
       
            console.log(response.data)
            $("#student_info").addClass('d-none').fadeOut(1000)
            $("#parent_info").removeClass('d-none').fadeIn(1000)
            $("#g-hide").val(response.std_id)
            setTimeout(document.getElementById("s_submit").disabled=false,1000); 
     
       
    }
    var error = (error)=>{
        console.log(error)
    }
    var url = '/student/register-student/'
    AjaxRequestPost(data=formData,onsuccess=success,onerror=error,url=url)
})
var parent_form = $("#parent_form");
parent_form.submit((e)=>{
    document.getElementById("p_submit").disabled=true;
    e.preventDefault();
    var formData =  new FormData();
    formData.append('name',$('#name').val()),
    formData.append('email',$('#email').val()),
    formData.append('phone',$('#phone').val()),
    formData.append('p_photo',$('#p_photo')[0].files[0]),
    formData.append('gender',$('#gender').val()),
    formData.append('p_age',$('#p_age').val()),
    formData.append('guardian',$('#g-hide').val())
    formData.append('address',$('#address').val())
    formData.append('unique_ref',$('#p_photo')[0].files[0].lastModified)
    var success = (response)=>{
            console.log(response.data)
            setTimeout(document.getElementById("p_submit").disabled=false,1000);
            $("#p_submit").addClass('d-none')
            $("#inv").removeClass("d-none")
            $("#ant").removeClass("d-none") 
            $("#inv").attr('href',`/student/student-detail/${response.std_id}`)
            $("#ant").click(()=>{
                $("#p_submit").removeClass('d-none')
                $("#inv").addClass("d-none")
                $("#ant").addClass("d-none") 
            }) }
    var error = (error)=>{
        console.log(error)
    }
    var url = '/student/register-parent/'
    AjaxRequestPost(data=formData,onsuccess=success,onerror=error,url=url)
})


// ajaxCall({'pk':id,'quantity':1},`/add-to-cart/`,'POST',onsuccess,onerror)  