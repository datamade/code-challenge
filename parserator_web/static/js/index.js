'use strict'

function successFunction (data) {
  $("#address-results").show()
  $("#error-results").hide()
  $("#parse-type").text(data.address_type)

  var address_array = Object.entries(data.address_components)

  // clear table of any previous results
  $(".table tbody").html("")

  // add each element to table
  for (var i = 0; i < address_array.length; i++) {
    $(".table tbody").append(
      "<tr><td>" +
        address_array[i][1] +
        "</td><td>" +
        address_array[i][0] +
        "</td></tr>"
    )
  }
}

function errorFunction (data) {
  $("#error-results").html(data.responseJSON.detail)
  $("#address-results").hide()
  $("#error-results").show()
}

$("#submit").on("click", function (event) {
  event.preventDefault()

  // created js obj
  var data = { input_string: $("#address").val() }

  $.ajax({
    url: "/api/parse/",
    datatype: "json",
    type: "GET",
    data: data,
    success: function (data) {
      successFunction(data)
    },
    error: function (data) {
      errorFunction(data)
    },
  })
})
