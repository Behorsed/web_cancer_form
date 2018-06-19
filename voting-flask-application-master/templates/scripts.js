

function setAction (element,value) {
  switch (value){
    case "kobieta":
  document.getElementById('dziex').style.display = 'none';
          document.getElementById('dalej').style.display = 'block';
    break;
    case "mezczyzna":
        document.getElementById('dalej').style.display = 'none';
      document.getElementById('dziex').style.display = 'block';
      document.getElementById('sexForm').action = "../templates/index.html";
    break;
    case "formView":
    window.location.href = "/raw";
    document.getElementById('sexForm').action = "../templates/raw.html";
    element.form.submit();

  }
}

//<script type="text/javascript">

function show(id,value) {
switch(id){
case "partnerzy":
    if (value=="0") {
        document.getElementById('sexWiek').style.display = 'none';
        document.getElementById('ciaza').style.display = 'none';
        document.getElementById('sexWiek').required=false;
        document.getElementById('ciaza').required=false;

    } else {
      document.getElementById('sexWiek').style.display = 'block';
      document.getElementById('ciaza').style.display = 'block';
       document.getElementById('sexWiek').style.visibility = 'visible';
        document.getElementById('ciaza').style.visibility = 'visible';
        document.getElementById('ciaza').required=true;

    }
break;
case "ciaza":
  if (value=="0"){
    document.getElementById('ciazaWiek').style.display = 'none';
        document.getElementById('ciazaWiek').required=false;
  } else {
    document.getElementById('ciazaWiek').style.display = 'block';
    document.getElementById('ciazaWiek').style.visibility = 'visible';
    document.getElementById('ciaza').required=true;
  }
  break;

  case "chorzyHPV":
  if(value=="Tak"){
    document.getElementById('HPV').style.display='block';
    document.getElementById('HPV').style.visibility='visible';
    document.getElementById('HPV').required=true;
  }else{
    document.getElementById('HPV').style.display='none';
    document.getElementById('HPV').required=false;
  }
break;
  }

}
//</script>
