/* TODO: Pretty Print Error messages */
'use strict'
$(document).ready(function () {
  var addrResults = $('#address-results')
  var errorResults = $('#error-results')
  addrResults.hide()
  errorResults.hide()

  var frm = $("#address-form")
  frm.submit(function (e) {
    e.preventDefault()
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
        //$('#address-table').children('tbody').html(tableData);
        addrResults.show()
      },
      error: function (error)
      {
        //Would like to review this at some point to do some type 
        //of pretty print for error text
        errorText = JSON.parse(error.responseText)['error']
        //Hopefully no addresses use html tags, but I think this should be good
        //for the time being to do a basic pretty print
        errorText = errorText.replace(/(?:\r\n|\r|\n)/g, '<br>')
        $('#error-type').html(errorText)
        errorResults.show()
      },
    })
  })

   
})