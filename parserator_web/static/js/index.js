/* TODO: Pretty Print Error messages */
'use strict'
$(document).ready(function () {
  var addrResults = $('#address-results')
  var errorResults = $('#error-results')
  var frm = $("#address-form")

  frm.submit(function (e) {
    e.preventDefault()
    
    addrResults.hide()
    errorResults.hide()

    var urlAddr =frm.attr('action')
    $.ajax({
      url: urlAddr,
      type: "GET",
      data: frm.serialize(),
      success: function (data)
      {
        var tableData = ''
        var input_string = data['input_string']
        var address_type = data['address_type']
        $('#parse-type').text(address_type)

        $.each(data['address_components'], function (key,value) {

          tableData += '<tr>'
          tableData += '<td>' + key + '</td>'
          tableData += '<td>' + value + '</td>'
          tableData += '</tr>'
        })
        addrResults.children('table').children('tbody').html(tableData)
        addrResults.show()
      },
      error: function (error)
      {
        var errorFull = JSON.parse(error.responseText)['error']
        var errorType = JSON.parse(error.responseText)['error_type']

        var errorMessage = "ERROR: The address was not able to be parsed due to a "+errorType+". Please try again with a different input!"
        //Hopefully no addresses use html tags, but I think this should be good
        //for the time being for the full error message.
        errorFull = errorFull.replace(/(?:\r\n|\r|\n)/g, '<br>')
        $('#error-type').html(errorMessage)
        $('#error-full').html(errorFull)
        errorResults.show()
      },
    })
  })

   
})