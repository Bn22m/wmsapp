//
//displayapp.js
//@ Author: Brian
//
var search22 = document.getElementById("searchp");
var dvinfo22 = document.getElementById("dvinfo2");

function displayResultsApp(dvdisplay, dvlist, header, info){
  dvdisplay.innerHTML = "<hr><br><h1>"+info+"</h1>";
  var table = document.createElement("table");
  var tr = table.insertRow(-1);
  var v1;
  var v2;
  var v3;
  var v4;
  var v5;
  for(var i = 0; i < header.length; i++){
    var th = document.createElement("th");
    th.innerHTML = header[i];
    tr.appendChild(th);
  }
  for(var i = 0; i < dvlist.length; i++){
    tr = table.insertRow(-1);
    for(var j = 0; j < header.length; j++){
      var td = tr.insertCell(-1);
      if (j < header.length - 1){
        td.innerHTML = dvlist[i][header[j]];
        if(j == 2){
          td.innerHTML = dvlist[i].supplierID;
        }
        else if(j == 3){
          td.innerHTML = dvlist[i].categories.categoryID;
        }
      }
      else {
        v1 = dvlist[i][header[0]];
        v2 = dvlist[i].supplierID;
        v3 = dvlist[i].categories.categoryID;
        v4 = dvlist[i].categories.picture;
        td.innerHTML = '<input type="text" id="info'+i+'" value="'+info+'" readonly />';
        td.innerHTML += '<input type="text" id="pro'+i+'" value="'+v1+'" hidden />';
        td.innerHTML += '<input type="text" id="sup'+i+'" value="'+v2+'" readonly />';
        td.innerHTML += '<input type="text" id="cat'+i+'" value="'+v3+'" readonly />';
        td.innerHTML += '<button onclick="info2('+i+');">Info'+i+'</button>';
        var td2 = tr.insertCell(-1);
        td2.innerHTML = '<div class="dvcpic1"><img src="/static/'+v4+'" alt="wms"></div>';
      }
    }
    if(i == 0 & (search22.value == "category")){
      v5 = "<p>"+dvlist[i].categories.categoryName+"</p>";
      v5 += "<p>"+dvlist[i].categories.description+"</p>";
      dvinfo22.innerHTML = v5;
    }
    else if(i == 0 & (search22.value == "supplier")){
      v5 = "<p><b>"+dvlist[i].supplierID+"</b></p>";
      dvinfo22.innerHTML = v5;
    }
  }
  dvdisplay.appendChild(table);
  dvdisplay.innerHTML = dvdisplay.innerHTML + "<br><hr><br>";
}

function info2(pindex){
  var dvinfo = document.getElementById("dvinfo");
  var infolist = document.getElementById("info"+pindex);
  var txtsup = document.getElementById("sup"+pindex);
  var txtcat = document.getElementById("cat"+pindex);
  dbprogres.value = 5;
  var vc = infolist.value;
  var infop = "<h1>"+vc+"</h1>";
  if(vc == "Categories"){
    infop += "<p>"+txtcat.value+"</p>";
    productFilterT(txtcat.value, 'category')
  }
  else if(vc == "Suppliers"){
    infop += "<p>"+txtsup.value+"</p>";
    productFilterT(txtsup.value, 'supplier')
  }
  dvinfo.innerHTML = infop;
  //
  console.log("@# info: "+pindex, infop);
}
