/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
$(document).ready(function() {
   var frm = $("#addrForm");
   frm.submit(function(e){
      e.preventDefault();
      var urlAddr =frm.attr('action');
      $.ajax({
         url: urlAddr,
         type: "GET",
         data: frm.serialize(),
         success: function(data)
         {
            alert(data);
         },
         error: function(data)
         {
            alert(data);
         },
      });
   });
});