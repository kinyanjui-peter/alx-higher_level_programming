// jquery script
$(document).ready(function () {
    const element = $('header');
  
    if (element) {
      // use css to set color
      element.css('color', '#FF0000');
    } else {
      console.error('Header element not found');
    }
  });
