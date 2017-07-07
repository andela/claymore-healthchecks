/**
 * Created by dominicbett on 06/07/2017.
 */

$(function () {
    $("#add_stakeholder").click(function(e){
        var url = e.target.getAttribute("data-url");
        // var code = window.location.href.split('/')[5];
        // $("#stakeholder").attr("action", "/stakeholders/add/"+code+"/");
        $("#stakeholder").attr("action", url);
        $("#update-stakeholder-modal").modal("show");
        return false;
    });
});