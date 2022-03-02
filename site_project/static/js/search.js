function myfunction(){
   var a=document.getElementById('search-k').value.toUpperCase()
   var b=document.getElementById('card-lists')
   var c=document.getElementsByClassName('card h-100')
   for(let i=0; i <c.length; i++){
     let title=c[i].querySelector('.card-body a.card-title')
     console.log(title)
     if(title.innerText.toUpperCase().indexOf(a) > -1){
       c[i].style.display=""
     }else{
       c[i].style.display="none"
     }
   }
 }