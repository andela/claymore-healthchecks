/**
 * Created by dominicbett on 06/07/2017.
 */

$(function () {
    $("#add_stakeholder").click(function(e){
        var url = e.target.getAttribute("data-url");
        $("#stakeholder").attr("action", url);
        $("#update-stakeholder-modal").modal("show");
        return false;
    });
    
    $(".stake-holder-remove").click(function(e){
        url = e.target.getAttribute("data-url");
        name = e.target.getAttribute("data-name");
        $("#remove-stakeholder-form").attr("action", url);
        $(".remove-stakeholder-name").text(name);

        $("#remove-stakeholder-modal").modal("show");
        return false;
    });
});

function change_hierachy_value(value, st_id){
    //Updates the hierachy of a stakeholder.

    var hierachy_id = $('#'+st_id);
    var hierachy_value = hierachy_id.html();
    if (hierachy_value <= 0){
        if (value < 0){
            return false
        }
    }
    else if (hierachy_value >=6) {
        if (value > 0){
            return false
        }
    }
    hierachy_id.html( parseInt(hierachy_value) + value);
}