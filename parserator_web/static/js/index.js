/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

'use strict'

document.addEventListener('DOMContentLoaded', function () {
   
  // Get the relevant page elements
  var addressForm = document.querySelector('form')
  var addressField = document.querySelector('#address')
  var addressResults = document.querySelector('#address-results')
  var parseType = document.querySelector('#parse-type')
  var addressTableBody = document.querySelector('tbody')

  // Parse and display address or error when form is submitted
  addressForm.onsubmit = function () {
    var addressInput = document.querySelector('#address').value

    // Clear the form field for the next attempt
    addressField.value = ''
    // Clear any prior errors
    if (document.querySelector('#error')) {
      document.querySelector('#error').remove()
    }
    // Clear any prior results 
    if (addressResults.style.display === 'block') {
      addressResults.style.display === 'none'
      var rows = addressTableBody.getElementsByTagName('tr')
      // Convert the NodeList to an array to avoid looping over a shrinking NodeList
      var rowsArray = Array.prototype.slice.call(rows)
      for (var i = 0; i < rowsArray.length; i++) {
        rowsArray[i].remove()
      }
    }

    fetch('api/parse/?input=' + addressInput)
      .then(function (response) {return response.json()})
      .then(function (data) {
        if (data.error) {
          // Display the error message
          var errorDiv = document.createElement('div')
          errorDiv.id = 'error'
          var error = document.createElement('h4')
          error.className = 'error'
          error.textContent = 'Error: ' + data.error
          var message = document.createElement('p')
          message.textContent = data.message
          errorDiv.append(error, message)
          document.querySelector('.container').append(errorDiv)
        } else {
          // Display the address type and components table
          var addressType = data.address_type
          parseType.textContent = addressType
          var addressComponents = data.address_components
          for (var component in addressComponents) {
            var row = document.createElement('tr')
            var addressPart = document.createElement('td')
            addressPart.textContent = addressComponents[component]
            var tag = document.createElement('td')
            tag.textContent = component
            row.append(addressPart, tag)
            addressTableBody.append(row)
          }
          // Unhide the results div
          addressResults.style.display = 'block'
        }
      })
    // Stop the form from actually submitting
    return false
  }
})
