$(document).ready(function() {
  $('#createCustomerForm').validate({
    rules: {
      name: {
        required: true,
        minlength: 2,
        maxlength: 200
      },
      // Add more rules for other form fields if needed
    },
    messages: {
      name: {
        required: "Please enter a name",
        minlength: "Name must be at least 2 characters long",
        maxlength: "Name cannot exceed 200 characters"
      },
      // Add more messages for other form fields if needed
    },
    submitHandler: function(form) {
      form.submit(); // Submit the form if it's valid
    }
  });
});
