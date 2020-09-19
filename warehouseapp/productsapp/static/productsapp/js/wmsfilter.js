//
//wmsfilter.js
//@ Author: Brian
//

function wmsFilterCat(list, x, y, b, v, presults){
  console.log("wmsFilter: "+x, ", y: "+ y+", b: "+b+", v:"+v);
  if(list[x][y][b] == v){
    console.log(list);
    wmFilter(list, x, y, b, v, presults);
  }
}

function wmFilter(list, x, y, b, v, presults){
  var d1 = new Date();
  console.log("wmFilter: "+x, ", y: "+ y+", b: "+b+", v:"+v+", prs: "+presults);
  var list1 = [];
  var list2 = []
  for(var i = x-1; i >= 0; i--){
    if(list[i][y][b] == v){
      list1.push(list[i]);
    }
    else {
      break;
    }
    console.log("wmFilter: "+i, list[i]);
  }
  for(var i = x; i < list.length; i++){
    if(list[i][y][b] == v){
      list1.push(list[i]);
    }
    else{
      break;
    }
    console.log("wmFilter: "+i, list[i]);
  }
  console.log("list2: ", list2.length);
  list2 = mergeSortCat(list1, y, b);
  var d2 = new Date();
  var d3 = d2 - d1;
  console.log("list2: ", list2.length+", @"+d3);
  if(list2.length > 0){
    wmsResults(list2, presults, v);
  }
}

function wmsResults(list, txtresults, info){
  var db2 = JSON.stringify(list);
  txtresults.value = db2;
  displayResults(list, info);
}

function displayResults(dvlist, info){
  var dvdisplay = document.getElementById("dvdisplay");
  var header = ["productID", "productName", "supplierID",
    "categoryID", "quantityPerUnit", "unitPrice", "unitsInStock",
    "unitsOnOrder", "reorderLevel", "discontinued", 'info'];
  displayResultsApp(dvdisplay, dvlist, header, info);
}

//
//overloading
//

function wmsFilterSup(list, x, y, v, presults){
  console.log("wmsFilter: "+x, ", y: "+y+", v: "+v);
  if(list[x][y] == v){
    console.log(list);
    wmFilterSup(list, x, y, v, presults);
  }
}

function wmFilterSup(list, x, y, v, presults){
  var d1 = new Date();
  console.log("wmFilterSup: "+x, ", y: "+ y+", v:"+v+", prs: "+presults);
  var list1 = [];
  var list2 = []
  for(var i = x-1; i >= 0; i--){
    if(list[i][y] == v){
      list1.push(list[i]);
    }
    else {
      break;
    }
    console.log("wmFilterSup: "+i, list[i]);
  }
  for(var i = x; i < list.length; i++){
    if(list[i][y] == v){
      list1.push(list[i]);
    }
    else{
      break;
    }
    console.log("wmFilterSup: "+i, list[i]);
  }
  console.log("list2: ", list2.length);
  list2 = mergeSortSup(list1, y);
  var d2 = new Date();
  var d3 = d2 - d1;
  console.log("list2: ", list2.length+", @"+d3);
  if(list2.length > 0){
    wmsResults(list2, presults, v);
  }
}
