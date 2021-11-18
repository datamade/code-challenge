/* TODO: Flesh this out to connect the form to the API and render results
in the #address-results div. */

'use strict'

function fillAddressResults (data) {

  // Unhide the results table and grab the table element for results filling
  document.getElementById('address-results').style = "display:block"
  var tblbdy = document.querySelector('table.table tbody')

  var keys = Object.keys(data['address_components'])
  var componentLength = keys.length


  for (var i = 0; i < componentLength; i++) {

    // A bit verbose, but address component length will be variable based on user input
    // loop through all of the components and fill the table

    var row = document.createElement("tr")
    var addressCell = document.createElement("td")
    var addressPartText = document.createTextNode(data['address_components'][keys[i]])
    var tagCell = document.createElement("td")
    var tagPartText = document.createTextNode(keys[i])

    addressCell.appendChild(addressPartText)
    tagCell.append(tagPartText)
    row.appendChild(addressCell)
    row.appendChild(tagCell)

    tblbdy.appendChild(row)
  }
}
 

// Add the API call to the submit button from the form
document.getElementById('submit').addEventListener('click',function (event) {

  event.preventDefault()

  $.ajax({
    url: 'http://localhost:8000/api/parse',
    datatype: 'json',
    type: 'GET',
    data: {
      input_string: document.getElementById('address').value
    },
    success: function (data) {
      fillAddressResults(data)
    }
  })

})
