/* Connects the form to the API and render results
   in the #address-results div. */

'use strict'

$('.form').on('submit', function (event) {
  event.preventDefault()
  submitAddress()
})

function submitAddress () {
  var address = getAddress()
  var url = "api/parse?address=" + getAddress()
  if (address === "") {
    writeError("Please enter an address.")
    return
  }
  try {
    $.get(url, function (data) {
      writeResults(data.address_type, data.address_components)
    }).fail(function (data) {
      writeError(data.responseJSON.detail)
    })
  } catch (error) {
    writeError("Something went wrong, please try again.")
  }
}

function getAddress () {
  var address = $("#address").val().trim()
  return encodeURIComponent(address)
}

function writeResults (addressType, addressComponents) {
  writeTextById("parse-type", addressType)
  writeAddressComponents(addressComponents)
  showSuccess()
}

function writeAddressComponents (addressComponents) {
  $("#address-parts").empty()
  for (var component in addressComponents) {
    if (Object.prototype.hasOwnProperty.call(addressComponents, component)) {
      var addressPart = addressComponents[component]
      var tag = component
      var row = '<tr><td>' + addressPart + '</td><td>' + tag + '</td></tr>'
      $("#address-parts").append(row)
    }
  }
}

function writeError (message) {
  writeTextById("error-message", message)
  showError()
}

function showSuccess () {
  hide("error")
  show("success")
  show("address-results")
}

function showError () {
  hide("success")
  show("error")
  show("address-results")
}

function show (id) {
  showOrHideById(id, true)
}

function hide (id) {
  showOrHideById(id, false)
}

function showOrHideById (id, show) {
  var setting = show ? '' : 'none'
  $("#" + id).css("display", setting)
}

function writeTextById (id, text) {
  $("#" + id).text(text)
}
