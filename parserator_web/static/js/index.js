/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */

'use strict'
document.addEventListener('DOMContentLoaded', function () {
  
  function getAPI (event) {
      
    event.preventDefault()
    var parseForm = document.forms['parse-form']
    var apiAddress = parseForm['action']
    var address = parseForm.address.value
    apiAddress = apiAddress + "?" + "address=" + address
      
    fetch(apiAddress)
      .then(function (response) { 
        return response.json()
      })
      .then(function (data) {
        if (data.error) {
          document.querySelector('#address-results').style = "display: none"  
          var errorDiv = document.querySelector('#error-results')  
          errorDiv.style = "display: block"  
          errorDiv.innerHTML = data.error  
        } 
        else {
          document.querySelector('#error-results').style = "display: none"
          var inputString = data.input_string
          var addressComponents = data.address_components
          var addressType = data.address_type
          document.querySelector('#address-results').style = "display: block"
          document.querySelector('#parse-type').innerHTML = addressType
          var newTbody = document.createElement('tbody')


          Object.keys(addressComponents).forEach(function (item) {
            var tr = newTbody.insertRow()

            var td = tr.insertCell()
            td.innerText = item
            var td2 = tr.insertCell()
            td2.innerText = addressComponents[item]
          })
          // Overwrites table data each new search
          var tbody = document.querySelector('tbody')
          tbody.parentNode.replaceChild(newTbody, tbody)
        }
         
      })
      .catch(function (error) {
        console.log(error)
      })         
  }

  var parseForm = document.forms['parse-form']
  parseForm.addEventListener('submit', getAPI)
})
