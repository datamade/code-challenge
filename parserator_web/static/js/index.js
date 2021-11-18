/* TODO: Flesh this out to connect the form to the API and render results
in the #address-results div. */

'use strict'

function successResults (data) {

  // If previous errors, hide the error div and show results only
  document.getElementById('error-results').style = "display:none"
  // Unhide the results table and grab the table element for results filling
  document.getElementById('address-results').style = "display:block"
  var oldTblBdy = document.querySelector('table.table tbody')
  var newTblBdy = document.createElement('tbody')

  var keys = Object.keys(data['address_components'])
  var componentLength = keys.length


  for (var i = 0; i < componentLength; i++) {

    // A bit verbose, but address component length will be variable based on user input
    // loop through all of the components and fill a new table to replace the old

    var row = document.createElement("tr")
    var addressCell = document.createElement("td")
    var addressPartText = document.createTextNode(data['address_components'][keys[i]])
    var tagCell = document.createElement("td")
    var tagPartText = document.createTextNode(keys[i])

    addressCell.appendChild(addressPartText)
    tagCell.append(tagPartText)
    row.appendChild(addressCell)
    row.appendChild(tagCell)

    newTblBdy.appendChild(row)
  }

  oldTblBdy.parentNode.replaceChild(newTblBdy, oldTblBdy)
}

function failedResults (data) {

  // If a previous parse exists, hide the address div
  document.getElementById('address-results').style = "display:none"

  var errorDiv = document.getElementById('error-results')

  errorDiv.style = "display:block"
  errorDiv.innerHTML = data.responseJSON.detail

}
 

// Add the API call to the submit button from the form
document.getElementById('submit').addEventListener('click',function (event) {

  event.preventDefault()

  $.ajax({
    url: '/api/parse/',
    datatype: 'json',
    type: 'GET',
    data: {
      input_string: document.getElementById('address').value
    },
    success: function (data) {
      successResults(data)
    },
    error: function (data) {
      failedResults(data)
    }
  })

})
