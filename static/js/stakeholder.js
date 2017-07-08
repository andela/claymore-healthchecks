/**
 * Created by dominicbett on 06/07/2017.
 */

$(function () {
    hierachy = $(".hierachy-value").html();
    $("#add_stakeholder").click(function(e){
        var url = e.target.getAttribute("data-url");
        $("#stakeholder").attr("action", url);
        $("#update-stakeholder-modal").modal("show");
        return false;
    });

    $("#increment-btn").click(function(e){
        if (hierachy >= 6){
            $("#increment-btn").attr('disabled', 'disabled');
        }
        else if(hierachy < 6){
            $("#increment-btn").removeAttr('disabled')
            $(".hierachy-value").html(hierachy++)
        }
    });

    $("#decrement-btn").click(function(e){
        if (hierachy <= 0){
            $("#decrement-btn").attr('disabled', 'disabled');
        }
        else if(hierachy > 0){
            $("#decrement-btn").removeAttr('disabled');
            $(".hierachy-value").html(hierachy--)
        }
    });

    $(".stake-holder-remove").click(function(e){
        url = e.target.getAttribute("data-url");
        name = e.target.getAttribute("data-name");
        $("#remove-stakeholder-form").attr("action", url);
        $(".remove-stakeholder-name").text(name)

        $("#remove-stakeholder-modal").modal("show");
        return false;
    });
});
