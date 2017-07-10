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

    // var i;
    // var increment_btns = $(".increment-btn");
    // var decrement_btns = $(".decrement-btn");
    // var hierachy_values = $(".hierachy-value");
    // console.log(hierachy_values);

    // for (i = 0; i < increment_btns.length; i++){
    //     increment_btns[i].click(function(){
    //         console.log(increment_btns)
    //         hierachy = hierachy_values[i].html();
    //         hierachy_values[i].html(hierachy++);
    //         console.log(hierachy)
    //     });
    // }
    //
    // for (i = 0; i < decrement_btns.length; i++){
    //     decrement_btns[i].click(function(){
    //         hierachy = hierachy_values[i].html();
    //         hierachy_values[i].html(hierachy--);
    //     });
    // }



    // $(".increment-btn").click(function(){
    //     $(".hierachy-value").html("clicked");
    //     console.log("Clicked");
    // });

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