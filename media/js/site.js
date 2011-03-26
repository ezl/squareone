$(document).ready(function() {
  $(".success, .info, .warning, .error").click(
    function(event) {
      $(this).slideUp();
    }
  )
});
