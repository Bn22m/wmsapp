//
//binarysearch.js
//@ Author: Brian
//

function binarySearchCat(v, list, x, b) {
  console.log("BS: "+v+", ", x, b);
  return searchCat(v, list, 0, list.length, x, b);
}

function searchCat(v, list, l, r, x, b){
  console.log("v: "+v+", l : "+l+", r: "+r+", x:"+x+", b: "+b );
  if(r <= l){
    return -1;
  }
  var mid = Math.floor((l + r)/2);
  console.log("mid: "+mid, list[mid][x][b]);
  if (v > list[mid][x][b]) {
    return searchCat(v, list, mid+1, r, x, b);
  }
  else if (v < list[mid][x][b]) {
    return searchCat(v, list, l, mid, x, b);
  }
  else {
    return mid;
  }
}

function mergeSortCat(a, x, b) {
  console.log("mergeSortCat: ", a, x, b);
	return pmgSort(a, 0, a.length-1, x, b);
}

function pmgSort(a, left, right, x, b) {
  var mid;
  console.log(left," : ", right);
	if (left < right) {
	mid = Math.floor((left + right)/2);
	a = pmgSort(a, left, mid, x, b);
	a = pmgSort(a, mid+1, right, x, b);
	a = pmerge(a, left, mid, right, x, b);
  console.log(left," #: ", a[left][x][b]);
  console.log(mid," #: ", a[mid][x][b]);
  console.log(right," #: ", a[right][x][b]);
	}
	return a;
}

function pmerge(a, low, mid, high, x, b) {
  //console.log(low,":", mid,":", high,":", a[low][x][b])
	var temp = [];
	var left = low;
  var right = mid+1;
  var count = 0;

  while(left <= mid && right <= high) {
    console.log("left: "+left+", x: "+x+", b: "+b, "right: "+right)
	  if (a[left][x][b] <= a[right][x][b])
	  temp[count++] = a[left++];
	  else
	  temp[count++] = a[right++];
  }

  while(left <= mid)
	  temp[count++] = a[left++];
  while(right <= high)
	  temp[count++] = a[right++];

  for (var k = 0; k < temp.length; k++)
	  a[low+k] = temp[k];

	return a;
}
