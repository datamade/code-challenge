"use strict"

document.addEventListener('DOMContentLoaded', function () {
  var form = document.getElementById('address-form')
  var resultsDiv = document.getElementById('address-results')
  var resultsBody = document.getElementById('results-body')
  var parseTypeSpan = document.getElementById('parse-type')
  var errorMessageDiv = document.getElementById('error-message')

  form.addEventListener('submit', function (event) {
    event.preventDefault()

    var addressInput = document.getElementById('address').value
    var url = 'api/parse/?address=' + encodeURIComponent(addressInput)

    fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(function (response) {
        if (!response.ok) {
          return response.json().then(function (errorData) {
            throw new Error(errorData.detail || 'An error occurred')
          })
        }
        return response.json()
      })
      .then(function (data) {
      // Clear previous results and error messages
        resultsBody.innerHTML = ''
        errorMessageDiv.style.display = 'none'
        resultsDiv.style.display = 'block'
        parseTypeSpan.innerText = data.address_type

        // Populate table with results
        for (var tag in data.address_components) {
          if (data.address_components.hasOwnProperty(tag)) {
            var part = data.address_components[tag]
            var row = document.createElement('tr')
            var tagCell = document.createElement('td')
            tagCell.innerText = tag
            var partCell = document.createElement('td')
            partCell.innerText = part
            row.appendChild(tagCell)
            row.appendChild(partCell)
            resultsBody.appendChild(row)
          }
        }
      })
      .catch(function (error) {
        console.error('Error:', error)
        resultsBody.innerHTML = ''
        parseTypeSpan.innerText = ''
        errorMessageDiv.innerText = error.message
        errorMessageDiv.style.display = 'block'
        resultsDiv.style.display = 'block'
      })
  })
})
