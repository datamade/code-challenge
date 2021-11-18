"use strict"

// Run when Parse! button is clicked
function parse (e) {

  e.preventDefault()

  // Get refrences to page elements
  var address = document.getElementsByName("address")[0].value
  var address_type = document.getElementById("parse-type")
  var error_div = document.getElementById("error_div")
  var table_body = document.getElementsByTagName("tbody")[0]
  var results_div = document.getElementById("address-results")

  var xmlhttp = new XMLHttpRequest()

  // Only make an API request if there is an address string.
  if (address) {
    xmlhttp.open("GET", "api/parse" + "?" + "address=" + address)
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    xmlhttp.send(null)
  }
  // Remove any elements from previous API calls.
  else {
    buildTable([], table_body)
    address_type.innerHTML = ''
    results_div.style.display="none"
  }
  // Remove API error message if present
  if (error_div) {
    results_div.removeChild(error_div)
  }

  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState == XMLHttpRequest.DONE) {

      var res = JSON.parse(xmlhttp.response)
      results_div.style.display="contents"

      // Show the response on a successful API call.
      if (xmlhttp.status == 200) {
        var components = res["address_components"]
        address_type.innerHTML = res["address_type"]
        table_body.parentNode.replaceChild(buildTable(components), table_body)
      }

      // Show the error message on unsuccessful calls.
      else if (xmlhttp.status == 400) {
        table_body.parentNode.replaceChild(buildTable([]), table_body)
        var error_div = document.createElement("div")
        error_div.setAttribute("id", "error_div")
        error_div.innerHTML = res["detail"]
        results_div.prepend(error_div)
      }
    }
  }
}

/**
 * Returns a table body containing parsed address compoents
 * or an empty table body.
 * @param {array} components 
 * @returns {object} <tbody> element
 */
function buildTable (components) {
  var table = document.createElement("tbody")
  for (var component in components) {
    var row = document.createElement("tr")
    var part = document.createElement("td")
    var tag = document.createElement("td")
    part.innerHTML = components[component]
    tag.innerHTML = component
    row.append(part)
    row.append(tag)
    table.appendChild(row)
  }
  return table
}

// Get the form and listen for button clicks.
var form = document.querySelector("form")
form.addEventListener("submit", parse)