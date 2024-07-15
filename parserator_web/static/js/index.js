/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
"use strict"
$(document).ready(function () {
  $("#address-form").submit(function (e) {
    e.preventDefault()

    var address = $("#address").val()
    $.ajax({
      url: "/api/parse/",
      type: "GET",
      data: {
        address: address,
      },
      success: function (response, status, xhr) {
        if (response.error) {
          $("#address-results").hide()
          $("#error-results").show()
          $("#parse-error").text(response.error)
        } else {
          $("#error-results").hide()
          $("#address-results").show()
          $("#parse-type").text(response.address_type)

          var addressTable = $("#address-results-table")
          addressTable.empty()

          $.each(response.address_components, function (key, value) {
            addressTable.append(
              $("<tr>").append($("<td>").text(key), $("<td>").text(value))
            )
          })
        }
      },
      error: function (xhr, status, error) {
        $("#address-results").hide()
        $("#error-results").show()
        $("#parse-error").text(xhr.responseJSON.error)
      },
    })
  })
})
