"use strict"

$(document).ready(function () {

  $("#submit").click(function (e) {

    // Prevent page from reloading on form submit
    e.preventDefault()

    // Clear any previous results
    $("#address-results tbody tr").remove()

    // Get value in address field
    var address = $("#address").val()

    // Make request to API to parse address
    $.ajax({
      type: 'GET',
      url: "/api/parse/",
      data: $("#address").serialize(),
      success: function (data) {

        // Add address type to HTML
        $("#parse-type").text(data["address_type"])

        // Add parse address components to HTML
        var components = data["address_components"]
        for (var address_part in components) {
          var address_tag = components[address_part]
          $("#address-results tbody").append("<tr>"
              + "<td>" + address_part + "</td>"
              + "<td>" + address_tag + "</td>"
              + "</tr>")
        };

        // Show results
        $("#address-results").show()
      },
      error: function (e) {
        // Hide results, display error
        $("#address-results").hide()

        alert(e["responseJSON"]["detail"])
      }
    })
  })
})
