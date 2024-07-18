'use strict'

// TODO: We'll want to change this url in production, obviously
const url = "http://localhost:8000/api/parse"
const submitButton = document.getElementById("submit")

// We'll save the blank results html for use later
let blankTable = document.getElementById("address-table").innerHTML

submitButton.onclick = async function (event) {
  event.preventDefault()
  
  let results = document.getElementById("address-results")

  // We'll blank this out in case we get an error
  // So that we don't show old responses as if to new queries
  results.style.display = "none"
  
  let addressString = document.getElementById("address").value
  let queryTerms = new URLSearchParams({ address: addressString })
  try {
    const response = await fetch(`${url}?${queryTerms}`)
    console.log(response)
    if (!response.ok) {
      if (response.status == 400) {
        alert(`${response.statusText}: Failed to parse this address`)
      } else {
        // TODO: Handle other failures?
      }
    } else {
      let responseData = await response.json()

      // Set the headline
      document.getElementById("parse-type").textContent = responseData.address_type

      // Build the table
      let table = document.getElementById("address-table")
      table.innerHTML = blankTable
      let addressParts = responseData.address_components
      for (let index in addressParts) {
        let field = addressParts[index][0]
        let value = addressParts[index][1]

        let nextRow = table.insertRow(-1)
        let fieldData = nextRow.insertCell(0)
        let valueData = nextRow.insertCell(1)
  
        fieldData.appendChild(document.createTextNode(field))
        valueData.appendChild(document.createTextNode(value))
      }
      results.style.display = "block"
    }
  } catch (error) {
    console.error(`${error} in response to query at ${url}?{queryTerms}`)
  }
}
