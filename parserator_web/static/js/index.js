/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
'use strict'
function generateAddressTable (data) {
  document.getElementById("address-results").style.display = "block"
  if (data) {
    var table = Object.keys(data.address_components)
      .map(function (key) {
        return (
          "<tr><th>" +
          data.address_components[key] +
          "</th><th>" +
          key +
          "</th></tr>"
        )
      })
      .join("")

    return document.getElementById("address-results").innerHTML =
      '<h4>Parsing results:</h4><p>Address type: <strong><span id="parse-type">' +
      data.address_type +
      '</span></strong></p><table class="table table-bordered">' +
      '<thead><tr><th>Address part</th><th>Tag</th></tr></thead><tbody>' +
      table +
      "</tbody></table>"
  } else {
    return document.getElementById("address-results").innerHTML =
      "<h1>Address Not valid</h1>"
  }
}
