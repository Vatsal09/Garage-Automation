//crsf - needed for Django internal form validation when submitting forms through ajax
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//post to removeVehicle implemented with ajax
function removeVehicle(accountId,pk,licensePlate){
    var answer = confirm("Remove " + licensePlate + "?");
    if (answer){
        $.ajax({
            'url': "/garageAutomation/home/",
            'type': 'POST',
            'data':{
                'csrfmiddlewaretoken':getCookie('csrftoken'),
                'removeVehicle': 'true',
                'account_id':accountId, 
                'license_plate':licensePlate,
                'vehicle_pk':pk
            },
            'success': function(result){
            location.reload();
        }});
    }
}

function deleteAccount(accountId){
    var answer = confirm("Are you sure you want to delete your account?");
    if (answer){
        $.ajax({
            'url': "/garageAutomation/home/",
            'type': 'POST',
            'data':{
                'csrfmiddlewaretoken':getCookie('csrftoken'),
                'deleteAccount': 'true',
                'account_id':accountId, 
            },
            'success': function(result){
            window.location = "/garageAutomation/logout"; //log out of session
        }});
    }
}