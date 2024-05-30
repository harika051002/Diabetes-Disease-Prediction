function clearInputValue(input) {
    input.value = '';  // Clear the input value when it gains focus
  }

  // Remove the value attribute after the page has loaded
  document.addEventListener('DOMContentLoaded', function() {
    var pregnanciesInput = document.getElementById('pregnanciesInput');
    pregnanciesInput.removeAttribute('value');
  });
  
  
  function togglePregnancyField() {
    var gender = document.getElementById('gender').value;
    console.log("Gender: " + gender);
    var pregnanciesField = document.getElementById('b');
    var pregnanciesInput = document.getElementById('pregnanciesInput');

    if (gender === 'male') {
      pregnanciesInput.value = 0;
      pregnanciesInput.readOnly = true; // Make the field readonly
    } else {
      pregnanciesInput.value = ''; // Clear the value for females
      pregnanciesInput.readOnly = false; // Make the field editable for females
    }

     // Show/hide the pregnancies field based on gender
     pregnanciesField.style.display = (gender === 'female') ? 'block' : 'none';
  }


  function checkFields(f1) {
    console.log("Form submitted!");
    if (f1.t1.value  < 0 || f1.t1.value > 2500) {
      alert("Please Enter valid Glucose Level");
      f1.t1.focus();
      return false;
    }

    if (f1.gender.value === 'female' && (f1.t2.value < 0 || f1.t2.value > 20)) {
      alert("Please Enter valid Pregnancies Data");
      f1.t2.focus();
      return false;
    }

    if (isNaN(f1.t3.value) || f1.t5.value < 0 || f1.t5.value > 450) {
      alert("Please Enter Valid Weight");
      f1.t5.focus();
      return false;
    }

    if (isNaN(f1.t4.value) || f1.t4.value < 1 || f1.t4.value > 8) {
      alert("Please Enter Valid Height");
      f1.t5.focus();
      return false;
    }

    if (isNaN(f1.t5.value) || f1.t5.value < 20 || f1.t5.value > 90) {
      alert("Please Enter Valid Age");
      f1.t6.focus();
      return false;
    }

    return true;
  }