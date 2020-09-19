//
//mergesort.js
//@ Author: Brian
//

function mergeSortSup(a, x) {
  console.log("cmergeSort: ", a, x);
	return mgSort(a, 0, a.length-1, x);
}

function mgSort(a, left, right, x) {
  var mid;
  console.log(left," : ", right);
	if (left < right) {
	mid = Math.floor((left + right)/2);
	a = mgSort(a, left, mid, x);
	a = mgSort(a, mid+1, right, x);
	a = merge(a, left, mid, right, x);
  console.log(left," #: ", a[left][x]);
  console.log(mid," #: ", a[mid][x]);
  console.log(right," #: ", a[right][x]);
	}
	return a;
}

function merge(a, low, mid, high, x) {
  console.log(low,":", mid,":", high,":\n", a[low][x])
	var temp = [];
	var left = low;
  var right = mid+1;
  var count = 0;

  while(left <= mid && right <= high) {
	  if (a[left][x] <= a[right][x])
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

function binarySearchSup(v, list, x) {
  console.log("BS: "+v+", ", x);
  return searchSup(v, list, 0, list.length, x);
}

function searchSup(v, list, l, r, x){
  console.log("v: "+v+", l : "+l+", r: "+r+", x:"+x );
  if(r <= l){
    return -1;
  }
  var mid = Math.floor((l + r)/2);
  console.log("mid: "+mid, list[mid][x]);
  if (v > list[mid][x]) {
    return searchSup(v, list, mid+1, r, x);
  }
  else if (v < list[mid][x]) {
    return searchSup(v, list, l, mid, x);
  }
  else {
    return mid;
  }
}
