
  function checkFields(f1) {
    console.log("Form submitted!");
    if (f1.t1.value  < 1 || f1.t1.value > 200) {
      alert("Please Enter valid Age");
      f1.t1.focus();
      return false;
    }

    if (!(f1.t2.value == 0 || f1.t2.value == 1)) {
      alert("Please Enter Gender either 0 or 1");
      f1.t2.focus();
      return false;
    }

    if (!(f1.t3.value == 0 || f1.t3.value == 1)) {
        alert("Please Enter Polyuria either 0 or 1");
        f1.t3.focus();
        return false;
      }

      if (!(f1.t4.value == 0 || f1.t4.value == 1)) {
        alert("Please Enter Polydipsia either 0 or 1");
        f1.t4.focus();
        return false;
      }

      if (!(f1.t5.value == 0 || f1.t5.value == 1)) {
        alert("Please Enter Partial Paresis either 0 or 1");
        f1.t5.focus();
        return false;
      }

      if (!(f1.t6.value == 0 || f1.t6.value == 1)) {
        alert("Please Enter Sudden Weight Loss either 0 or 1");
        f1.t6.focus();
        return false;
      }

      if (!(f1.t7.value == 0 || f1.t7.value == 1)) {
        alert("Please Enter Irritability either 0 or 1");
        f1.t7.focus();
        return false;
      }

      if (!(f1.t8.value == 0 || f1.t8.value == 1)) {
        alert("Please Enter Delayed Healing either 0 or 1");
        f1.t8.focus();
        return false;
      }

      if (!(f1.t9.value == 0 || f1.t9.value == 1)) {
        alert("Please Enter Alopecia either 0 or 1");
        f1.t9.focus();
        return false;
      }

      if (!(f1.t10.value == 0 || f1.t10.value == 1)) {
        alert("Please Enter Itching either 0 or 1");
        f1.t10.focus();
        return false;
      }
      if (!(f1.t11.value == 0 || f1.t11.value == 1)) {
        alert("Please Enter Genital thrush either 0 or 1");
        f1.t11.focus();
        return false;
      }
      if (!(f1.t12.value == 0 || f1.t12.value == 1)) {
        alert("Please Enter Visual Blurring either 0 or 1");
        f1.t12.focus();
        return false;
      }
      if (!(f1.t13.value == 0 || f1.t13.value == 1)) {
        alert("Please Enter Muscle Stiffness either 0 or 1");
        f1.t13.focus();
        return false;
      }
      if (!(f1.t14.value == 0 || f1.t14.value == 1)) {
        alert("Please Enter  Obesity either 0 or 1");
        f1.t14.focus();
        return false;
      }
      if (!(f1.t15.value == 0 || f1.t15.value == 1)) {
        alert("Please Enter Weakness either 0 or 1");
        f1.t15.focus();
        return false;
      }
      if (!(f1.t16.value == 0 || f1.t16.value == 1)) {
        alert("Please Enter Increased Appetite either 0 or 1");
        f1.t16.focus();
        return false;
      }

    return true;
  }